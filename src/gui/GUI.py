""" GUI.py
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
from ttkthemes import ThemedTk

from src.gui.editor import OptionPane, ItemTextPane, MissionEditorPane
from src.model import Mission
import src.config as config
import src.widgets as widgets


class GUI:
    """This handles the GUI for ESMB"""

    def __init__(self):
        logging.debug("\tBuilding GUI...")

        #TODO: Look into changing this to not need the dictionary
        #TODO: Make missionList an instance variable of ESMB
        self.missionList = []
        self.missionNameToObjectDict = {}
        self.missionNames = []

        if config.debugging:
            config.mission_file_items.add_item(Mission("Debugging"))
        #end if

        # Build the application window
        self.gui = ThemedTk(theme="plastik")
        self.gui.title("ESMissionBuilder")
        self.gui.configure(bg="orange")

        # enable window resizing
        self.gui.columnconfigure(0, weight=1)
        self.gui.rowconfigure(0, weight=1)

        self.disabledEntryStyle = ttk.Style()
        self.disabledEntryStyle.configure('D.TEntry', background='#D3D3D3')
        self.disabledComboboxStyle = ttk.Style()
        self.disabledComboboxStyle.configure('D.TCombobox', background='#D3D3D3')

        self.ofWidth = None
        self.cfWidth = None
        self.mfWidth = None

        # Declare the frames
        # TODO: move each frame into their own custom class - 1/3 Completed
        self.optionFrame  = None
        self.centerFrame  = None
        self.missionFrame = None

        # declare optionFrame components
        self.missionComboBox = None
        self.activeMission   = None

        # declare centerFrame components
        self.displayNameComponent   = None
        self.descriptionComponent   = None
        self.blockedComponent       = None
        self.deadlineComponent      = None
        self.cargoComponent         = None
        self.passengersComponent    = None
        self.illegalComponent       = None
        self.stealthComponent       = None
        self.invisibleComponent     = None
        self.priorityLevelComponent = None
        self.whereShownComponent    = None
        self.repeatComponent        = None
        self.clearanceComponent     = None
        self.infiltratingComponent  = None
        self.waypointComponent      = None
        self.stopoverComponent      = None
        self.sourceComponent        = None
        self.destinationComponent   = None
        # Triggers
        self.triggersFrame = None
        self.activeTrigger = None

        # declare missionFrame components
        self.missionTextBox = None

        self.build_main_view(self.gui)

        self.activeMission = None
        #if config.debugging:
        #    self.activeMission = self.missionList[0]

        config.gui = self
        self.gui.mainloop()
    #end init


    def build_main_view(self, window):
        """
        Instantiate the three major frames, and call methods to build the respective GUI areas

        :param window: The ThemedTK object that the rest of the GUI is built off of
        """
        #TODO: convert each of these into encapsulated frames, with no code in GUI
        #option_frame  = ttk.Frame(window)
        #center_frame  = widgets.ScrollingFrame(self, window)
        #mission_frame = ttk.Frame(window)

        self.optionFrame = OptionPane(window)
        self.optionFrame.grid(row=0, column=0, sticky="ns")

        #self.centerFrame = center_frame
        self.centerFrame = MissionEditorPane(window)
        self.centerFrame.grid(row=0, column=1, sticky="ns")

        self.missionFrame = ItemTextPane(window)
        self.missionFrame.grid(row=0, column=2, sticky="nsew")

        # set up each of the frames
        #self.build_option_frame()
        #self.build_center_frame()
        #self.build_mission_frame()

        logging.debug("\tGUI built")
    #end build_main_view


    def build_center_frame(self):
        """Add widgets to the centerFrame"""
        logging.debug("\tBuilding centerFrame...")

        self.centerFrame.grid(row=0, column=1, sticky="ns")

        cf = self.centerFrame.inner

        # Display name
        self.displayNameComponent = widgets.ComponentMandOptFrame(cf, "Mission Display Name", 1, 0, ["<name>"], "display_name")
        self.displayNameComponent.grid(row=0, column=0, sticky="ew")

        # Description
        self.descriptionComponent = widgets.ComponentMandOptFrame(cf, "Description", 1, 0, ["<text>"], "description")
        self.descriptionComponent.grid(row=1, column=0, sticky="ew")

        # isBlocked
        self.blockedComponent = widgets.ComponentMandOptFrame(cf, "Blocked", 1, 0, ["<message>"], "is_blocked")
        self.blockedComponent.grid(row=2, column=0, sticky="ew")

        # Deadline
        self.deadlineComponent = widgets.ComponentMandOptFrame(cf, "Deadline", 0, 2, ["[<days#>]", "[<multiplier#>]"], "deadline")
        self.deadlineComponent.grid(row=3, column=0, sticky="ew")

        # Cargo
        self.cargoComponent = widgets.ComponentMandOptFrame(cf, "Cargo", 2, 2, ["(random | <name>)", "<number#>", "[<number#>]", "[<probability#>]"], "cargo")
        self.cargoComponent.grid(row=4, column=0, sticky="ew")

        # Passengers
        self.passengersComponent = widgets.ComponentMandOptFrame(cf, "Passengers", 1, 2, ["<number#>", "[<number#>]", "[<probability#>]"], "passengers")
        self.passengersComponent.grid(row=5, column=0, sticky="ew")

        # Illegal
        self.illegalComponent = widgets.ComponentMandOptFrame(cf, "Illegal", 1, 1, ["<fine#>", "[<message>]"], "illegal")
        self.illegalComponent.grid(row=6, column=0, sticky="ew")

        # Stealth
        self.stealthComponent = widgets.ComponentMandOptFrame(cf, "Stealth", 0, 0, [], "stealth")
        self.stealthComponent.grid(row=7, column=0, sticky="ew")

        # Invisible
        self.invisibleComponent = widgets.ComponentMandOptFrame(cf, "Invisible", 0, 0, [], "invisible")
        self.invisibleComponent.grid(row=8, column=0, sticky="ew")

        # priorityLevel
        self.priorityLevelComponent = widgets.ComboComponentFrame(cf, "Priority Level", ["Priority", "Minor"], "priority_level")
        self.priorityLevelComponent.grid(row=9, column=0, sticky="ew")

        # whereShown
        self.whereShownComponent = widgets.ComboComponentFrame(cf, "Where Shown", ["Job", "Landing", "Assisting", "Boarding"], "where_shown")
        self.whereShownComponent.grid(row=10, column=0, sticky="ew")

        # Repeat
        self.repeatComponent = widgets.ComponentMandOptFrame(cf, "Repeat", 0, 1, ["[<times#>]"], "repeat")
        self.repeatComponent.grid(row=11, column=0, sticky="ew")

        # Clearance
        self.clearanceComponent = widgets.ComponentMandOptFrame(cf, "Clearance", 0, 1, ["[<message>]"], "clearance")
        self.clearanceComponent.grid(row=12, column=0, sticky="ew")

        # Infiltrating
        self.infiltratingComponent = widgets.ComponentMandOptFrame(cf, "Infiltrating", 0, 0, [], "infiltrating")
        self.infiltratingComponent.grid(row=13, column=0, sticky="ew")

        # Waypoint
        self.waypointComponent = widgets.ComponentMandOptFrame(cf, "Waypoint", 1, 0, ["[<system>]"], "waypoint")
        self.waypointComponent.grid(row=14, column=0, sticky="ew")

        # Stopover
        self.stopoverComponent = widgets.ComponentMandOptFrame(cf, "Stopover", 1, 0, ["[<planet>]"], "stopover")
        self.stopoverComponent.grid(row=15, column=0, sticky="ew")

        # Source
        self.sourceComponent = widgets.ComponentMandOptFrame(cf, "Source", 1, 0, ["[<planet>]"], "source")
        self.sourceComponent.grid(row=16, column=0, sticky="ew")

        # Destination
        self.destinationComponent = widgets.ComponentMandOptFrame(cf, "Destination", 1, 0, ["[<planet>]"], "destination")
        self.destinationComponent.grid(row=17, column=0, sticky="ew")

        # triggers
        self.triggersFrame = widgets.AggregatedTriggerFrame(self, cf)
        self.triggersFrame.grid(row=18, column=0, sticky="ew")

        # add a blank label to pad the bottom of the frame
        bl1 = ttk.Label(cf, textvariable=" ")
        bl1.grid(row=19, column=0, sticky="ew")
    #end build_center_frame


    ### UPDATING FRAMES ###


    def update_center_frame(self):
        """Update missionFrame to use the most recent data"""
        logging.debug("Updating centerFrame...")

        components = self.activeMission.components

        # missionDisplayName
        self.displayNameComponent.reset()
        if components.missionDisplayName is not None:
            self.displayNameComponent.set(0, 0, components.missionDisplayName)

        # description
        self.descriptionComponent.reset()
        if components.description is not None:
            description = components.description
            self.descriptionComponent.set(0, 0, description)
        #end if

        # blocked
        self.blockedComponent.reset()
        if components.blocked is not None:
            self.blockedComponent.set(0, 0, components.blocked)

        # deadline
        self.deadlineComponent.reset()
        if components.deadline.isActive is True:
            self.deadlineComponent.set(0, None, "isDeadlineCheckbutton")
            if components.deadline.deadline[0] is not None:
                self.deadlineComponent.set(1, 0, components.deadline.deadline[0])
                if components.deadline.deadline[1] is not None:
                    self.deadlineComponent.set(2, 1, components.deadline.deadline[1])
            #end if
        #end if

        # cargo
        self.cargoComponent.reset()
        if components.cargo.isActive is True:
            self.cargoComponent.set(0, 0, components.cargo.cargo[0])
            self.cargoComponent.set(0, 1, components.cargo.cargo[1])
            if components.cargo.cargo[2] is not None:
                self.cargoComponent.set(1, 2, components.cargo.cargo[2])
                if components.cargo.cargo[2] is not None:
                    self.cargoComponent.set(2, 3, components.cargo.cargo[3])
            #end if
        #end if

        # passengers
        self.passengersComponent.reset()
        if components.passengers.isActive is True:
            self.passengersComponent.set(0, 0, components.passengers.passengers[0])
            if components.passengers.passengers[1] is not None:
                self.passengersComponent.set(1, 1, components.passengers.passengers[1])
                if components.passengers.passengers[2] is not None:
                    self.passengersComponent.set(2, 2, components.passengers.passengers[2])
            #end if
        #end if

        # illegal
        self.illegalComponent.reset()
        if components.illegal.isActive is True:
            self.illegalComponent.set(0, 0, components.illegal.illegal[0])
            if components.illegal.illegal[1] is not None:
                self.illegalComponent.set(1, 1, components.illegal.illegal[1])
            # end if
        # end if

        # stealth
        self.stealthComponent.reset()
        if components.isStealth is True:
            self.stealthComponent.set(0, None, "stealthCheckbutton")

        # invisible
        self.invisibleComponent.reset()
        if components.isInvisible is True:
            self.invisibleComponent.set(0, None, "isInvisibleCheckbutton")

        # priorityLevel
        self.priorityLevelComponent.reset()
        if components.priorityLevel is not None:
            self.priorityLevelComponent.set(components.priorityLevel)

        # whereShown
        self.whereShownComponent.reset()
        if components.whereShown is not None:
            self.whereShownComponent.set(components.whereShown)

        # repeat
        self.repeatComponent.reset()
        if components.repeat.isActive is True:
            self.repeatComponent.set(0, None, "isRepeatCheckbutton")
            if components.repeat.repeat is not None:
                self.repeatComponent.set(1, 0, components.repeat.repeat)
        #end if

        # clearance
        self.clearanceComponent.reset()
        if components.clearance.isActive is True:
            self.clearanceComponent.set(0, None, "isClearanceCheckbutton")
            if components.clearance.clearance is not None:
                self.clearanceComponent.set(1, 0, components.clearance.clearance)
        #end if

        # infiltrating
        self.infiltratingComponent.reset()
        if components.isInfiltrating is True:
            self.infiltratingComponent.set(0, None, "isInfiltratingCheckbutton")

        # waypoint
        self.waypointComponent.reset()
        if components.waypoint is not None:
            self.waypointComponent.set(0, 0, components.waypoint)


        # stopover
        self.stopoverComponent.reset()
        if components.stopover.isActive is True:
            self.stopoverComponent.set(0, 0, components.stopover.stopover)

        # source
        self.sourceComponent.reset()
        if components.source.isActive is True:
            self.sourceComponent.set(0, 0, components.source.source)

        # destination
        self.destinationComponent.reset()
        if components.destination.isActive is True:
            self.destinationComponent.set(0, 0, components.destination.destination)

        # Clear out the AggregatedTriggerFrame
        self.triggersFrame.grid_forget()
        self.triggersFrame = widgets.AggregatedTriggerFrame(self, self.centerFrame.inner)
        self.triggersFrame.grid(row=18, column=0, sticky="ew")

        # Triggers
        if components.triggerList:
            logging.debug("\tTriggers found")
            for trigger in components.triggerList:
                self.triggersFrame.populate_trigger(trigger)
    #end update_center_frame
#end class GUI
