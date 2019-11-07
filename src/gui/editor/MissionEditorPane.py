""" MissionEditorPane.py
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
from tkinter import ttk

import src.config as config
import src.widgets as widgets
from src.gui.editor import GUIPane


class MissionEditorPane(widgets.ScrollingFrame, GUIPane):
    def __init__(self, parent):
        widgets.ScrollingFrame.__init__(self, parent, "Mission Options")
        logging.debug("\tInitializing MissionEditorPane...")

        self.mission_editor_frame = self.inner

        # declare MissionEditorPane components
        self.display_name_component = None
        self.description_component = None
        self.blocked_component = None
        self.deadline_component = None
        self.cargo_component = None
        self.passengers_component = None
        self.illegal_component = None
        self.stealth_component = None
        self.invisible_component = None
        self.priority_level_component = None
        self.where_shown_component = None
        self.repeat_component = None
        self.clearance_component = None
        self.infiltrating_component = None
        self.waypoint_component = None
        self.stopover_component = None
        self.source_component = None
        self.destination_component = None

        # Triggers
        self.triggers_frame = None
        self.active_trigger = None

        self._build_pane()
    #end init


    def _build_pane(self):
        me = self.mission_editor_frame

        # Display name
        self.display_name_component = widgets.ComponentMandOptFrame(me, "Mission Display Name", 1, 0, ["<name>"], "display_name")
        self.display_name_component.grid(row=0, column=0, sticky="ew")

        # Description
        self.description_component = widgets.ComponentMandOptFrame(me, "Description", 1, 0, ["<text>"], "description")
        self.description_component.grid(row=1, column=0, sticky="ew")

        # isBlocked
        self.blocked_component = widgets.ComponentMandOptFrame(me, "Blocked", 1, 0, ["<message>"], "is_blocked")
        self.blocked_component.grid(row=2, column=0, sticky="ew")

        # Deadline
        self.deadline_component = widgets.ComponentMandOptFrame(me, "Deadline", 0, 2, ["[<days#>]", "[<multiplier#>]"], "deadline")
        self.deadline_component.grid(row=3, column=0, sticky="ew")

        # Cargo
        self.cargo_component = widgets.ComponentMandOptFrame(me, "Cargo", 2, 2, ["(random | <name>)", "<number#>", "[<number#>]", "[<probability#>]"], "cargo")
        self.cargo_component.grid(row=4, column=0, sticky="ew")

        # Passengers
        self.passengers_component = widgets.ComponentMandOptFrame(me, "Passengers", 1, 2, ["<number#>", "[<number#>]", "[<probability#>]"], "passengers")
        self.passengers_component.grid(row=5, column=0, sticky="ew")

        # Illegal
        self.illegal_component = widgets.ComponentMandOptFrame(me, "Illegal", 1, 1, ["<fine#>", "[<message>]"], "illegal")
        self.illegal_component.grid(row=6, column=0, sticky="ew")

        # Stealth
        self.stealth_component = widgets.ComponentMandOptFrame(me, "Stealth", 0, 0, [], "stealth")
        self.stealth_component.grid(row=7, column=0, sticky="ew")

        # Invisible
        self.invisible_component = widgets.ComponentMandOptFrame(me, "Invisible", 0, 0, [], "invisible")
        self.invisible_component.grid(row=8, column=0, sticky="ew")

        # priorityLevel
        self.priority_level_component = widgets.ComboComponentFrame(me, "Priority Level", ["Priority", "Minor"], "priority_level")
        self.priority_level_component.grid(row=9, column=0, sticky="ew")

        # whereShown
        self.where_shown_component = widgets.ComboComponentFrame(me, "Where Shown", ["Job", "Landing", "Assisting", "Boarding"], "where_shown")
        self.where_shown_component.grid(row=10, column=0, sticky="ew")

        # Repeat
        self.repeat_component = widgets.ComponentMandOptFrame(me, "Repeat", 0, 1, ["[<times#>]"], "repeat")
        self.repeat_component.grid(row=11, column=0, sticky="ew")

        # Clearance
        self.clearance_component = widgets.ComponentMandOptFrame(me, "Clearance", 0, 1, ["[<message>]"], "clearance")
        self.clearance_component.grid(row=12, column=0, sticky="ew")

        # Infiltrating
        self.infiltrating_component = widgets.ComponentMandOptFrame(me, "Infiltrating", 0, 0, [], "infiltrating")
        self.infiltrating_component.grid(row=13, column=0, sticky="ew")

        # Waypoint
        self.waypoint_component = widgets.ComponentMandOptFrame(me, "Waypoint", 1, 0, ["[<system>]"], "waypoint")
        self.waypoint_component.grid(row=14, column=0, sticky="ew")

        # Stopover
        self.stopover_component = widgets.ComponentMandOptFrame(me, "Stopover", 1, 0, ["[<planet>]"], "stopover")
        self.stopover_component.grid(row=15, column=0, sticky="ew")

        # Source
        self.source_component = widgets.ComponentMandOptFrame(me, "Source", 1, 0, ["[<planet>]"], "source")
        self.source_component.grid(row=16, column=0, sticky="ew")

        # Destination
        self.destination_component = widgets.ComponentMandOptFrame(me, "Destination", 1, 0, ["[<planet>]"], "destination")
        self.destination_component.grid(row=17, column=0, sticky="ew")

        # triggers
        self.triggers_frame = widgets.AggregatedTriggerFrame(me)
        self.triggers_frame.grid(row=18, column=0, sticky="ew")

        # add a blank label to pad the bottom of the frame
        bl1 = ttk.Label(me, textvariable=" ")
        bl1.grid(row=19, column=0, sticky="ew")
    #end _build_pane


    def update_pane(self):
        logging.debug("Updating center_pane...")

        components = config.active_item.components

        # update each component
        self._update_mission_display_name(components)
        self._update_description(components)
        self._update_blocked(components)
        self._update_deadline(components)
        self._update_cargo(components)
        self._update_passengers(components)
        self._update_illegal(components)
        self._update_stealth(components)
        self._update_invisible(components)
        self._update_priority_level(components)
        self._update_where_shown(components)
        self._update_repeat(components)
        self._update_clearance(components)
        self._update_infiltrating(components)
        self._update_waypoint(components)
        self._update_stopover(components)
        self._update_source(components)
        self._update_destination(components)
        self._update_triggers(components)
    #end update_pane


    def _update_mission_display_name(self, components):
        self.display_name_component.reset()
        if components.mission_display_name is not None:
            self.display_name_component.set(0, 0, components.mission_display_name)
    #end _update_mission_display_name


    def _update_description(self, components):
        self.description_component.reset()
        if components.description is not None:
            description = components.description
            self.description_component.set(0, 0, description)
        # end if
    #edn _update_description


    def _update_blocked(self, components):
        self.blocked_component.reset()
        if components.blocked is not None:
            self.blocked_component.set(0, 0, components.blocked)
    #end _update_blocked


    def _update_deadline(self, components):
        self.deadline_component.reset()
        if components.deadline.is_active is True:
            self.deadline_component.set(0, None, "isDeadlineCheckbutton")
            if components.deadline.deadline[0] is not None:
                self.deadline_component.set(1, 0, components.deadline.deadline[0])
                if components.deadline.deadline[1] is not None:
                    self.deadline_component.set(2, 1, components.deadline.deadline[1])
            # end if
        # end if
    #end _update_deadline


    def _update_cargo(self, components):
        self.cargo_component.reset()
        if components.cargo.is_active is True:
            self.cargo_component.set(0, 0, components.cargo.cargo[0])
            self.cargo_component.set(0, 1, components.cargo.cargo[1])
            if components.cargo.cargo[2] is not None:
                self.cargo_component.set(1, 2, components.cargo.cargo[2])
                if components.cargo.cargo[2] is not None:
                    self.cargo_component.set(2, 3, components.cargo.cargo[3])
            # end if
        # end if
    #end _update_cargo


    def _update_passengers(self, components):
        self.passengers_component.reset()
        if components.passengers.is_active is True:
            self.passengers_component.set(0, 0, components.passengers.passengers[0])
            if components.passengers.passengers[1] is not None:
                self.passengers_component.set(1, 1, components.passengers.passengers[1])
                if components.passengers.passengers[2] is not None:
                    self.passengers_component.set(2, 2, components.passengers.passengers[2])
            # end if
        # end if
    #end _update_passengers


    def _update_illegal(self, components):
        self.illegal_component.reset()
        if components.illegal.is_active is True:
            self.illegal_component.set(0, 0, components.illegal.illegal[0])
            if components.illegal.illegal[1] is not None:
                self.illegal_component.set(1, 1, components.illegal.illegal[1])
            # end if
        # end if
    #end _update_illegal


    def _update_stealth(self, components):
        self.stealth_component.reset()
        if components.is_stealth is True:
            self.stealth_component.set(0, None, "stealthCheckbutton")
    #end _update_stealth


    def _update_invisible(self, components):
        self.invisible_component.reset()
        if components.is_invisible is True:
            self.invisible_component.set(0, None, "isInvisibleCheckbutton")
    #end _update_invisible


    def _update_priority_level(self, components):
        self.priority_level_component.reset()
        if components.priority_level is not None:
            self.priority_level_component.set(components.priority_level)
    #end _update_priority_level


    def _update_where_shown(self, components):
        self.where_shown_component.reset()
        if components.where_shown is not None:
            self.where_shown_component.set(components.where_shown)
    #end _update_where_shown


    def _update_repeat(self, components):
        self.repeat_component.reset()
        if components.repeat.is_active is True:
            self.repeat_component.set(0, None, "isRepeatCheckbutton")
            if components.repeat.repeat is not None:
                self.repeat_component.set(1, 0, components.repeat.repeat)
        # end if
    #end _update_repeat


    def _update_clearance(self, components):
        self.clearance_component.reset()
        if components.clearance.is_active is True:
            self.clearance_component.set(0, None, "isClearanceCheckbutton")
            if components.clearance.clearance is not None:
                self.clearance_component.set(1, 0, components.clearance.clearance)
        # end if
    #end _update_clearance


    def _update_infiltrating(self, components):
        self.infiltrating_component.reset()
        if components.is_infiltrating is True:
            self.infiltrating_component.set(0, None, "isInfiltratingCheckbutton")
    #end _update_infiltrating


    def _update_waypoint(self, components):
        self.waypoint_component.reset()
        if components.waypoint is not None:
            self.waypoint_component.set(0, 0, components.waypoint)
    #end _update_waypoint


    def _update_stopover(self, components):
        self.stopover_component.reset()
        if components.stopover.is_active is True:
            self.stopover_component.set(0, 0, components.stopover.stopover)
    #end _update_stopover


    def _update_source(self, components):
        self.source_component.reset()
        if components.source.is_active is True:
            self.source_component.set(0, 0, components.source.source)
    #end _update_source


    def _update_destination(self, components):
        self.destination_component.reset()
        if components.destination.is_active is True:
            self.destination_component.set(0, 0, components.destination.destination)
    #end _update_destination


    def _update_triggers(self, components):
        # Clear out the AggregatedTriggerFrame
        self.triggers_frame.grid_forget()
        self.triggers_frame = widgets.AggregatedTriggerFrame(self.mission_editor_frame)
        self.triggers_frame.grid(row=18, column=0, sticky="ew")

        # Triggers
        if components.trigger_list:
            logging.debug("\tTriggers found")
            for trigger in components.trigger_list:
                self.triggers_frame.populate_trigger(trigger)
        #end if
    #end _update_triggers
#end class MissionEditorPane
