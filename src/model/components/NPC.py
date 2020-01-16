""" NPC.py
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


class NPC:
    """This object stores data for npc objects inside Endless Sky mission objects"""
    #TODO: implement this
    def __init__(self, name):
        logging.debug("\t\tComponent %s initializing..." % self.__class__)

        self.is_active = False
        self.name = name
    #end init
#end class NPC
