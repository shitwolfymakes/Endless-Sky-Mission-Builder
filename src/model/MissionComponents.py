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

import src.model.components as components


class MissionComponents:
    """This class keeps instances of each different component in one place, for easy access"""

    def __init__(self):
        #TODO: refactor to use Repeat object
        logging.debug("\tMission components initializing...")

        self.missionDisplayName = None          # mission <name>
        self.description        = None          # description <text>
        self.blocked            = None          # blocked <message>
        self.deadline           = components.Deadline()
        self.cargo              = components.Cargo()
        self.passengers         = components.Passengers()
        self.illegal            = components.Illegal()
        self.isStealth          = False
        self.isInvisible        = False         # invisible
        self.priorityLevel      = None          # (priority | minor)
        self.whereShown         = None          # (job | landing | assisting | boarding)
        self.repeat             = components.Repeat()
        self.clearance          = components.Clearance()
        self.isInfiltrating     = False         # infiltrating
        self.waypoint           = None          # waypoint <system>
        self.stopover           = components.Stopover()
        self.source             = components.Source()
        self.destination        = components.Destination()
        self.triggerList        = []
    #end init

#end class MissionComponents
