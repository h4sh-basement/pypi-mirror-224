#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class UpdateStory(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``160``
        - ID: ``205A4133``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        story (:obj:`StoryItem <pyrogram.raw.base.StoryItem>`):
            N/A

    """

    __slots__: List[str] = ["user_id", "story"]

    ID = 0x205a4133
    QUALNAME = "types.UpdateStory"

    def __init__(self, *, user_id: int, story: "raw.base.StoryItem") -> None:
        self.user_id = user_id  # long
        self.story = story  # StoryItem

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStory":
        # No flags
        
        user_id = Long.read(b)
        
        story = TLObject.read(b)
        
        return UpdateStory(user_id=user_id, story=story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(self.story.write())
        
        return b.getvalue()
