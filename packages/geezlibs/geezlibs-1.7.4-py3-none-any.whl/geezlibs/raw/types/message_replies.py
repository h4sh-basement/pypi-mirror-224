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


class MessageReplies(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~geezlibs.raw.base.MessageReplies`.

    Details:
        - Layer: ``148``
        - ID: ``83D60FC2``

    Parameters:
        replies (``int`` ``32-bit``):
            N/A

        replies_pts (``int`` ``32-bit``):
            N/A

        comments (``bool``, *optional*):
            N/A

        recent_repliers (List of :obj:`Peer <geezlibs.raw.base.Peer>`, *optional*):
            N/A

        channel_id (``int`` ``64-bit``, *optional*):
            N/A

        max_id (``int`` ``32-bit``, *optional*):
            N/A

        read_max_id (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["replies", "replies_pts", "comments", "recent_repliers", "channel_id", "max_id", "read_max_id"]

    ID = 0x83d60fc2
    QUALNAME = "types.MessageReplies"

    def __init__(self, *, replies: int, replies_pts: int, comments: Optional[bool] = None, recent_repliers: Optional[List["raw.base.Peer"]] = None, channel_id: Optional[int] = None, max_id: Optional[int] = None, read_max_id: Optional[int] = None) -> None:
        self.replies = replies  # int
        self.replies_pts = replies_pts  # int
        self.comments = comments  # flags.0?true
        self.recent_repliers = recent_repliers  # flags.1?Vector<Peer>
        self.channel_id = channel_id  # flags.0?long
        self.max_id = max_id  # flags.2?int
        self.read_max_id = read_max_id  # flags.3?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReplies":
        
        flags = Int.read(b)
        
        comments = True if flags & (1 << 0) else False
        replies = Int.read(b)
        
        replies_pts = Int.read(b)
        
        recent_repliers = TLObject.read(b) if flags & (1 << 1) else []
        
        channel_id = Long.read(b) if flags & (1 << 0) else None
        max_id = Int.read(b) if flags & (1 << 2) else None
        read_max_id = Int.read(b) if flags & (1 << 3) else None
        return MessageReplies(replies=replies, replies_pts=replies_pts, comments=comments, recent_repliers=recent_repliers, channel_id=channel_id, max_id=max_id, read_max_id=read_max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.comments else 0
        flags |= (1 << 1) if self.recent_repliers else 0
        flags |= (1 << 0) if self.channel_id is not None else 0
        flags |= (1 << 2) if self.max_id is not None else 0
        flags |= (1 << 3) if self.read_max_id is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.replies))
        
        b.write(Int(self.replies_pts))
        
        if self.recent_repliers is not None:
            b.write(Vector(self.recent_repliers))
        
        if self.channel_id is not None:
            b.write(Long(self.channel_id))
        
        if self.max_id is not None:
            b.write(Int(self.max_id))
        
        if self.read_max_id is not None:
            b.write(Int(self.read_max_id))
        
        return b.getvalue()
