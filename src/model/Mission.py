""" Mission.py
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

from model.model_data_parsers import MissionParser

import model



class Mission(model.FileItem):
    """The Mission class is the data structure that stores the data for an Endless Sky mission."""

    def __init__(self, name):
        logging.debug("Building mission: %s" % name)

        super().__init__("mission")
        self.components = model.MissionComponents()
        self.name = name

        self.parse()
    #end init


    def parse(self):
        parser = MissionParser(self)
        self.lines = parser.run()
    #end parse


    def add_trigger(self):
        """Add a trigger object to this mission"""
        new_trigger = model.components.Trigger()
        self.components.trigger_list.append(new_trigger)
        return new_trigger
    #end add_trigger


    def remove_trigger(self, trigger):
        """Remove a trigger object from this mission"""
        self.components.trigger_list.remove(trigger)
    #end remove_trigger


    def to_string(self):
        return "".join(self.lines)
    #end to_string
#end class Mission
