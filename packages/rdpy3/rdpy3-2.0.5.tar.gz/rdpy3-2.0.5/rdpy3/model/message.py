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
Raw type use in RDPY

It's a basic implementation looks like google protobuf but dynamically
We are in python!
"""

import struct
from copy import deepcopy
from io import BytesIO
from rdpy3.model.error import InvalidExpectedDataException, InvalidSize, CallPureVirtualFuntion, InvalidValue
import rdpy3.model.log as log


def sizeof(element):
    """
    @summary:  Size in Byte of element.
                Ignore element which conditional is False
    @param element: Type or Tuple(Type | Tuple,)
    @return: size of element in byte or zero for unknown element
    """
    if isinstance(element, tuple) or isinstance(element, list):
        size = 0
        for i in element:
            size += sizeof(i)
        return size
    elif isinstance(element, Message) and element._conditional():
        return element.__sizeof__()
    return 0


class Message:
    """
    @summary:  Root type object inheritance
                Record conditional optional of constant mechanism
    """
    def __init__(self, conditional=lambda: True, optional=False, constant=False):
        """
        """
        self._conditional = conditional
        self._optional = optional
        self._constant = constant
        # use to record read state
        # if type is optional and not present during read
        # this boolean stay false
        self._is_readed = False
        # use to know if type was written
        self._is_writed = False

    def write(self, s):
        """
        @summary:  Check conditional callback 
                    before call __write__ function 
        @param s: Stream that will be written
        """
        self._is_writed = self._conditional()
        if not self._is_writed:
            return
        self.__write__(s)

    def read(self, s):
        """
        @summary:  Check conditional callback 
                    Call __read__ function
                    And check constness state after
        @param s: Stream
        @raise InvalidExpectedDataException: if constness is not respected
        """
        self._is_readed = self._conditional()
        if not self._is_readed:
            return

        # not constant mode direct reading
        if not self._constant:
            self.__read__(s)
            return

        # constant mode
        old = deepcopy(self)
        self.__read__(s)
        # check constant value
        if isinstance(old.value, str):
            old.value = old.value.encode()
        if old != self:
            # rollback read value
            s.seek(-sizeof(self), 1)
            raise InvalidExpectedDataException("%s const value expected %s != %s"%(self.__class__, old.value, self.value))

    def __read__(self, s):
        """
        @summary: Interface definition of private read function
        @param s: Stream 
        """
        raise CallPureVirtualFuntion("%s:%s defined by interface %s"%(self.__class__, "__read__", "Type"))

    def __write__(self, s):
        """
        @summary: Interface definition of private write function
        @param s: Stream 
        """
        raise CallPureVirtualFuntion("%s:%s defined by interface %s"%(self.__class__, "__write__", "Type"))

    def __sizeof__(self):
        """
        @summary: Return size of type use for sizeof function
        @return: size in byte of type
        """
        raise CallPureVirtualFuntion("%s:%s defined by interface %s"%(self.__class__, "__sizeof__", "Type"))


class DynMessage(Message):
    """
    Expression evaluate when is get or set
    Ex: Type contain length of array and array
    To know the size of array you need to read
    length field before. At ctor time no length was read.
    You need a callable object that will be evaluate when it will be used
    """
    def __init__(self, **kwargs):
        """
        @param value: value will be wrapped (raw python type  | lambda | function)
        """
        super().__init__(**kwargs)
        self._value = None

    def get_value(self):
        """
        @summary:  Call when value is get -> Evaluate inner expression
                    Can be overwritten to add specific check before
                    self.value is call
        @return: value expression evaluated
        """
        return self._value()

    def set_value(self, value):
        """
        @summary:  Call when value is set
                    Can be overwritten to add specific check before
                    self.value = value is call
        @param value: new value wrapped if constant -> lambda function
        """
        value_callable = lambda:value
        if callable(value):
            value_callable = value

        self._value = value_callable
    
    def __call__(self):
        return self.value

    value = property(get_value, set_value)

# CallableValue = DynMessage

class CallableValue(object):
    """
    @summary:  Expression evaluate when is get or set
                Ex: Type contain length of array and array
                To know the size of array you need to read 
                length field before. At ctor time no length was read.
                You need a callable object that will be evaluate when it will be used
    """
    def __init__(self, value):
        """
        @param value: value will be wrapped (raw python type  | lambda | function)
        """
        self._value = None
        self.value = value
    
    def __getValue__(self):
        """
        @summary:  Call when value is get -> Evaluate inner expression
                    Can be overwritten to add specific check before
                    self.value is call
        @return: value expression evaluated
        """
        return self._value()
    
    def __setValue__(self, value):
        """
        @summary:  Call when value is set
                    Can be overwritten to add specific check before
                    self.value = value is call
        @param value: new value wrapped if constant -> lambda function
        """
        value_callable = lambda:value
        if callable(value):
            value_callable = value
            
        self._value = value_callable
    
    @property
    def value(self):
        """
        @summary: Evaluate callable expression
        @return: result of callable value
        """
        return self.__getValue__()
    
    @value.setter
    def value(self, value):
        """
        @summary: Setter of value
        @param value: new value encompass in value type object
        """
        self.__setValue__(value)
    
    def __call__(self):
        return self.value


class SimpleType(DynMessage):
    """
    @summary:  Non composite type
                leaf in type tree
                And is a callable value
    """
    def __init__(self, structFormat, typeSize, signed, value, conditional = lambda:True, optional = False, constant = False):
        """
        @param structFormat: letter that represent type in struct package
        @param typeSize: size in byte of type
        @param signed: true if type represent a signed type
        @param value: value recorded in this object (raw Python type | lambda | function)
        @param conditional :    Callable object
                                 Read and Write operation depend on return of this function
        @param optional:   If there is no enough byte in current stream
                            And optional is True, read type is ignored
        @param constant:   Check if object value doesn't change after read operation
        """
        super().__init__(conditional=conditional, optional=optional, constant=constant)
        self._signed = signed
        self._typeSize = typeSize
        self._structFormat = structFormat
        self.value = value

    def __write__(self, s):
        """
        @summary:  Write value in stream
                    Use struct package to pack value
                    In accordance of structFormat field
        @param s: Stream that will be written
        """
        s.write(struct.pack(self._structFormat, self.value))

    def __read__(self, s):
        """
        @summary:  Read inner value from stream
                    Use struct package to unpack
                    In accordance of structFormat and typeSize fields
        @param s: Stream that will be read
        @raise InvalidSize: if there is not enough data in stream
        """
        if s.data_len() < self._typeSize:
            raise InvalidSize(f"Stream ({s.data_len()}) is too small to read expected SimpleType ({self._typeSize})")
        value = struct.unpack(self._structFormat, s.read(self._typeSize))[0]

        self.value = value

    def __sizeof__(self):
        """
        @summary: Return size of type in bytes
        @return: typeSize pass in constructor
        """
        return self._typeSize

    def __eq__(self, other):
        """
        @summary:  Compare two simple type
                    Call inner value compare operator
        @param other:  SimpleType value or try to build same type as self
                        around value
        @return: python value compare
        """
        if not isinstance(other, SimpleType):
            other = self.__class__(other)
        return self.value.__eq__(other.value)

    def __ne__(self, other):
        """
        @summary:  Compare two simple type
                    Call inner value compare operator
        @param other:  SimpleType value or try to build same type as self
                        around value
        @return: python value compare
        """
        if not isinstance(other, SimpleType):
            other = self.__class__(other)
        return self.value.__ne__(other.value)

    def __invert__(self):
        """
        @summary: Implement not operator
        @return: not inner value
        """
        invert = ~self.value
        if not self._signed:
            invert &= self.mask()
        return self.__class__(invert)

    def __add__(self, other):
        """
        @summary: Implement addition operator
        @param other:  SimpleType value or try to construct same type as self
                        around other value
        @return: add operator of inner values
        @raise InvalidValue: if new value is out of bound
        """
        if not isinstance(other, SimpleType):
            other = self.__class__(other)
        return self.__class__(self.value.__add__(other.value))

    def __sub__(self, other):
        """
        @summary: Implement sub operator
        @param other:  SimpleType value or try to construct same type as self
                        around other value
        @return: sub operator of inner values
        @raise InvalidValue: if new value is out of bound
        """
        if not isinstance(other, SimpleType):
            other = self.__class__(other)
        return self.__class__(self.value.__sub__(other.value))

    def __and__(self, other):
        """
        @summary: Implement bitwise and operator
        @param other:  SimpleType value or try to construct same type as self
                        around other value
        @return: and operator of inner values
        @raise InvalidValue: if new value is out of bound
        """
        if not isinstance(other, SimpleType):
            other = self.__class__(other)
        return self.__class__(self.value.__and__(other.value))

    def __or__(self, other):
        """
        @summary: Implement bitwise or operator
        @param other:  SimpleType value or try to construct same type as self
                        around other value
        @return: or operator of inner values
        @raise InvalidValue: if new value is out of bound
        """
        if not isinstance(other, SimpleType):
            other = self.__class__(other)
        return self.__class__(self.value.__or__(other.value))

    def __xor__(self, other):
        """
        @summary: Implement bitwise xor operator
        @param other:  SimpleType value or try to construct same type as self
                        around other value
        @return: xor operator of inner values
        @raise InvalidValue: if new value is out of bound
        """
        if not isinstance(other, SimpleType):
            other = self.__class__(other)
        return self.__class__(self.value.__xor__(other.value))

    def __lshift__(self, other):
        """
        @summary: Left shift operator
        @param other:  SimpleType value or try to construct same type as self
                        around other value
        @return: lshift operator of inner values
        @raise InvalidValue: if new value is out of bound
        """
        if not isinstance(other, SimpleType):
            other = self.__class__(other)
        return self.__class__(self.value.__lshift__(other.value))

    def __rshift__(self, other):
        """
        @summary: Right shift operator
        @param other:  SimpleType value or try to construct same type as self
                        around other value
        @return: rshift operator of inner values
        @raise InvalidValue: if new value is out of bound
        """
        if not isinstance(other, SimpleType):
            other = self.__class__(other)
        return self.__class__(self.value.__rshift__(other.value))

    def __hash__(self):
        """
        @summary: Hash function to handle simple type in hash collection
        @return: hash of inner value
        """
        return hash(self.value)

    def __nonzero__(self):
        """
        @summary: Boolean conversion
        @return: bool of inner value
        """
        return bool(self.value)


class CompositeType(Message):
    """
    """
    def __init__(self, read_len=None, conditional=lambda: True, optional=False, constant=False, readLen=None):
        """
        """
        super().__init__(conditional=conditional, optional=optional, constant=constant)

        # list of ordorred type
        self._type_name = []
        self._read_len = read_len if read_len else readLen

    def __setattr__(self, name, value):
        """
        """
        if name[0] != '_' and (isinstance(value, Message) or isinstance(value, tuple)) and name not in self._type_name:
            self._type_name.append(name)
        self.__dict__[name] = value

    def __read__(self, s):
        """
        """
        read_len = 0
        for name in self._type_name:
            try:
                s.read_type(self.__dict__[name])
                read_len += sizeof(self.__dict__[name])
                # read is ok but read out of bound
                if self._read_len is not None and read_len > self._read_len():
                    # roll back
                    s.seek(-sizeof(self.__dict__[name]), 1)
                    # and notify if not optional
                    if not self.__dict__[name]._optional:
                        raise InvalidSize("Impossible to read type %s : read length is too small"%(self.__class__))

            except Exception as e:
                log.error("Error during read %s::%s"%(self.__class__, name))
                # roll back already read
                for tmp_name in self._type_name:
                    if tmp_name == name:
                        break
                    s.seek(-sizeof(self.__dict__[tmp_name]), 1)
                raise e

        if self._read_len is not None and read_len < self._read_len():
            log.debug("Still have correct data in packet %s, read %s bytes as padding"%(self.__class__, self._read_len() - read_len))
            s.read(self._read_len() - read_len)

    def __write__(self, s):
        """
        @summary:  Write all sub-type handle by __setattr__ function
                    Call write on each ordered sub type
        @param s: Stream
        """
        for name in self._type_name:
            try:
                s.write_type(self.__dict__[name])
            except Exception as e:
                log.error("Error during write %s::%s"%(self.__class__, name))
                raise e

    def __sizeof__(self):
        """
        @summary: Call sizeof on each sub type
        @return: sum of sizeof of each Type attributes
        """
        if self._is_readed and not self._read_len is None:
            return self._read_len()

        size = 0
        for name in self._type_name:
            size += sizeof(self.__dict__[name])
        return size

    def __eq__(self, other):
        """
        @summary:  Compare each properties which are Type inheritance
                    if one is different then not equal
        @param other: CompositeType
        @return: True if each sub-type are equals
        """
        if self._type_name != other._typeName:
            return False
        for name in self._type_name:
            if self.__dict__[name] != other.__dict__[name]:
                return False
        return True

    def __ne__(self, other):
        """
        @summary: return not equal result operator
        @param other: CompositeType
        @return: False if each subtype are equals
        """
        return not self.__eq__(other)

"""
All simple Raw type use in RDPY
"""

class UInt8(SimpleType):
    """
    @summary: unsigned byte
    """
    def __init__(self, value = 0, conditional = lambda:True, optional = False, constant = False):
        """
        @param value: python value wrap
        @param conditional :    Callable object
                                 Read and Write operation depend on return of this function
        @param optional:   If there is no enough byte in current stream
                            And optional is True, read type is ignored
        @param constant:   Check if object value doesn't change after read operation
        """
        SimpleType.__init__(self, "B", 1, False, value, conditional = conditional, optional = optional, constant = constant)

class SInt8(SimpleType):
    """
    @summary: signed byte
    """
    def __init__(self, value = 0, conditional = lambda:True, optional = False, constant = False):
        """
        @param value: python value wrap
        @param conditional :    Callable object
                                 Read and Write operation depend on return of this function
        @param optional:   If there is no enough byte in current stream
                            And optional is True, read type is ignored
        @param constant:   Check if object value doesn't change after read operation
        """
        SimpleType.__init__(self, "b", 1, True, value, conditional = conditional, optional = optional, constant = constant)


class UInt16Be(SimpleType):
    """
    @summary: unsigned short
               with Big endian representation in stream
    """
    def __init__(self, value = 0, conditional = lambda:True, optional = False, constant = False):
        """
        @param value: python value wrap
        @param conditional :    Callable object
                                 Read and Write operation depend on return of this function
        @param optional:   If there is no enough byte in current stream
                            And optional is True, read type is ignored
        @param constant:   Check if object value doesn't change after read operation
        """
        SimpleType.__init__(self, ">H", 2, False, value, conditional = conditional, optional = optional, constant = constant)

class UInt16Le(SimpleType):
    """
    @summary: unsigned short
               with Little endian representation in stream
    """
    def __init__(self, value = 0, conditional = lambda:True, optional = False, constant = False):
        """
        @param value: python value wrap
        @param conditional :    Callable object
                                 Read and Write operation depend on return of this function
        @param optional:   If there is no enough byte in current stream
                            And optional is True, read type is ignored
        @param constant:   Check if object value doesn't change after read operation
        """
        SimpleType.__init__(self, "<H", 2, False, value, conditional = conditional, optional = optional, constant = constant)

class SInt16Le(SimpleType):
    """
    @summary: signed short
               with Little endian representation in stream
    """
    def __init__(self, value = 0, conditional = lambda:True, optional = False, constant = False):
        """
        @param value: python value wrap
        @param conditional :    Callable object
                                 Read and Write operation depend on return of this function
        @param optional:   If there is no enough byte in current stream
                            And optional is True, read type is ignored
        @param constant:   Check if object value doesn't change after read operation
        """
        SimpleType.__init__(self, "<h", 2, True, value, conditional = conditional, optional = optional, constant = constant)

class UInt32Be(SimpleType):
    """
    @summary: unsigned int
               with Big endian representation in stream
    """
    def __init__(self, value = 0, conditional = lambda:True, optional = False, constant = False):
        """
        @param value: python value wrap
        @param conditional :    Callable object
                                 Read and Write operation depend on return of this function
        @param optional:   If there is no enough byte in current stream
                            And optional is True, read type is ignored
        @param constant:   Check if object value doesn't change after read operation
        """
        SimpleType.__init__(self, ">I", 4, False, value, conditional = conditional, optional = optional, constant = constant)

class UInt32Le(SimpleType):
    """
    @summary: unsigned int
               with Little endian representation in stream
    """
    def __init__(self, value = 0, conditional = lambda:True, optional = False, constant = False):
        """
        @param value: python value wrap
        @param conditional :    Callable object
                                 Read and Write operation depend on return of this function
        @param optional:   If there is no enough byte in current stream
                            And optional is True, read type is ignored
        @param constant:   Check if object value doesn't change after read operation
        """
        SimpleType.__init__(self, "<I", 4, False, value, conditional = conditional, optional = optional, constant = constant)

class SInt32Le(SimpleType):
    """
    @summary: signed int
               with Little endian representation in stream
    """
    def __init__(self, value = 0, conditional = lambda:True, optional = False, constant = False):
        """
        @param value: python value wrap
        @param conditional :    Callable object
                                 Read and Write operation depend on return of this function
        @param optional:   If there is no enough byte in current stream
                            And optional is True, read type is ignored
        @param constant:   Check if object value doesn't change after read operation
        """
        SimpleType.__init__(self, "<I", 4, True, value, conditional = conditional, optional = optional, constant = constant)

class SInt32Be(SimpleType):
    """
    @summary: signed int
               with Big endian representation in stream
    """
    def __init__(self, value = 0, conditional = lambda:True, optional = False, constant = False):
        """
        @param value: python value wrap
        @param conditional :    Callable object
                                 Read and Write operation depend on return of this function
        @param optional:   If there is no enough byte in current stream
                            And optional is True, read type is ignored
        @param constant:   Check if object value doesn't change after read operation
        """
        SimpleType.__init__(self, ">I", 4, True, value, conditional = conditional, optional = optional, constant = constant)

class UInt24Be(SimpleType):
    """
    @summary: unsigned 24 bit integer
               with Big endian representation in stream
    """
    def __init__(self, value = 0, conditional = lambda:True, optional = False, constant = False):
        """
        @param value: python value wrap
        @param conditional :    Callable object
                                 Read and Write operation depend on return of this function
        @param optional:   If there is no enough byte in current stream
                            And optional is True, read type is ignored
        @param constant:   Check if object value doesn't change after read operation
        """
        SimpleType.__init__(self, ">I", 3, False, value, conditional = conditional, optional = optional, constant = constant)

    def __write__(self, s):
        """
        @summary: special write for a special type
        @param s: Stream
        """
        s.write(struct.pack(">I", self.value)[1:])

    def __read__(self, s):
        """
        @summary: special read for a special type
        @param s: Stream
        """
        self.value = struct.unpack(self._structFormat, b'\x00' + s.read(self._typeSize))[0]


class UInt24Le(SimpleType):
    """
    @summary: unsigned 24 bit integer
               with Little endian representation in stream
    """
    def __init__(self, value = 0, conditional = lambda:True, optional = False, constant = False):
        """
        @param value: python value wrap
        @param conditional :    Callable object
                                 Read and Write operation depend on return of this function
        @param optional:   If there is no enough byte in current stream
                            And optional is True, read type is ignored
        @param constant:   Check if object value doesn't change after read operation
        """
        SimpleType.__init__(self, "<I", 3, False, value, conditional = conditional, optional = optional, constant = constant)

    def __write__(self, s):
        """
        @summary: special write for a special type
        @param s: Stream
        """
        # don't write first byte
        s.write(struct.pack("<I", self.value)[:3])

    def __read__(self, s):
        """
        @summary: special read for a special type
        @param s: Stream
        """
        self.value = struct.unpack(self._structFormat, s.read(self._typeSize) + b'\x00')[0]


class Buffer(DynMessage):
    """
    This a raw binary bytes data
    """
    def __init__(self, value: bytes = b"", read_len=None, conditional=lambda:True, optional: bool = False, constant: bool = False, until: bytes = None, readLen=None, unicode=False):
        """
        """
        super().__init__(conditional=conditional, optional=optional, constant=constant)
        # type use to know read length
        self._read_len = read_len if read_len else readLen
        self._until = until
        self.value = value

    def __eq__(self, other):
        """
        """
        return self.value.__eq__(other.value)

    def __ne__(self, other):
        """
        """
        return self.value.__ne__(other.value)

    def __hash__(self):
        """
        """
        return hash(self.value)

    def __str__(self):
        """
        """
        return self.value

    def __write__(self, s):
        """

        """
        to_write = self.value

        if not self._until is None:
            to_write += self._until
        if isinstance(to_write, str):
            to_write = to_write.encode('utf-8')
        s.write(to_write)

    def __read__(self, s):
        """
        """
        if self._read_len is None:
            if self._until is None:
                self.value = s.getvalue()[s.tell():]
            else:
                self.value = ""
                while self.value[-len(self._until):] != self._until and s.data_len() != 0:
                    self.value += s.read(1)
        else:
            self.value = s.read(self._read_len())

    def __sizeof__(self):
        """
        @summary:  return length of string
                    if string is unicode encode return 2*len(str) + 2
        @return: length of inner string
        """
        return len(self.value)


def encodeUnicode(s):
    """
    @summary: Encode string in unicode
    @param s: str python
    @return: unicode string
    """
    return "".join([c + "\x00" for c in s]) + "\x00\x00"

def decodeUnicode(s):
    """
    @summary: Decode Unicode string
    @param s: unicode string
    @return: str python
    """
    i = 0
    r = ""
    while i < len(s) - 2:
        if i % 2 == 0:
            r += s[i]
        i += 1
    return r


class Stream(BytesIO):
    """
    @summary:  Stream use to read all types
    """
    def __init__(self, initial_bytes = ...):
        # print('initial_bytes:', repr(initial_bytes)) # '\x00\x00\x00\x00'
        if isinstance(initial_bytes, str):
            initial_bytes = initial_bytes.encode('utf-8')

        if initial_bytes is ...:
            super().__init__()
        else:
            super().__init__(initial_bytes)

    # @property
    # def buflist(self):
    #     buflist = self.getvalue()
    #     buflist = [bytes(e).decode() for e in buflist]
    #     # print('buflist:', repr(buflist))
    #     return buflist
    
    def data_len(self) -> int:
        """
        :returns: not yet read length
        """
        value_len = len(self.getvalue()) 
        pos = self.tell()
        # print('value len',value_len, 'pos', pos)
        return value_len - pos

    def read_len(self) -> int:
        """
        Compute already read size
        :returns: read size of stream
        """
        # return self.seek()
        return self.tell()
    
    def readType(self, value:Message):
        return self.read_type(value)

    def read_type(self, value: Message):
        """
        Call specific read on type object
        or iterate over tuple elements
        rollback read if error occurred during read value
        :ivar tuple | Type object
        """
        # read each tuple
        if isinstance(value, tuple) or isinstance(value, list):
            for element in value:
                try:
                    self.read_type(element)
                except Exception as e:
                    # rollback already readed elements
                    for tmpElement in value:
                        if tmpElement == element:
                            break
                        self.seek(-sizeof(tmpElement))
                        # self.pos -= sizeof(tmpElement)
                    raise e
            return value

        # optional value not present
        if self.data_len() == 0 and value._optional:
            return

        value.read(self)
        return value
    
    def get_pos(self):
        return self.tell()

    def set_pos(self, pos):
        self.seek(pos)
    
    pos = property(get_pos, set_pos)

    def readNextType(self, t):
        """
        @summary: read next type but didn't consume it
        @param t: Type element
        """
        self.read_type(t)
        self.seek(-sizeof(t))
        # self.pos -= sizeof(t)

    def write_type(self, value: Message):
        """
        Call specific write on type object
        or iterate over tuple element

        :ivar Type: Type to write
        """
        # write each element of tuple
        if isinstance(value, tuple) or isinstance(value, list):
            for element in value:
                self.write_type(element)
            return self
        value.write(self)
        return self


class ArrayType(Message):
    """
    @summary: Factory af n element
    """
    def __init__(self, type_factory, init=None, read_len=None, conditional=lambda:True, optional=False, constant=False, readLen = None):
        """
        """
        super().__init__(conditional, optional, constant)
        self._type_factory = type_factory
        self._read_len = read_len if read_len else readLen
        self._array = init or []

    def __read__(self, s):
        """
        """
        self._array = []
        i = 0
        # self._read_len is None means that array will be read until end of stream
        while self._read_len is None or i < self._read_len():
            element = self._type_factory()
            element._optional = self._read_len is None
            s.read_type(element)
            if not element._is_readed:
                break
            self._array.append(element)
            i += 1

    def __write__(self, s):
        """
        """
        s.write_type(self._array)

    def __getitem__(self, item):
        """
        @summary: Magic function to be FactoryType as transparent as possible
        @return: index of _value
        """
        return self._array.__getitem__(item)

    def __sizeof__(self):
        """
        @summary: Size in bytes of all inner type
        """
        return sizeof(self._array)

    def __len__(self):
        return len(self._array)

class FactoryType(Message):
    """
    @summary:  Call a factory callback at read or write time
                Wrapp attribute access to inner type
    """
    def __init__(self, factory, conditional = lambda:True, optional = False, constant = False):
        """
        @param factory: Call back call before read or write type
        @param conditional :    Callable object
                                 Read and Write operation depend on return of this function
        @param optional:   If there is no enough byte in current stream
                            And optional is True, read type is ignored
        @param constant:   Check if object value doesn't change after read operation
        """
        Message.__init__(self, conditional, optional, constant)
        self._factory = factory
        if not callable(factory):
            self._factory = lambda:factory

        self._value = None

    def __read__(self, s):
        """
        @summary: Call factory and write it
        @param s: Stream
        """
        self._value = self._factory()
        s.read_type(self._value)

    def __write__(self, s):
        """
        @summary: Call factory and read it
        @param s: Stream
        """
        self._value = self._factory()
        s.write_type(self._value)

    def __getattr__(self, name):
        """
        @summary: Magic function to be FactoryType as transparent as possible
        @return: _value parameter
        """
        return self._value.__getattribute__(name)

    def __getitem__(self, item):
        """
        @summary: Magic function to be FactoryType as transparent as possible
        @return: index of _value
        """
        return self._value.__getitem__(item)

    def __sizeof__(self):
        """
        @summary: Size of of object returned by factory
        @return: Size of of object returned by factory
        """
        return sizeof(self._value)

def CheckValueOnRead(cls):
    """
    @summary:  Wrap read method of class
                to check value on read
                if new value is different from old value
    @param cls: class that inherit from Type
    @raise InvalidValue: if constness is not respected
    """
    oldRead = cls.read
    def read(self, s):
        old = deepcopy(self)
        oldRead(self, s)
        if self != old:
            raise InvalidValue("CheckValueOnRead %s != %s"%(self, old))
    cls.read = read
    return cls


class String(DynMessage):
# class String(Type, CallableValue):
    """
    @summary:  String type
                Leaf in Type tree
    """
    def __init__(self, value = "", readLen = None, conditional = lambda:True, optional = False, constant = False, unicode = False, until = None):
        """
        @param value: python string use for inner value
        @param readLen: length use to read in stream (SimpleType) if 0 read entire stream
        @param conditional :    Callable object
                                 Read and Write operation depend on return of this function
        @param optional:   If there is no enough byte in current stream
                            And optional is True, read type is ignored
        @param constant:   Check if object value doesn't change after read operation
        @param unicode: Encode and decode value as unicode
        @param until: read until sequence is readed or write sequence at the end of string
        """
        super().__init__(conditional = conditional, optional = optional, constant = constant)
        # Type.__init__(self, conditional = conditional, optional = optional, constant = constant)
        # CallableValue.__init__(self, value)
        #type use to know read length
        self._readLen = readLen
        self._unicode = unicode
        self._until = until
        self.value = value
        
    def __eq__(self, other):
        """
        @summary: return equal result operator
        @param other: other String parameter
        @return: if two inner value are equals
        """
        return self.value == other.value


    def __ne__(self, other):
        """
        @summary: return not equal result operator
        @param other: other String parameter
        @return: if two inner value are not equals
        """
        return self.value != other.value
    
    def __hash__(self):
        """
        @summary: hash function to treat simple type in hash collection
        @return: hash of inner value
        """
        return hash(self.value)
    
    def __str__(self):
        """
        @summary: call when str function is call
        @return: inner python string
        """
        return self.value
    
    def __write__(self, s):
        """
        @summary:  Write the inner value after evaluation
                    Append until sequence if present
                    Encode in unicode format if asked
        @param s: Stream
        """
        toWrite = self.value
        
        if not self._until is None:
            toWrite += self._until
            
        if self._unicode:
            s.write(encodeUnicode(self.value))
        else:
            val = self.value.encode() if isinstance(self.value, str) else self.value
            s.write(val)
    
    def __read__(self, s):
        """
        @summary:  Read readLen bytes as string
                    If readLen is None read until 'until' sequence match
                    If until sequence is None read until end of stream
        @param s: Stream
        """
        if self._readLen is None:
            if self._until is None:
                self.value = s.getvalue()[s.pos:]
            else:
                self.value = ""
                while self.value[-len(self._until):] != self._until and s.dataLen() != 0:
                    self.value += s.read(1)
        else:
            self.value = s.read(self._readLen.value)
        
        if self._unicode:
            # self.value = self.value
            self.value = decodeUnicode(self.value)
        
    def __sizeof__(self):
        """
        @summary:  return length of string
                    if string is unicode encode return 2*len(str) + 2
        @return: length of inner string
        """
        if self._unicode:
            return 2 * len(self.value) + 2
        else:
            return len(self.value)