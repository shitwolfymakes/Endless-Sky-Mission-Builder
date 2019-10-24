""" Conversation.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""
import logging

import src.model as model


class Event(model.FileItem):
    #TODO: implement this
    def __init__(self, name):
        logging.debug("Building event %s", name)

        super().__init__("event")
        self.name = name

        self.parse()
    #end init


    def print_item_lines_to_text(self):
        """Concatenate all the lines together. Used to make a block of text to display in the item_text_pane."""
        # Note to self: this is the most efficient and pythonic way to concat all these strings together
        event_text = "".join(self.lines)
        return event_text
    #end print_item_lines_to_text


    def parse(self):
        pass
    #end parse


    def to_string(self):
        pass
    #end to_string
#end class Event
