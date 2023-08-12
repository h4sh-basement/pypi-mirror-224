#
# Copyright (c) 2014-2015 Sylvain Peyrefitte
#
# This file is part of rdpy3.
#
# rdpy3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

"""
Transport packet layer implementation

Use to build correct size packet and handle slow path and fast path mode
"""
import asyncio
import ssl

from rdpy3.core.nla import cssp, sspi
from rdpy3.model.layer import RawLayer
from rdpy3.model.message import UInt8, UInt16Be, sizeof, Stream
from rdpy3.model.error import CallPureVirtualFuntion

class Action:
    """
    @see: http://msdn.microsoft.com/en-us/library/cc240621.aspx
    @see: http://msdn.microsoft.com/en-us/library/cc240589.aspx
    """
    FASTPATH_ACTION_FASTPATH = 0x0
    FASTPATH_ACTION_X224 = 0x3


class SecFlags:
    """
    @see: http://msdn.microsoft.com/en-us/library/cc240621.aspx
    """
    FASTPATH_OUTPUT_SECURE_CHECKSUM = 0x1
    FASTPATH_OUTPUT_ENCRYPTED = 0x2


class IFastPathListener(object):
    """
    @summary:  Fast path packet listener
                Usually X224 layer
    """
    def recvFastPath(self, secFlag, fastPathS):
        """
        @summary: Call when fast path packet is received
        @param secFlag: {SecFlags}
        @param fastPathS: {Stream}
        """
        raise CallPureVirtualFuntion("%s:%s defined by interface %s"%(self.__class__, "recvFastPath", "IFastPathListener"))
    
    def initFastPath(self, fastPathSender):
        """
        @summary: initialize stack
        @param fastPathSender: {IFastPathSender}
        """
        self.setFastPathSender(fastPathSender)
        fastPathSender.setFastPathListener(self)
    
    def setFastPathSender(self, fastPathSender):
        """
        @param fastPathSender : {IFastPathSender}
        """
        raise CallPureVirtualFuntion("%s:%s defined by interface %s"%(self.__class__, "setFastPathSender", "IFastPathListener"))
    
class IFastPathSender(object):
    """
    @summary: Fast path send capability
    """
    def sendFastPath(self, secFlag, fastPathS):
        """
        @summary: Send fastPathS Type as fast path packet
        @param secFlag: {integer} Security flag for fastpath packet
        @param fastPathS: {Type | Tuple} type transform to stream and send as fastpath
        """
        raise CallPureVirtualFuntion("%s:%s defined by interface %s"%(self.__class__, "sendFastPath", "IFastPathSender"))
    
    def initFastPath(self, fastPathListener):
        """
        @summary: initialize stack
        @param fastPathListener: {IFastPathListener}
        """
        self.setFastPathListener(fastPathListener)
        fastPathListener.setFastPathSender(self)
        
    def setFastPathListener(self, fastPathListener):
        """
        @param fastPathListener: {IFastPathListener}
        """
        raise CallPureVirtualFuntion("%s:%s defined by interface %s"%(self.__class__, "setFastPathListener", "IFastPathSender"))



class Tpkt(RawLayer, IFastPathSender):
    """
    @summary:  TPKT layer in RDP protocol stack
                represent the Raw Layer in stack (first layer)
                This layer only handle size of packet and determine if is a fast path packet
    """

    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def readHeader(self, data):
        """
        @summary: Read header of TPKT packet
        @param data: {Stream} received from twisted layer
        """
        #first read packet version
        version = UInt8()
        data.read_type(version)
        #classic packet
        if version.value == Action.FASTPATH_ACTION_X224:
            #padding
            data.read_type(UInt8())
            #read end header
            self.expect(2, self.readExtendedHeader)
        else:
            #is fast path packet
            self._secFlag = ((version.value >> 6) & 0x3)
            data.read_type(self._lastShortLength)
            if self._lastShortLength.value & 0x80:
                #size is 1 byte more
                self.expect(1, self.readExtendedFastPathHeader)
                return
            self.expect(self._lastShortLength.value - 2, self.readFastPath)
                
        
    def readExtendedHeader(self, data):
        """
        @summary: Header may be on 4 bytes
        @param data: {Stream} from twisted layer
        """
        #next state is read data
        size = UInt16Be()
        data.read_type(size)
        self.expect(size.value - 4, self.readData)
    
    def readExtendedFastPathHeader(self, data):
        """
        @summary: Fast path header may be on 1 byte more
        @param data: {Stream} from twisted layer
        """
        leftPart = UInt8()
        data.read_type(leftPart)
        self._lastShortLength.value &= ~0x80
        packetSize = (self._lastShortLength.value << 8) + leftPart.value
        #next state is fast patn data
        self.expect(packetSize - 3, self.readFastPath)
    
    def readFastPath(self, data):
        """
        @summary: Fast path data
        @param data: {Stream} from twisted layer
        """
        self._fastPathListener.recvFastPath(self._secFlag, data)
        self.expect(2, self.readHeader)
    
    def readData(self, data):
        """
        @summary: Read classic TPKT packet, last state in tpkt automata
        @param data: {Stream} with correct size
        """
        #next state is pass to 
        self._presentation.recv(data)
        self.expect(2, self.readHeader)
        
    async def write(self, message):
        """
        @summary: Send encompassed data
        @param message: {network.Type} message to send
        """
        s = Stream()
        s.write_type((UInt8(Action.FASTPATH_ACTION_X224), UInt8(0), UInt16Be(sizeof(message) + 4), message))
        self.writer.write(s.getvalue())
        await self.writer.drain()

    async def read(self):
        """
        Read an entire payload from the reader stream
        """
        header = Stream(await self.reader.readexactly(2))
        action = UInt8()
        header.read_type(action)
        if action.value == Action.FASTPATH_ACTION_X224:
            # read padding
            header.read_type(UInt8())

            size = UInt16Be()
            Stream(await self.reader.readexactly(2)).read_type(size)
            return Stream(await self.reader.readexactly(size.value - 4))


    def sendFastPath(self, secFlag, fastPathS):
        """
        @param fastPathS: {Type | Tuple} type transform to stream and send as fastpath
        @param secFlag: {integer} Security flag for fastpath packet
        """
        RawLayer.send(self, (UInt8(Action.FASTPATH_ACTION_FASTPATH | ((secFlag & 0x3) << 6)), UInt16Be((sizeof(fastPathS) + 3) | 0x8000), fastPathS))
    
    async def start_tls(self):
        """
        Start TLS protocol
        """
        ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.VerifyMode.CERT_NONE

        reader, writer = await asyncio.open_connection(sock=self.writer.transport._sock, ssl=ssl_ctx, server_hostname="")
        return Tpkt(reader, writer)
       
    async def start_nla(self, authentication_protocol: sspi.IAuthenticationProtocol):
        """
        use to start NLA (NTLM over SSL) protocol
        must be called after startTLS function

        :ivar authentication_protocol: Authentication protocol use by CSSP to authenticate user
            and transfert credentials
        """
        tpkt = await self.start_tls()
        await cssp.connect(tpkt.reader, tpkt.writer, authentication_protocol)
        return tpkt


class TPKT(RawLayer, IFastPathSender):
    """
    @summary:  TPKT layer in RDP protocol stack
                represent the Raw Layer in stack (first layer)
                This layer only handle size of packet and determine if is a fast path packet
    """
    def __init__(self, presentation):
        """
        @param presentation: {Layer} presentation layer, in RDP case is x224 layer
        """
        RawLayer.__init__(self, presentation)
        #length may be coded on more than 1 bytes
        self._lastShortLength = UInt8()
        #fast path listener
        self._fastPathListener = None
        #last secure flag
        self._secFlag = 0
            
    def setFastPathListener(self, fastPathListener):
        """
        @param fastPathListener : {IFastPathListener}
        @note: implement IFastPathSender
        """
        self._fastPathListener = fastPathListener
        
    def connect(self):
        """
        @summary:  Call when transport layer connection
                    is made (inherit from RawLayer)
        """
        #header is on two bytes
        self.expect(2, self.readHeader)
        #no connection automata on this layer
        if not self._presentation is None:
            self._presentation.connect()
        
    def readHeader(self, data):
        """
        @summary: Read header of TPKT packet
        @param data: {Stream} received from twisted layer
        """
        #first read packet version
        version = UInt8()
        data.readType(version)
        #classic packet
        if version.value == Action.FASTPATH_ACTION_X224:
            #padding
            data.readType(UInt8())
            #read end header
            self.expect(2, self.readExtendedHeader)
        else:
            #is fast path packet
            self._secFlag = ((version.value >> 6) & 0x3)
            data.readType(self._lastShortLength)
            if self._lastShortLength.value & 0x80:
                #size is 1 byte more
                self.expect(1, self.readExtendedFastPathHeader)
                return
            self.expect(self._lastShortLength.value - 2, self.readFastPath)
                
        
    def readExtendedHeader(self, data):
        """
        @summary: Header may be on 4 bytes
        @param data: {Stream} from twisted layer
        """
        #next state is read data
        size = UInt16Be()
        data.readType(size)
        self.expect(size.value - 4, self.readData)
    
    def readExtendedFastPathHeader(self, data):
        """
        @summary: Fast path header may be on 1 byte more
        @param data: {Stream} from twisted layer
        """
        leftPart = UInt8()
        data.readType(leftPart)
        self._lastShortLength.value &= ~0x80
        packetSize = (self._lastShortLength.value << 8) + leftPart.value
        #next state is fast patn data
        self.expect(packetSize - 3, self.readFastPath)
    
    def readFastPath(self, data):
        """
        @summary: Fast path data
        @param data: {Stream} from twisted layer
        """
        self._fastPathListener.recvFastPath(self._secFlag, data)
        self.expect(2, self.readHeader)
    
    def readData(self, data):
        """
        @summary: Read classic TPKT packet, last state in tpkt automata
        @param data: {Stream} with correct size
        """
        #next state is pass to 
        self._presentation.recv(data)
        self.expect(2, self.readHeader)
        
    def send(self, message):
        """
        @summary: Send encompassed data
        @param message: {network.Type} message to send
        """
        RawLayer.send(self, (UInt8(Action.FASTPATH_ACTION_X224), UInt8(0), UInt16Be(sizeof(message) + 4), message))
        
    def sendFastPath(self, secFlag, fastPathS):
        """
        @param fastPathS: {Type | Tuple} type transform to stream and send as fastpath
        @param secFlag: {integer} Security flag for fastpath packet
        """
        RawLayer.send(self, (UInt8(Action.FASTPATH_ACTION_FASTPATH | ((secFlag & 0x3) << 6)), UInt16Be((sizeof(fastPathS) + 3) | 0x8000), fastPathS))
    
    def startTLS(self, sslContext):
        """
        @summary: start TLS protocol
        @param sslContext: {ssl.ClientContextFactory | ssl.DefaultOpenSSLContextFactory} context use for TLS protocol
        """
        self.transport.startTLS(sslContext)
       
    def startNLA(self, sslContext, callback):
        """
        @summary: use to start NLA (NTLM over SSL) protocol
                    must be called after startTLS function
        """
        self.transport.startNLA(sslContext, callback)