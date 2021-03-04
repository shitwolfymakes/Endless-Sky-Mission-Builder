""" MissionComponents.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

This file contains the classes defining the components of a mission
"""

import logging

import model.components as components

class MissionComponents:
    """This class keeps instances of each different component in one place, for easy access"""

    def __init__(self):
        #TODO: refactor to use Repeat object
        logging.debug("\tMission components initializing...")

        self.mission_display_name = None            # mission <name>
        self.description = None                     # description <text>
        self.blocked = None                         # blocked <message>
        self.deadline = components.Deadline()
        self.cargo = components.Cargo()
        self.passengers = components.Passengers()
        self.illegal = components.Illegal()
        self.is_stealth = False
        self.is_invisible = False                   # invisible
        self.priority_level = None                  # (priority | minor)
        self.where_shown = None                     # (job | landing | assisting | boarding)
        self.repeat = components.Repeat()
        self.clearance = components.Clearance()
        self.is_infiltrating = False                # infiltrating
        self.waypoint = None                        # waypoint <system>
        self.stopover = components.Stopover()
        self.source = components.Source()
        self.destination = components.Destination()
        self.trigger_list = []
    #end init
#end class MissionComponents
