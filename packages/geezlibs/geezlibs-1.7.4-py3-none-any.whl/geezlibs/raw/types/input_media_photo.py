#  GeezLibs - Telegram MTProto API Client Library for Python.
#  Copyright (C) 2022-2023 izzy<https://github.com/hitokizzy>
#
#  This file is part of GeezLibs.
#
#  GeezLibs is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  GeezLibs is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with GeezLibs.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from geezlibs.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from geezlibs.raw.core import TLObject
from geezlibs import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class InputMediaPhoto(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~geezlibs.raw.base.InputMedia`.

    Details:
        - Layer: ``148``
        - ID: ``B3BA0635``

    Parameters:
        id (:obj:`InputPhoto <geezlibs.raw.base.InputPhoto>`):
            N/A

        ttl_seconds (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "ttl_seconds"]

    ID = 0xb3ba0635
    QUALNAME = "types.InputMediaPhoto"

    def __init__(self, *, id: "raw.base.InputPhoto", ttl_seconds: Optional[int] = None) -> None:
        self.id = id  # InputPhoto
        self.ttl_seconds = ttl_seconds  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaPhoto":
        
        flags = Int.read(b)
        
        id = TLObject.read(b)
        
        ttl_seconds = Int.read(b) if flags & (1 << 0) else None
        return InputMediaPhoto(id=id, ttl_seconds=ttl_seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ttl_seconds is not None else 0
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        return b.getvalue()
