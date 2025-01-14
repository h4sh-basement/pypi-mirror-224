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


class UpdateUserTyping(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~geezlibs.raw.base.Update`.

    Details:
        - Layer: ``148``
        - ID: ``C01E857F``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        action (:obj:`SendMessageAction <geezlibs.raw.base.SendMessageAction>`):
            N/A

    """

    __slots__: List[str] = ["user_id", "action"]

    ID = 0xc01e857f
    QUALNAME = "types.UpdateUserTyping"

    def __init__(self, *, user_id: int, action: "raw.base.SendMessageAction") -> None:
        self.user_id = user_id  # long
        self.action = action  # SendMessageAction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUserTyping":
        # No flags
        
        user_id = Long.read(b)
        
        action = TLObject.read(b)
        
        return UpdateUserTyping(user_id=user_id, action=action)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(self.action.write())
        
        return b.getvalue()
