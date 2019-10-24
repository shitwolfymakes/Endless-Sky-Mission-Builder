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


class Conversation:
    #TODO: Create objects for labels, choices, and branches to be stored in convo_parts_list
    def __init__(self):
        logging.debug("\t\tComponent %s initializing..." % self.__class__)

        self.name = None
        self.scene_image = None
        self.convo_parts_list = []
        self.lines = []
    #end init
#end class Conversation
