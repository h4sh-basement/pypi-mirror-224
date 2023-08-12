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
Implement Multi-Channel Service

Each channel have a particular role.
The main channel is the graphical channel.
It exist channel for file system order, audio channel, clipboard etc...
"""
from typing import Tuple

from rdpy3.core import x224
from rdpy3.model.layer import LayerAutomata, IStreamSender, Layer
from rdpy3.model.message import sizeof, Stream, UInt8, UInt16Le, Buffer
from rdpy3.model.error import InvalidExpectedDataException, InvalidValue, InvalidSize, CallPureVirtualFuntion
from rdpy3.core.t125.ber import writeLength
import rdpy3.model.log as log

from rdpy3.core.t125 import ber, gcc, per
import rdpy3.security.rsa_wrapper as rsa


class Message:
    """
    """
    MCS_TYPE_CONNECT_INITIAL = 0x65
    MCS_TYPE_CONNECT_RESPONSE = 0x66


class DomainMCSPDU:
    """
    """
    ERECT_DOMAIN_REQUEST = 1
    DISCONNECT_PROVIDER_ULTIMATUM = 8
    ATTACH_USER_REQUEST = 10
    ATTACH_USER_CONFIRM = 11
    CHANNEL_JOIN_REQUEST = 14
    CHANNEL_JOIN_CONFIRM = 15
    SEND_DATA_REQUEST = 25
    SEND_DATA_INDICATION = 26


class Channel:
    """
    """
    MCS_GLOBAL_CHANNEL = 1003
    MCS_USERCHANNEL_BASE = 1001


class IGCCConfig(object):
    """
    @summary: Channel information
    """

    def getUserId(self):
        """
        @return: {integer} mcs user id
        @see: mcs.IGCCConfig
        """
        raise CallPureVirtualFuntion("%s:%s defined by interface %s" % (self.__class__, "getUserId", "IGCCConfig"))

    def getChannelId(self):
        """
        @return: {integer} return channel id of proxy
        @see: mcs.IGCCConfig
        """
        raise CallPureVirtualFuntion("%s:%s defined by interface %s" % (self.__class__, "getChannelId", "IGCCConfig"))

    def getGCCClientSettings(self):
        """
        @return: {gcc.Settings} mcs layer gcc client settings
        @see: mcs.IGCCConfig
        """
        raise CallPureVirtualFuntion(
            "%s:%s defined by interface %s" % (self.__class__, "getGCCClientSettings", "IGCCConfig"))

    def getGCCServerSettings(self):
        """
        @return: {gcc.Settings} mcs layer gcc server settings
        @see: mcs.IGCCConfig
        """
        raise CallPureVirtualFuntion(
            "%s:%s defined by interface %s" % (self.__class__, "getGCCServerSettings", "IGCCConfig"))


def write_domain_params(max_channels: int, max_users: int, max_tokens: int, max_pdu_size: int) -> tuple:
    """
    """
    domain_param = (ber.writeInteger(max_channels), ber.writeInteger(max_users), ber.writeInteger(max_tokens),
                    ber.writeInteger(1), ber.writeInteger(0), ber.writeInteger(1),
                    ber.writeInteger(max_pdu_size), ber.writeInteger(2))
    return ber.writeUniversalTag(ber.Tag.BER_TAG_SEQUENCE, True), writeLength(sizeof(domain_param)), domain_param


def read_domain_params(stream: Stream) -> Tuple[int, int, int, int]:
    """
    """
    if not ber.readUniversalTag(stream, ber.Tag.BER_TAG_SEQUENCE, True):
        raise InvalidValue("bad BER tags")
    ber.readLength(stream)  # length
    max_channels = ber.readInteger(stream)
    max_users = ber.readInteger(stream)
    max_tokens = ber.readInteger(stream)
    ber.readInteger(stream)
    ber.readInteger(stream)
    ber.readInteger(stream)
    max_pdu_size = ber.readInteger(stream)
    ber.readInteger(stream)
    return max_channels, max_users, max_tokens, max_pdu_size


def mcs_pdu_header(mcs_pdu: UInt8, options=0) -> UInt8:
    return (mcs_pdu << 2) | options


def check_mcs_pdu_header(opcode: UInt8, mcs_pdu):
    return (opcode >> 2) == mcs_pdu


def erect_domain_request() -> Tuple:
    return mcs_pdu_header(UInt8(DomainMCSPDU.ERECT_DOMAIN_REQUEST)), per.writeInteger(0), per.writeInteger(0)


def read_attach_confirm(data: Stream) -> int:
    """
    """
    opcode = data.read_type(UInt8())

    if not check_mcs_pdu_header(opcode, DomainMCSPDU.ATTACH_USER_CONFIRM):
        raise InvalidExpectedDataException("Invalid MCS PDU : ATTACH_USER_CONFIRM expected")

    if per.readEnumerates(data) != 0:
        raise InvalidExpectedDataException("Server reject user")

    return per.readInteger16(data, Channel.MCS_USERCHANNEL_BASE)


def attach_user_request() -> UInt8:
    return mcs_pdu_header(UInt8(DomainMCSPDU.ATTACH_USER_REQUEST))


def channel_join_request(user_id: int, channel_id: int):
    return (mcs_pdu_header(UInt8(DomainMCSPDU.CHANNEL_JOIN_REQUEST)),
            per.writeInteger16(user_id, Channel.MCS_USERCHANNEL_BASE),
            per.writeInteger16(channel_id))


def channel_join_confirm(user_id: int, channel_id: int, data: Stream) -> bool:
    """
    """
    opcode = data.read_type(UInt8())

    if not check_mcs_pdu_header(opcode.value, DomainMCSPDU.CHANNEL_JOIN_CONFIRM):
        raise InvalidExpectedDataException("Invalid MCS PDU : CHANNEL_JOIN_CONFIRM expected")

    confirm = per.readEnumerates(data)

    if user_id != per.readInteger16(data, Channel.MCS_USERCHANNEL_BASE):
        raise InvalidExpectedDataException("Invalid MCS User Id")

    if channel_id != per.readInteger16(data):
        raise InvalidExpectedDataException("Invalid MCS channel id")

    return confirm == 0


class Client:
    def __init__(self, x224_layer: x224.X224):
        self.x224 = x224_layer
        self.channel_ids = {}

    async def write_connect_initial(self):
        """
        """
        settings = gcc.client_settings()
        settings.get_block(gcc.MessageType.CS_CORE).serverSelectedProtocol.value = self.x224.get_selected_protocol()

        cc_req = gcc.writeConferenceCreateRequest(settings)
        cc_req_stream = Stream()
        cc_req_stream.write_type(cc_req)

        tmp = (ber.writeOctetstring(b"\x01"), ber.writeOctetstring(b"\x01"), ber.writeBoolean(True),
               write_domain_params(34, 2, 0, 0xffff),
               write_domain_params(1, 1, 1, 0x420),
               write_domain_params(0xffff, 0xfc17, 0xffff, 0xffff),
               ber.writeOctetstring(cc_req_stream.getvalue()))
        await self.x224.write((ber.writeApplicationTag(Message.MCS_TYPE_CONNECT_INITIAL, sizeof(tmp)), tmp))

    async def read_connect_response(self):
        payload = await self.x224.read()
        ber.readApplicationTag(payload, UInt8(Message.MCS_TYPE_CONNECT_RESPONSE))
        ber.readEnumerated(payload)
        ber.readInteger(payload)
        read_domain_params(payload)
        if not ber.readUniversalTag(payload, ber.Tag.BER_TAG_OCTET_STRING, False):
            raise InvalidExpectedDataException("invalid expected BER tag")
        gccRequestLength = ber.readLength(payload)
        if payload.data_len() != gccRequestLength:
            raise InvalidSize("bad size of GCC request")
        gcc.readConferenceCreateResponse(payload)


    async def connect(self):
        await self.write_connect_initial()
        await self.read_connect_response()
        await self.x224.write(erect_domain_request())
        await self.x224.write(attach_user_request())
        user_id = read_attach_confirm(await self.x224.read())
        self.channel_ids["global"] = 1003
        self.channel_ids["user"] = user_id

        # connect all channels
        for channel_id in self.channel_ids.values():
            await self.x224.write(channel_join_request(user_id, channel_id))
            if not channel_join_confirm(user_id, channel_id, await self.x224.read()):
                print("Server refused channel %s"%channel_id)


class MCSLayer(LayerAutomata):
    """
    @summary: Multiple Channel Service layer
    the main layer of RDP protocol
    is why he can do everything and more!
    """

    class MCSProxySender(Layer, IStreamSender, IGCCConfig):
        """
        @summary: Proxy use to set as transport layer for upper channel
        use to abstract channel id for presentation layer
        """

        def __init__(self, presentation, mcs, channelId):
            """
            @param presentation: {Layer} presentation layer 
            @param mcs: {MCSLayer} MCS layer use as proxy
            @param channelId: {integer} channel id for presentation layer 
            """
            Layer.__init__(self, presentation)
            self._mcs = mcs
            self._channelId = channelId

        def send(self, data):
            """
            @summary: A send proxy function, use channel id and specific 
            send function of MCS layer
            @param data: {type.Type | Tuple}
            """
            self._mcs.send(self._channelId, data)

        def close(self):
            """
            @summary: Close wrapped layer
            """
            self._mcs.close()

        def getUserId(self):
            """
            @return: {integer} mcs user id
            @see: mcs.IGCCConfig
            """
            return self._mcs._userId

        def getChannelId(self):
            """
            @return: {integer} return channel id of proxy
            @see: mcs.IGCCConfig
            """
            return self._channelId

        def getGCCClientSettings(self):
            """
            @return: {gcc.Settings} mcs layer gcc client settings
            @see: mcs.IGCCConfig
            """
            return self._mcs._clientSettings

        def getGCCServerSettings(self):
            """
            @return: {gcc.Settings} mcs layer gcc server settings
            @see: mcs.IGCCConfig
            """
            return self._mcs._serverSettings

    def __init__(self, presentation, receiveOpcode, sendOpcode, virtualChannels=[]):
        """
        @param presentation: {Layer} presentation layer
        @param virtualChannels: {Array(Layer]} list additional channels like rdpsnd... [tuple(mcs.ChannelDef, layer)]
        @param receiveOpcode: {integer} opcode check when receive data
        @param sendOpcode: {integer} opcode use when send data
        """
        LayerAutomata.__init__(self, presentation)
        self._clientSettings = gcc.clientSettings()
        self._serverSettings = gcc.serverSettings()
        # default user Id
        self._userId = 1 + Channel.MCS_USERCHANNEL_BASE
        # list of channel use in this layer and connection state
        self._channels = {Channel.MCS_GLOBAL_CHANNEL: presentation}
        # virtual channels
        self._virtualChannels = virtualChannels
        # send opcode
        self._sendOpcode = sendOpcode
        # receive opcode
        self._receiveOpcode = receiveOpcode

    def close(self):
        """
        @summary: Send disconnect provider ultimatum
        """
        self._transport.send((UInt8(self.writeMCSPDUHeader(DomainMCSPDU.DISCONNECT_PROVIDER_ULTIMATUM, 1)),
                              per.writeEnumerates(0x80), Buffer(b"\x00" * 6)))
        self._transport.close()

    def allChannelConnected(self):
        """
        @summary: All channels are connected to MCS layer
        Send connect to upper channel
        And prepare MCS layer to receive data
        """
        # connection is done
        self.setNextState(self.recvData)
        # try connection on all requested channel
        for (channelId, layer) in self._channels.items():
            # use proxy for each channel
            MCSLayer.MCSProxySender(layer, self, channelId).connect()

    def send(self, channelId, data):
        """
        @summary: Specific send function for channelId
        @param channelId: {integer} Channel use to send
        @param data: {type.type | tuple} message to send
        """
        self._transport.send((self.writeMCSPDUHeader(UInt8(self._sendOpcode)),
                              per.writeInteger16(self._userId, Channel.MCS_USERCHANNEL_BASE),
                              per.writeInteger16(channelId),
                              UInt8(0x70),
                              per.writeLength(sizeof(data)), data))

    def recvData(self, data):
        """
        @summary: Main receive method
        @param data: {Stream} 
        """
        opcode = UInt8()
        data.read_type(opcode)

        if self.readMCSPDUHeader(opcode.value, DomainMCSPDU.DISCONNECT_PROVIDER_ULTIMATUM):
            log.info("MCS DISCONNECT_PROVIDER_ULTIMATUM")
            self._transport.close()
            return

        # client case
        elif not self.readMCSPDUHeader(opcode.value, self._receiveOpcode):
            raise InvalidExpectedDataException("Invalid expected MCS opcode receive data")

        # server user id
        per.readInteger16(data, Channel.MCS_USERCHANNEL_BASE)

        channelId = per.readInteger16(data)

        per.readEnumerates(data)
        per.readLength(data)

        # channel id doesn't match a requested layer
        if not self._channels.has_key(channelId):
            log.error("receive data for an unconnected layer")
            return

        self._channels[channelId].recv(data)

    def writeDomainParams(self, maxChannels, maxUsers, maxTokens, maxPduSize):
        """
        @summary: Write a special domain parameter structure
        use in connection sequence
        @param maxChannels: {integer} number of MCS channel use
        @param maxUsers: {integer} number of MCS user used (1)
        @param maxTokens: {integer} unknown
        @param maxPduSize: {integer} unknown
        @return: {Tuple(type)} domain parameter structure
        """
        domainParam = (ber.writeInteger(maxChannels), ber.writeInteger(maxUsers), ber.writeInteger(maxTokens),
                       ber.writeInteger(1), ber.writeInteger(0), ber.writeInteger(1),
                       ber.writeInteger(maxPduSize), ber.writeInteger(2))
        return (ber.writeUniversalTag(ber.Tag.BER_TAG_SEQUENCE, True), writeLength(sizeof(domainParam)), domainParam)

    def writeMCSPDUHeader(self, mcsPdu, options=0):
        """
        @summary: Write MCS PDU header
        @param mcsPdu: {integer} PDU code
        @param options: {integer} option contains in header
        @return: {integer}
        """
        return (mcsPdu << 2) | options

    def readMCSPDUHeader(self, opcode, mcsPdu):
        """
        @summary: Read mcsPdu header and return options parameter
        @param opcode: {integer} opcode
        @param mcsPdu: {integer} mcsPdu will be checked
        @return: {boolean} true if opcode is correct
        """
        return (opcode >> 2) == mcsPdu

    def readDomainParams(self, s):
        """
        @summary: Read domain parameters structure
        @param s: {Stream}
        @return: {Tuple} (max_channels, max_users, max_tokens, max_pdu_size)
        """
        if not ber.readUniversalTag(s, ber.Tag.BER_TAG_SEQUENCE, True):
            raise InvalidValue("bad BER tags")
        ber.readLength(s)  # length
        max_channels = ber.readInteger(s)
        max_users = ber.readInteger(s)
        max_tokens = ber.readInteger(s)
        ber.readInteger(s)
        ber.readInteger(s)
        ber.readInteger(s)
        max_pdu_size = ber.readInteger(s)
        ber.readInteger(s)
        return (max_channels, max_users, max_tokens, max_pdu_size)


class ClientOld(MCSLayer):
    """
    @summary: Client automata of multiple channel service layer
    """

    def __init__(self, presentation, virtualChannels=[]):
        """
        @param presentation: {Layer} presentation layer
        @param virtualChannels: {Array(Layer)} list additional channels like rdpsnd... [tuple(mcs.ChannelDef, layer)]
        """
        MCSLayer.__init__(self, presentation, DomainMCSPDU.SEND_DATA_INDICATION, DomainMCSPDU.SEND_DATA_REQUEST,
                          virtualChannels)
        # use to know state of static channel
        self._isGlobalChannelRequested = False
        self._isUserChannelRequested = False
        # nb channel requested
        self._nbChannelRequested = 0

    def connect(self):
        """
        @summary: Connect message in client automata case
        Send ConnectInitial
        Wait ConnectResponse
        """
        self._clientSettings.CS_CORE.serverSelectedProtocol.value = self._transport._selectedProtocol
        # ask for virtual channel
        self._clientSettings.CS_NET.channelDefArray._array = [x for (x, _) in self._virtualChannels]
        # send connect initial
        self.sendConnectInitial()
        # next wait response
        self.setNextState(self.recvConnectResponse)

    def connectNextChannel(self):
        """
        @summary: Send sendChannelJoinRequest message on next disconnect channel
        Send channel request or connect upper layer if all channels are connected
        Wait channel confirm
        """
        self.setNextState(self.recvChannelJoinConfirm)
        # global channel
        if not self._isGlobalChannelRequested:
            self.sendChannelJoinRequest(Channel.MCS_GLOBAL_CHANNEL)
            self._isGlobalChannelRequested = True
            return

        # user channel
        if not self._isUserChannelRequested:
            self.sendChannelJoinRequest(self._userId)
            self._isUserChannelRequested = True
            return

        # static virtual channel
        if self._nbChannelRequested < self._serverSettings.get_block(gcc.MessageType.SC_NET).channelCount.value:
            channelId = self._serverSettings.get_block(gcc.MessageType.SC_NET).channelIdArray[self._nbChannelRequested]
            self._nbChannelRequested += 1
            self.sendChannelJoinRequest(channelId)
            return

        self.allChannelConnected()

    def recvConnectResponse(self, data):
        """
        @summary: Receive MCS connect response from server
        Send Erect domain Request
        Send Attach User Request
        Wait Attach User Confirm
        @param data: {Stream}
        """
        ber.readApplicationTag(data, UInt8(Message.MCS_TYPE_CONNECT_RESPONSE))
        ber.readEnumerated(data)
        ber.readInteger(data)
        self.readDomainParams(data)
        if not ber.readUniversalTag(data, ber.Tag.BER_TAG_OCTET_STRING, False):
            raise InvalidExpectedDataException("invalid expected BER tag")
        gccRequestLength = ber.readLength(data)
        if data.data_len() != gccRequestLength:
            raise InvalidSize("bad size of GCC request")
        self._serverSettings = gcc.readConferenceCreateResponse(data)

        # send domain request
        self.sendErectDomainRequest()
        # send attach user request
        self.sendAttachUserRequest()
        # now wait user confirm from server
        self.setNextState(self.recvAttachUserConfirm)

    def recvAttachUserConfirm(self, data):
        """
        @summary: Receive an attach user confirm
        Send Connect Channel
        @param data: {Stream}
        """
        opcode = UInt8()
        data.read_type(opcode)

        if not self.readMCSPDUHeader(opcode.value, DomainMCSPDU.ATTACH_USER_CONFIRM):
            raise InvalidExpectedDataException("Invalid MCS PDU : ATTACH_USER_CONFIRM expected")

        if per.readEnumerates(data) != 0:
            raise InvalidExpectedDataException("Server reject user")

        self._userId = per.readInteger16(data, Channel.MCS_USERCHANNEL_BASE)

        self.connectNextChannel()

    def recvChannelJoinConfirm(self, data):
        """
        @summary: Receive a channel join confirm from server
        client automata function
        @param data: {Stream}
        """
        opcode = UInt8()
        data.read_type(opcode)

        if not self.readMCSPDUHeader(opcode.value, DomainMCSPDU.CHANNEL_JOIN_CONFIRM):
            raise InvalidExpectedDataException("Invalid MCS PDU : CHANNEL_JOIN_CONFIRM expected")

        confirm = per.readEnumerates(data)

        userId = per.readInteger16(data, Channel.MCS_USERCHANNEL_BASE)
        if self._userId != userId:
            raise InvalidExpectedDataException("Invalid MCS User Id")

        channelId = per.readInteger16(data)
        # must confirm global channel and user channel
        if (confirm != 0) and (channelId == Channel.MCS_GLOBAL_CHANNEL or channelId == self._userId):
            raise InvalidExpectedDataException("Server must confirm static channel")

        if confirm == 0:
            serverNet = self._serverSettings.get_block(gcc.MessageType.SC_NET)
            for i in range(0, serverNet.channelCount.value):
                if channelId == serverNet.channelIdArray[i].value:
                    self._channels[channelId] = self._virtualChannels[i][1]

        self.connectNextChannel()

    def sendConnectInitial(self):
        """
        @summary: Send connect initial packet
        client automata function
        """
        ccReq = gcc.writeConferenceCreateRequest(self._clientSettings)
        ccReqStream = Stream()
        ccReqStream.write_type(ccReq)

        tmp = (ber.writeOctetstring("\x01"), ber.writeOctetstring("\x01"), ber.writeBoolean(True),
               self.writeDomainParams(34, 2, 0, 0xffff),
               self.writeDomainParams(1, 1, 1, 0x420),
               self.writeDomainParams(0xffff, 0xfc17, 0xffff, 0xffff),
               ber.writeOctetstring(ccReqStream.getvalue()))
        self._transport.send((ber.writeApplicationTag(Message.MCS_TYPE_CONNECT_INITIAL, sizeof(tmp)), tmp))

    def sendErectDomainRequest(self):
        """
        @summary: Send a formated erect domain request for RDP connection
        """
        self._transport.send((self.writeMCSPDUHeader(UInt8(DomainMCSPDU.ERECT_DOMAIN_REQUEST)),
                              per.writeInteger(0),
                              per.writeInteger(0)))

    def sendAttachUserRequest(self):
        """
        @summary: Send a formated attach user request for RDP connection
        """
        self._transport.send(self.writeMCSPDUHeader(UInt8(DomainMCSPDU.ATTACH_USER_REQUEST)))

    def sendChannelJoinRequest(self, channelId):
        """
        @summary: Send a formated Channel join request from client to server
        client automata function
        @param channelId: {integer} id of channel requested
        """
        self._transport.send((self.writeMCSPDUHeader(UInt8(DomainMCSPDU.CHANNEL_JOIN_REQUEST)),
                              per.writeInteger16(self._userId, Channel.MCS_USERCHANNEL_BASE),
                              per.writeInteger16(channelId)))


class Server(MCSLayer):
    """
    @summary: Server automata of multiple channel service layer
    """

    def __init__(self, presentation, virtualChannels=[]):
        """
        @param presentation: {Layer} presentation layer
        @param virtualChannels: {List(Layer)} list additional channels like rdpsnd... [tuple(mcs.ChannelDef, layer)]
        """
        MCSLayer.__init__(self, presentation, DomainMCSPDU.SEND_DATA_REQUEST, DomainMCSPDU.SEND_DATA_INDICATION,
                          virtualChannels)
        # nb channel requested
        self._nbChannelConfirmed = 0

    def connect(self):
        """
        @summary: Connect message for server automata
        Wait Connect Initial
        """
        # basic rdp security layer
        if self._transport._selectedProtocol == 0:
            self._serverSettings.SC_SECURITY.encryptionMethod.value = gcc.EncryptionMethod.ENCRYPTION_FLAG_128BIT
            self._serverSettings.SC_SECURITY.encryptionLevel.value = gcc.EncryptionLevel.ENCRYPTION_LEVEL_HIGH
            self._serverSettings.SC_SECURITY.serverRandom.value = rsa.random(256)
            self._serverSettings.SC_SECURITY.serverCertificate = self._presentation.getCertificate()

        self._serverSettings.SC_CORE.clientRequestedProtocol.value = self._transport._requestedProtocol
        self.setNextState(self.recvConnectInitial)

    def recvConnectInitial(self, data):
        """
        @summary: Receive MCS connect initial from client
        Send Connect Response
        Wait Erect Domain Request
        @param data: {Stream}
        """
        ber.readApplicationTag(data, UInt8(Message.MCS_TYPE_CONNECT_INITIAL))
        ber.readOctetString(data)
        ber.readOctetString(data)

        if not ber.readBoolean(data):
            raise InvalidExpectedDataException("invalid expected BER boolean tag")

        self.readDomainParams(data)
        self.readDomainParams(data)
        self.readDomainParams(data)
        self._clientSettings = gcc.readConferenceCreateRequest(Stream(ber.readOctetString(data)))

        if not self._clientSettings.CS_NET is None:
            i = 1
            for channelDef in self._clientSettings.CS_NET.channelDefArray._array:
                self._serverSettings.SC_NET.channelIdArray._array.append(UInt16Le(i + Channel.MCS_GLOBAL_CHANNEL))
                # if channel can be handle by serve add it
                for serverChannelDef, layer in self._virtualChannels:
                    if channelDef.name == serverChannelDef.name:
                        self._channels[i + Channel.MCS_GLOBAL_CHANNEL] = layer
                i += 1

        self.sendConnectResponse()
        self.setNextState(self.recvErectDomainRequest)

    def recvErectDomainRequest(self, data):
        """
        @summary: Receive erect domain request
        Wait Attach User Request
        @param data: {Stream}
        """
        opcode = UInt8()
        data.read_type(opcode)

        if not self.readMCSPDUHeader(opcode.value, DomainMCSPDU.ERECT_DOMAIN_REQUEST):
            raise InvalidExpectedDataException("Invalid MCS PDU : ERECT_DOMAIN_REQUEST expected")

        per.readInteger(data)
        per.readInteger(data)

        self.setNextState(self.recvAttachUserRequest)

    def recvAttachUserRequest(self, data):
        """
        @summary: Receive Attach user request
        Send Attach User Confirm
        Wait Channel Join Request
        @param data: {Stream}
        """
        opcode = UInt8()
        data.read_type(opcode)

        if not self.readMCSPDUHeader(opcode.value, DomainMCSPDU.ATTACH_USER_REQUEST):
            raise InvalidExpectedDataException("Invalid MCS PDU : ATTACH_USER_REQUEST expected")

        self.sendAttachUserConfirm()
        self.setNextState(self.recvChannelJoinRequest)

    def recvChannelJoinRequest(self, data):
        """
        @summary: Receive for each client channel a request
        Send Channel Join Confirm or Connect upper layer when all channel are joined
        @param data: {Stream}
        
        """
        opcode = UInt8()
        data.read_type(opcode)

        if not self.readMCSPDUHeader(opcode.value, DomainMCSPDU.CHANNEL_JOIN_REQUEST):
            raise InvalidExpectedDataException("Invalid MCS PDU : CHANNEL_JOIN_REQUEST expected")

        userId = per.readInteger16(data, Channel.MCS_USERCHANNEL_BASE)
        if self._userId != userId:
            raise InvalidExpectedDataException("Invalid MCS User Id")

        channelId = per.readInteger16(data)
        # actually algo support virtual channel but RDPY have no virtual channel
        confirm = 0 if channelId in self._channels.keys() or channelId == self._userId else 1
        self.sendChannelJoinConfirm(channelId, confirm)
        self._nbChannelConfirmed += 1
        if self._nbChannelConfirmed == self._serverSettings.get_block(gcc.MessageType.SC_NET).channelCount.value + 2:
            self.allChannelConnected()

    def sendConnectResponse(self):
        """
        @summary: Send connect response
        """
        ccReq = gcc.writeConferenceCreateResponse(self._serverSettings)
        ccReqStream = Stream()
        ccReqStream.write_type(ccReq)

        tmp = (ber.writeEnumerated(0), ber.writeInteger(0), self.writeDomainParams(22, 3, 0, 0xfff8),
               ber.writeOctetstring(ccReqStream.getvalue()))
        self._transport.send((ber.writeApplicationTag(Message.MCS_TYPE_CONNECT_RESPONSE, sizeof(tmp)), tmp))

    def sendAttachUserConfirm(self):
        """
        @summary: Send attach user confirm
        """
        self._transport.send((self.writeMCSPDUHeader(UInt8(DomainMCSPDU.ATTACH_USER_CONFIRM), 2),
                              per.writeEnumerates(0),
                              per.writeInteger16(self._userId, Channel.MCS_USERCHANNEL_BASE)))

    def sendChannelJoinConfirm(self, channelId, confirm):
        """
        @summary: Send a confirm channel (or not) to client
        @param channelId: {integer} id of channel
        @param confirm: {boolean} connection state 
        """
        self._transport.send((self.writeMCSPDUHeader(UInt8(DomainMCSPDU.CHANNEL_JOIN_CONFIRM), 2),
                              per.writeEnumerates(int(confirm)),
                              per.writeInteger16(self._userId, Channel.MCS_USERCHANNEL_BASE),
                              per.writeInteger16(channelId),
                              per.writeInteger16(channelId)))
