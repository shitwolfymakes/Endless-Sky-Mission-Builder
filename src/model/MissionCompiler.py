""" MissionCompiler.py
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

from src import config


class MissionCompiler:
    """This class compiles the data the user has entered into the current Mission object"""

    def __init__(self):
        self.editor = config.gui.center_pane
        self.mission = config.active_item.components
    #end init


    def run(self):
        """
        Zero the Mission data, then store what data is selected based on the value of the corresponding entry state
        """
        logging.debug("\tCompiling mission...")
        self._reset_mission_to_default()

        # mission display name
        if self.editor.display_name_component.listEntryStates[0].get():
            logging.debug("\t\tFound display name: %s" % self.editor.display_name_component.listEntryData[0].get())
            self.mission.mission_display_name = self.editor.display_name_component.listEntryData[0].get()
        #end if

        # description
        if self.editor.description_component.listEntryStates[0].get():
            logging.debug("\t\tFound description: %s" % self.editor.description_component.listEntryData[0].get())
            self.mission.description = self.editor.description_component.listEntryData[0].get()
        #end if

        # isBlocked
        if self.editor.blocked_component.listEntryStates[0].get():
            logging.debug("\t\tFound block: %s" % self.editor.blocked_component.listEntryData[0].get())
            self.mission.blocked = self.editor.blocked_component.listEntryData[0].get()
        #end if

        # deadline
        if self.editor.deadline_component.listEntryStates[0].get():
            logging.debug("\t\tFound deadline")
            self.mission.deadline.is_active = True
            if self.editor.deadline_component.listEntryStates[1].get():
                logging.debug("\t\t\tFound deadline days: %s" % self.editor.deadline_component.listEntryData[0].get())
                self.mission.deadline.deadline[0] = self.editor.deadline_component.listEntryData[0].get()
                if self.editor.deadline_component.listEntryStates[2].get():
                    logging.debug("\t\t\tFound deadline message: %s" % self.editor.deadline_component.listEntryData[1].get())
                    self.mission.deadline.deadline[1] = self.editor.deadline_component.listEntryData[1].get()
                #end if
            #end if
        #end if

        # cargo
        if self.editor.cargo_component.listEntryStates[0].get():
            logging.debug("\t\tFound cargo:")
            logging.debug("\t\t\t%s" % self.editor.cargo_component.listEntryData[0].get())
            logging.debug("\t\t\t%s" % self.editor.cargo_component.listEntryData[1].get())
            self.mission.cargo.is_active = True
            self.mission.cargo.cargo[0] = self.editor.cargo_component.listEntryData[0].get()
            self.mission.cargo.cargo[1] = self.editor.cargo_component.listEntryData[1].get()
            if self.editor.cargo_component.listEntryStates[1].get():
                logging.debug("\t\t\tFound cargo optional modifiers:")
                logging.debug("\t\t\t\t%s" % self.editor.cargo_component.listEntryData[2].get())
                self.mission.cargo.cargo[2] = self.editor.cargo_component.listEntryData[2].get()
                if self.editor.cargo_component.listEntryStates[2].get():
                    logging.debug("\t\t\t\t%s" % self.editor.cargo_component.listEntryData[3].get())
                    self.mission.cargo.cargo[3] = self.editor.cargo_component.listEntryData[3].get()
                #end if
            #end if
        #end if

        # passengers
        if self.editor.passengers_component.listEntryStates[0].get():
            logging.debug("\t\tFound passengers: %s" % self.editor.passengers_component.listEntryData[0].get())
            self.mission.passengers.is_active = True
            self.mission.passengers.passengers[0] = self.editor.passengers_component.listEntryData[0].get()
            if self.editor.passengers_component.listEntryStates[1].get():
                logging.debug("\t\t\tFound passengers optional data:")
                logging.debug("\t\t\t\t%s" % self.editor.passengers_component.listEntryData[1].get())
                self.mission.passengers.passengers[1] = self.editor.passengers_component.listEntryData[1].get()
                if self.editor.passengers_component.listEntryStates[2].get():
                    logging.debug("\t\t\t\t%s" % self.editor.passengers_component.listEntryData[2].get())
                    self.mission.passengers.passengers[2] = self.editor.passengers_component.listEntryData[2].get()
                #end if
            #end if
        #end if

        # illegal
        if self.editor.illegal_component.listEntryStates[0].get():
            logging.debug("\t\tFound illegal: %s" % self.editor.illegal_component.listEntryData[0].get())
            self.mission.illegal.is_active = True
            self.mission.illegal.illegal[0] = self.editor.illegal_component.listEntryData[0].get()
            if self.editor.illegal_component.listEntryStates[1].get():
                logging.debug("\t\t\tFound illegal optional modifier: %s" % self.editor.illegal_component.listEntryData[1].get())
                self.mission.illegal.illegal[1] = self.editor.illegal_component.listEntryData[1].get()
            # end if
        # end if

        # stealth
        if self.editor.stealth_component.listEntryStates[0].get():
            logging.debug("\t\tFound stealth modifier")
            self.mission.is_stealth = True
        # end if

        # isInvisible
        if self.editor.invisible_component.listEntryStates[0].get():
            logging.debug("\t\tFound mission invisible modifier")
            self.mission.is_invisible = True
        #end if

        # priorityLevel
        if self.editor.priority_level_component.is_active.get():
            logging.debug("\t\tFound priority level: %s" % self.editor.priority_level_component.combo.get().lower())
            self.mission.priority_level = self.editor.priority_level_component.combo.get().lower()
        #end if

        # whereShown
        if self.editor.where_shown_component.is_active.get():
            logging.debug("\t\tFound where shown: %s" % self.editor.where_shown_component.combo.get().lower())
            self.mission.where_shown = self.editor.where_shown_component.combo.get().lower()
        # end if

        # repeat
        if self.editor.repeat_component.listEntryStates[0].get():
            logging.debug("\t\tFound repeat")
            self.mission.repeat.is_active = True
            if self.editor.repeat_component.listEntryStates[1].get():
                logging.debug("\t\t\tFound repeat optionals modifier: %s" % self.editor.repeat_component.listEntryData[0].get())
                self.mission.repeat.repeat = self.editor.repeat_component.listEntryData[0].get()
            #end if
        #end if

        # clearance
        #TODO: fully implement this when filters are implemented
        if self.editor.clearance_component.listEntryStates[0].get():
            logging.debug("\t\tFound clearance: %s" % self.editor.clearance_component.listEntryData[0].get())
            self.mission.clearance.is_active = True
            self.mission.clearance.clearance = self.editor.clearance_component.listEntryData[0].get()
        #end if

        # infiltrating
        if self.editor.infiltrating_component.listEntryStates[0].get():
            logging.debug("\t\tFound infiltrating")
            self.mission.is_infiltrating = True
        #end if

        # waypoint
        if self.editor.waypoint_component.listEntryStates[0].get():
            logging.debug("\t\tFound waypoint: %s" % self.editor.waypoint_component.listEntryData[0].get())
            self.mission.waypoint = self.editor.waypoint_component.listEntryData[0].get()
        #end if

        # stopover
        #TODO: fully implement this when filters are implemented
        if self.editor.stopover_component.listEntryStates[0].get():
            logging.debug("\t\tFound stopover: %s" % self.editor.stopover_component.listEntryData[0].get())
            self.mission.stopover.is_active = True
            self.mission.stopover.stopover = self.editor.stopover_component.listEntryData[0].get()
        #end if

        # source
        #TODO: fully implement this when filters are implemented
        if self.editor.source_component.listEntryStates[0].get():
            logging.debug("\t\tFound source: %s" % self.editor.source_component.listEntryData[0].get())
            self.mission.source.is_active = True
            self.mission.source.source = self.editor.source_component.listEntryData[0].get()
        #end if

        # destination
        # TODO: fully implement this when filters are implemented
        if self.editor.destination_component.listEntryStates[0].get():
            logging.debug("\t\tFound source: %s" % self.editor.destination_component.listEntryData[0].get())
            self.mission.destination.is_active = True
            self.mission.destination.destination = self.editor.destination_component.listEntryData[0].get()
        # end if

        # Trigger data is compiled when TriggerWindow is closed

        # call the parser to save the new data
        config.active_item.parse()
    #end run


    def _reset_mission_to_default(self):
        self.mission.mission_display_name = None
        self.mission.description = None
        self.mission.blocked = None
        self.mission.deadline.reset()
        self.mission.cargo.reset()
        self.mission.passengers.reset()
        self.mission.illegal.reset()
        self.mission.is_stealth = False
        self.mission.is_invisible = False
        self.mission.priority_level = None
        self.mission.where_shown = None
        self.mission.repeat.reset()
        self.mission.clearance.reset()
        self.mission.is_infiltrating = False
        self.mission.waypoint = None
        self.mission.stopover.reset()
        self.mission.source.reset()
        self.mission.destination.reset()
    #end _reset_mission_to_default
#end class MissionCompiler
