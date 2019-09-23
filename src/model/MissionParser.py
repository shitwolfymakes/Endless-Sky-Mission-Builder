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


class MissionParser(object):
    def __init__(self, mission):
        self.mission = mission
        self.components = mission.components
        self.lines = []
        self.tokens = []
    #end init


    def run(self):
        logging.debug("\tParsing mission...")
        self._add_line("mission \"%s\"" % self.mission.missionName)

        # mission display name
        if self._has_mission_display_name():
            logging.debug("\t\t")

        # description
        if self._has_description():
            logging.debug("\t\t")

        # isBlocked
        if self._has_blocked():
            logging.debug("\t\t")

        # deadline
        if self._has_deadline():
            logging.debug("\t\t")

        # cargo
        if self._has_cargo():
            logging.debug("\t\t")

        # passengers
        if self._has_passengers():
            logging.debug("\t\t")

        # illegal
        if self._has_illegal():
            logging.debug("\t\t")

        # stealth
        if self._has_stealth():
            logging.debug("\t\t")

        # isInvisible
        if self._has_invisible():
            logging.debug("\t\t")

        # priorityLevel
        if self._has_priority_level():
            logging.debug("\t\t")

        # whereShown
        if self._has_where_shown():
            logging.debug("\t\t")

        # repeat
        if self._has_repeat():
            logging.debug("\t\t")

        # clearance
        if self._has_clearance():
            logging.debug("\t\t")

        # isInfiltrating
        if self._has_infiltrating():
            logging.debug("\t\t")

        # waypoint
        if self._has_waypoint():
            logging.debug("\t\t")

        # stopover
        if self._has_stopover():
            logging.debug("\t\t")

        # source
        if self._has_source():
            logging.debug("\t\t")

        # destination
        if self._has_destination():
            logging.debug("\t\t")

        # Trigger(s)
        if self._has_triggers():
            logging.debug("\t\t")

        return self.lines
    #end run


    def _add_line(self, line):
        self.lines.append(line + "\n")
    #end add_line


    def _has_mission_display_name(self):
        if self.components.missionDisplayName is None:
            return False
        return True
    #def _has_mission_display_name


    def _has_description(self):
        if self.components.description is None:
            return False
        return True
    #end _has_description


    def _has_blocked(self):
        if self.components.blocked is None:
            return False
        return True
    #end _has_blocked


    def _has_deadline(self):
        if self.components.deadline.isActive is False:
            return False
        return True
    #def _has_deadline


    def _has_cargo(self):
        if self.components.cargo.isActive is False:
            return False
        return True
    #end _has_cargo


    def _has_passengers(self):
        if self.components.passenger.isActive is False:
            return False
        return True
    #end _has_passengers


    def _has_illegal(self):
        if self.components.illegal.isIllegal is False:
            return False
        return True
    #end _has_illegal


    def _has_stealth(self):
        if self.components.isStealth is False:
            return False
        return True
    #end _has_stealth


    def _has_invisible(self):
        if self.components.isInvisible is False:
            return False
        return True
    #end _hes_invisible


    def _has_priority_level(self):
        if self.components.priorityLevel is None:
            return False
        return True
    #end _has_priority_level


    def _has_where_shown(self):
        if self.components.whereShown is None:
            return False
        return True
    #end _has_where_shown


    def _has_repeat(self):
        if self.components.repeat.isActive is False:
            return False
        return True
    #end _has_repeat


    def _has_clearance(self):
        if self.components.clearance.isActive is False:
            return False
        return True
    #end _has_clearance


    def _has_infiltrating(self):
        if self.components.isInfiltrating is False:
            return False
        return True
    #end _has_infiltrating


    def _has_waypoint(self):
        if self.components.waypoint is None:
            return False
        return True
    #end _has_waypoint


    def _has_stopover(self):
        if self.components.stopover.isActive is False:
            return False
        return True
    # end _has_stopover


    def _has_source(self):
        if self.components.source.isActive is False:
            return False
        return True
    #end _has_source


    def _has_destination(self):
        if self.components.destination.isActive is False:
            return False
        return True
    #end _has_destination


    def _has_triggers(self):
        if not self.components.triggerList:
            return False
        return True
    #end _has_triggers

#end class MissionParser
