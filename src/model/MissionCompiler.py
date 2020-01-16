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
    #TODO: WRITE UNIT TEST FOR THIS
    """This class compiles the data the user has entered into the current Mission object"""

    def __init__(self):
        self.editor = config.gui.center_pane
        self.active_item = config.active_item
        self.mission = self.active_item.components
    #end init


    def run(self):
        """
        Zero the Mission data, then store what data is selected based on the value of the corresponding entry state
        """
        logging.debug("\tCompiling mission...")
        self._reset_mission_to_default()

        # mission display name
        if self._has_mission_display_name():
            self._compile_mission_display_name()

        # description
        if self._has_description():
            self._compile_description()

        # isBlocked
        if self._has_blocked():
            self._compile_blocked()

        # deadline
        if self._has_deadline():
            self._compile_deadline()

        # cargo
        if self._has_cargo():
            self._compile_cargo()

        # passengers
        if self._has_passengers():
            self._compile_passengers()

        # illegal
        if self._has_illegal():
            self._compile_illegal()

        # stealth
        if self._has_stealth():
            self._compile_stealth()

        # isInvisible
        if self._has_invisible():
            self._compile_invisible()

        # priorityLevel
        if self._has_priority_level():
            self._compile_priority_level()

        # whereShown
        if self._has_where_shown():
            self._compile_where_shown()

        # repeat
        if self._has_repeat():
            self._compile_repeat()

        # clearance
        #TODO: fully implement this when filters are implemented
        if self._has_clearance():
            self._compile_clearance()

        # infiltrating
        if self._has_infiltrating():
            self._compile_infiltrating()

        # waypoint
        if self._has_waypoint():
            self._compile_waypoint()

        # stopover
        #TODO: fully implement this when filters are implemented
        if self._has_stopover():
            self._compile_stopover()

        # source
        #TODO: fully implement this when filters are implemented
        if self._has_source():
            self._compile_source()

        # destination
        # TODO: fully implement this when filters are implemented
        if self._has_destination():
            self._compile_destination()

        # Trigger data is compiled when TriggerWindow is closed

        #TODO: handle npcs

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


    ### methods to check if components are active
    def _has_mission_display_name(self):
        return self.editor.display_name_component.list_entry_states[0].get()
    #def _has_mission_display_name


    def _has_description(self):
        return self.editor.description_component.list_entry_states[0].get()
    #end _has_description


    def _has_blocked(self):
        return self.editor.blocked_component.list_entry_states[0].get()
    #end _has_blocked


    def _has_deadline(self):
        return self.editor.deadline_component.list_entry_states[0].get()
    #def _has_deadline


    def _has_cargo(self):
        return self.editor.cargo_component.list_entry_states[0].get()
    #end _has_cargo


    def _has_passengers(self):
        return self.editor.passengers_component.list_entry_states[0].get()
    #end _has_passengers


    def _has_illegal(self):
        return self.editor.illegal_component.list_entry_states[0].get()
    #end _has_illegal


    def _has_stealth(self):
        return self.editor.stealth_component.list_entry_states[0].get()
    #end _has_stealth


    def _has_invisible(self):
        return self.editor.invisible_component.list_entry_states[0].get()
    #end _hes_invisible


    def _has_priority_level(self):
        return self.editor.priority_level_component.is_active.get()
    #end _has_priority_level


    def _has_where_shown(self):
        return self.editor.where_shown_component.is_active.get()
    #end _has_where_shown


    def _has_repeat(self):
        return self.editor.repeat_component.list_entry_states[0].get()
    #end _has_repeat


    def _has_clearance(self):
        return self.editor.clearance_component.list_entry_states[0].get()
    #end _has_clearance


    def _has_infiltrating(self):
        return self.editor.infiltrating_component.list_entry_states[0].get()
    #end _has_infiltrating


    def _has_waypoint(self):
        return self.editor.waypoint_component.list_entry_states[0].get()
    #end _has_waypoint


    def _has_stopover(self):
        return self.editor.stopover_component.list_entry_states[0].get()
    #end _has_stopover


    def _has_source(self):
        return self.editor.source_component.list_entry_states[0].get()
    #end _has_source


    def _has_destination(self):
        return self.editor.destination_component.list_entry_states[0].get()
    #end _has_destination


    ### methods to compile the data from each component in the model
    def _compile_mission_display_name(self):
        logging.debug("\t\tFound display name: %s" % self.editor.display_name_component.list_entry_data[0].get())
        self.mission.mission_display_name = self.editor.display_name_component.list_entry_data[0].get()
    # end _compile_mission_display_name


    def _compile_description(self):
        logging.debug("\t\tFound description: %s" % self.editor.description_component.list_entry_data[0].get())
        self.mission.description = self.editor.description_component.list_entry_data[0].get()
    # end _compile_description


    def _compile_blocked(self):
        logging.debug("\t\tFound block: %s" % self.editor.blocked_component.list_entry_data[0].get())
        self.mission.blocked = self.editor.blocked_component.list_entry_data[0].get()
    # end _compile_blocked


    def _compile_deadline(self):
        logging.debug("\t\tFound deadline")
        self.mission.deadline.is_active = True
        if self.editor.deadline_component.list_entry_states[1].get():
            logging.debug("\t\t\tFound deadline days: %s" % self.editor.deadline_component.list_entry_data[0].get())
            self.mission.deadline.deadline[0] = self.editor.deadline_component.list_entry_data[0].get()
            if self.editor.deadline_component.list_entry_states[2].get():
                logging.debug(
                    "\t\t\tFound deadline message: %s" % self.editor.deadline_component.list_entry_data[1].get())
                self.mission.deadline.deadline[1] = self.editor.deadline_component.list_entry_data[1].get()
            # end if
        # end if
    # end _compile_deadline


    def _compile_cargo(self):
        logging.debug("\t\tFound cargo:")
        logging.debug("\t\t\t%s" % self.editor.cargo_component.list_entry_data[0].get())
        logging.debug("\t\t\t%s" % self.editor.cargo_component.list_entry_data[1].get())
        self.mission.cargo.is_active = True
        self.mission.cargo.cargo[0] = self.editor.cargo_component.list_entry_data[0].get()
        self.mission.cargo.cargo[1] = self.editor.cargo_component.list_entry_data[1].get()
        if self.editor.cargo_component.list_entry_states[1].get():
            logging.debug("\t\t\tFound cargo optional modifiers:")
            logging.debug("\t\t\t\t%s" % self.editor.cargo_component.list_entry_data[2].get())
            self.mission.cargo.cargo[2] = self.editor.cargo_component.list_entry_data[2].get()
            if self.editor.cargo_component.list_entry_states[2].get():
                logging.debug("\t\t\t\t%s" % self.editor.cargo_component.list_entry_data[3].get())
                self.mission.cargo.cargo[3] = self.editor.cargo_component.list_entry_data[3].get()
            # end if
        # end if
    # end _compile_cargo


    def _compile_passengers(self):
        logging.debug("\t\tFound passengers: %s" % self.editor.passengers_component.list_entry_data[0].get())
        self.mission.passengers.is_active = True
        self.mission.passengers.passengers[0] = self.editor.passengers_component.list_entry_data[0].get()
        if self.editor.passengers_component.list_entry_states[1].get():
            logging.debug("\t\t\tFound passengers optional data:")
            logging.debug("\t\t\t\t%s" % self.editor.passengers_component.list_entry_data[1].get())
            self.mission.passengers.passengers[1] = self.editor.passengers_component.list_entry_data[1].get()
            if self.editor.passengers_component.list_entry_states[2].get():
                logging.debug("\t\t\t\t%s" % self.editor.passengers_component.list_entry_data[2].get())
                self.mission.passengers.passengers[2] = self.editor.passengers_component.list_entry_data[2].get()
            # end if
        # end if
    # end _compile_passengers


    def _compile_illegal(self):
        logging.debug("\t\tFound illegal: %s" % self.editor.illegal_component.list_entry_data[0].get())
        self.mission.illegal.is_active = True
        self.mission.illegal.illegal[0] = self.editor.illegal_component.list_entry_data[0].get()
        if self.editor.illegal_component.list_entry_states[1].get():
            logging.debug(
                "\t\t\tFound illegal optional modifier: %s" % self.editor.illegal_component.list_entry_data[1].get())
            self.mission.illegal.illegal[1] = self.editor.illegal_component.list_entry_data[1].get()
        # end if
    # end _compile_illegal


    def _compile_stealth(self):
        logging.debug("\t\tFound stealth modifier")
        self.mission.is_stealth = True
    # end _compile_stealth


    def _compile_invisible(self):
        logging.debug("\t\tFound mission invisible modifier")
        self.mission.is_invisible = True
    # end _compile_invisible


    def _compile_priority_level(self):
        logging.debug("\t\tFound priority level: %s" % self.editor.priority_level_component.combo.get().lower())
        self.mission.priority_level = self.editor.priority_level_component.combo.get().lower()
    # end _compile_priority_level


    def _compile_where_shown(self):
        logging.debug("\t\tFound where shown: %s" % self.editor.where_shown_component.combo.get().lower())
        self.mission.where_shown = self.editor.where_shown_component.combo.get().lower()
    # end _compile_where_shown


    def _compile_repeat(self):
        logging.debug("\t\tFound repeat")
        self.mission.repeat.is_active = True
        if self.editor.repeat_component.list_entry_states[1].get():
            logging.debug("\t\t\tFound repeat optionals modifier: %s" % self.editor.repeat_component.list_entry_data[0].get())
            self.mission.repeat.repeat = self.editor.repeat_component.list_entry_data[0].get()
        # end if
    # end _compile_repeat


    def _compile_clearance(self):
        logging.debug("\t\tFound clearance: %s" % self.editor.clearance_component.list_entry_data[0].get())
        self.mission.clearance.is_active = True
        self.mission.clearance.clearance = self.editor.clearance_component.list_entry_data[0].get()
    # end _compile_clearance


    def _compile_infiltrating(self):
        logging.debug("\t\tFound infiltrating")
        self.mission.is_infiltrating = True
    # end _compile_infiltrating


    def _compile_waypoint(self):
        logging.debug("\t\tFound waypoint: %s" % self.editor.waypoint_component.list_entry_data[0].get())
        self.mission.waypoint = self.editor.waypoint_component.list_entry_data[0].get()
    # end _compile_waypoint


    def _compile_stopover(self):
        logging.debug("\t\tFound stopover: %s" % self.editor.stopover_component.list_entry_data[0].get())
        self.mission.stopover.is_active = True
        self.mission.stopover.stopover = self.editor.stopover_component.list_entry_data[0].get()
    # end _compile_stopover


    def _compile_source(self):
        logging.debug("\t\tFound source: %s" % self.editor.source_component.list_entry_data[0].get())
        self.mission.source.is_active = True
        self.mission.source.source = self.editor.source_component.list_entry_data[0].get()
    # end _compile_source


    def _compile_destination(self):
        logging.debug("\t\tFound source: %s" % self.editor.destination_component.list_entry_data[0].get())
        self.mission.destination.is_active = True
        self.mission.destination.destination = self.editor.destination_component.list_entry_data[0].get()
    # end _compile_destination
#end class MissionCompiler
