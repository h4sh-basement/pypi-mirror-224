# Copyright 2023 Marc Lehmann

# This file is part of tablecache.
#
# tablecache is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# tablecache is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with tablecache. If not, see <https://www.gnu.org/licenses/>.

import abc
import datetime
import math
import numbers
import struct
import typing as t
import uuid


class Codec(abc.ABC):
    """
    Abstract base for codecs.

    A codec can encode certain values to bytes, then decode those back to the
    original value.

    If an input value for encoding or decoding is unsuitable in any way, a
    ValueError is raised.
    """
    T = t.TypeVar('T')

    @abc.abstractmethod
    def encode(self, value: T) -> bytes:
        raise NotImplementedError

    @abc.abstractmethod
    def decode(self, bs: bytes) -> T:
        raise NotImplementedError


class Nullable(Codec):
    """
    Wrapper codec that allows representing nullable values.

    Encodes optional values by using an inner codec for values, and a marker
    for None.
    """
    def __init__(self, value_codec):
        self._value_codec = value_codec

    def encode(self, value: t.Optional[t.Any]) -> bytes:
        if value is None:
            return b'\x00'
        return b'\x01' + self._value_codec.encode(value)

    def decode(self, bs: bytes) -> t.Optional[t.Any]:
        if bs == b'\x00':
            return None
        return self._value_codec.decode(bs[1:])


class BoolCodec(Codec):
    """Codec that represents bools as single bytes."""
    def encode(self, value: bool) -> bytes:
        if not isinstance(value, bool):
            raise ValueError('Value is not a bool.')
        return b'\x01' if value else b'\x00'

    def decode(self, bs: bytes) -> bool:
        if bs == b'\x00':
            return False
        if bs == b'\x01':
            return True
        raise ValueError('Invalid bool representation.')


class StringCodec(Codec):
    """Simple str<->bytest codec (UTF-8)."""
    def encode(self, value: str) -> bytes:
        if not isinstance(value, str):
            raise ValueError('Value is not a string.')
        return value.encode()

    def decode(self, bs: bytes) -> str:
        return bs.decode()


class IntAsStringCodec(Codec):
    """Codec that represents ints as strings."""
    def encode(self, value: int) -> bytes:
        if not isinstance(value, int):
            raise ValueError('Value is not an int.')
        return str(value).encode()

    def decode(self, bs: bytes) -> int:
        return int(bs.decode())


class FloatAsStringCodec(Codec):
    """
    Codec that represents floats as strings.

    Handles infinities and NaNs, but makes no distinction between signalling
    NaNs (all NaNs are decoded to quiet NaNs).
    """
    def encode(self, value: numbers.Real) -> bytes:
        if not isinstance(value, numbers.Real):
            raise ValueError('Value is not a real number.')
        return str(value).encode()

    def decode(self, bs: bytes) -> numbers.Real:
        return float(bs.decode())


class EncodedNumberCodec(Codec):
    """Codec that encodes numbers to bytes directly."""
    NumberType = t.TypeVar('NumberType')

    def __init__(self, struct_format: str) -> None:
        self._struct_format = struct_format

    def encode(self, value: NumberType) -> bytes:
        try:
            return struct.pack(self._struct_format, value)
        except struct.error as e:
            raise ValueError('Unable to encode number.') from e

    def decode(self, bs: bytes) -> NumberType:
        try:
            value, = struct.unpack(self._struct_format, bs)
        except struct.error as e:
            raise ValueError('Unable to decode number.') from e
        return value


class EncodedIntCodec(EncodedNumberCodec):
    NumberType = int


class SignedInt8Codec(EncodedIntCodec):
    def __init__(self) -> None:
        super().__init__('>b')


class SignedInt16Codec(EncodedIntCodec):
    def __init__(self) -> None:
        super().__init__('>h')


class SignedInt32Codec(EncodedIntCodec):
    def __init__(self) -> None:
        super().__init__('>i')


class SignedInt64Codec(EncodedIntCodec):
    def __init__(self) -> None:
        super().__init__('>q')


class UnsignedInt8Codec(EncodedIntCodec):
    def __init__(self) -> None:
        super().__init__('>B')


class UnsignedInt16Codec(EncodedIntCodec):
    def __init__(self) -> None:
        super().__init__('>H')


class UnsignedInt32Codec(EncodedIntCodec):
    def __init__(self) -> None:
        super().__init__('>I')


class UnsignedInt64Codec(EncodedIntCodec):
    def __init__(self) -> None:
        super().__init__('>Q')


class EncodedFloatCodec(EncodedNumberCodec):
    NumberType = float
    """
    Codec that encodes floats to bytes directly.

    Infinities and NaNs are handled. Signalling NaNs mostly work, with the
    exception that the most significant bit of the signalling part is always 1
    (i.e. single-precision NaNs always start with 7fc or ffc, and double
    precision with 7ff8 or fff8).
    """


class Float32Codec(EncodedFloatCodec):
    _min_value, = struct.unpack('>f', bytes.fromhex('ff7fffff'))
    _max_value, = struct.unpack('>f', bytes.fromhex('7f7fffff'))

    def __init__(self) -> None:
        super().__init__('>f')

    def encode(self, value: float) -> bytes:
        encoded = super().encode(value)
        if not math.isinf(value) and (value < self._min_value
                                      or value > self._max_value):
            raise ValueError('Value is outside of float32 range.')
        return encoded


class Float64Codec(EncodedFloatCodec):
    def __init__(self) -> None:
        super().__init__('>d')


class UuidCodec(Codec):
    """Codec for UUIDs."""
    def encode(self, value: uuid.UUID) -> bytes:
        if not isinstance(value, uuid.UUID):
            raise ValueError('Value is not a UUID.')
        return value.bytes

    def decode(self, bs: bytes) -> uuid.UUID:
        return uuid.UUID(bytes=bs)


class NaiveDatetimeCodec(Codec):
    """
    Codec for timezone-unaware datetimes.

    Encodes values as an epoch timestamp in a double precision float, so
    precision is limited to that value range.

    Will encode timezone-aware datetimes, but drop any timezone information
    during encoding.
    """
    def __init__(self):
        self._float_codec = Float64Codec()

    def encode(self, value: datetime.datetime) -> bytes:
        if not isinstance(value, datetime.datetime):
            raise ValueError('Value is not a datetime.')
        try:
            return self._float_codec.encode(value.timestamp())
        except Exception as e:
            raise ValueError('Unable to encode timestamp as float.') from e

    def decode(self, bs: bytes) -> datetime.datetime:
        try:
            timestamp = self._float_codec.decode(bs)
            return datetime.datetime.fromtimestamp(timestamp)
        except Exception as e:
            raise ValueError('Unable to decode timestamp float.') from e
