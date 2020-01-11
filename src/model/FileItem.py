""" FileItem.py Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""

from abc import ABC, abstractmethod


class FileItem(ABC):
    def __init__(self, item_type):
        self.type = item_type
        self.name = None
        self.lines = []
    #end def


    def add_line(self, line):
        self.lines.append(line + "\n")
    # end add_line


    @abstractmethod
    def parse(self):
        pass
    #end parse


    @abstractmethod
    def to_string(self):
        """Concatenate all the lines together. Used to make a block of text to display in the item_text_pane."""
        # Note to self: this is the most efficient and pythonic way to concat all these strings together
        item_text = "".join(self.lines)
        return item_text
    #end to_string
#end class FileItem
