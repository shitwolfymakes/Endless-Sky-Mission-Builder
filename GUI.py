''' GUI.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

This handles the GUI for ESMB

'''
import tkinter.font as tkfont

from menuactions import *
from guiutils import *
from ScrollingCenterFrame import ScrollingCenterFrame
from AggregatedTriggerFrame import AggregatedTriggerFrame

class GUI(object):

    def __init__(self, debugMode):
        print("Building GUI...")
        self.debugging = debugMode

        self.missionList = []
        self.missionNameToObjectDict = {}
        self.missionNames = []

        if self.debugging:
            self.missionList             = [Mission("Debugging", default=True)]
            self.missionNameToObjectDict = {self.missionList[0].missionName : self.missionList[0]}
            self.missionNames.append(self.missionList[0].missionName)
        #end if

        # Build the application window
        self.gui = ThemedTk(theme="arc")
        self.gui.title("ESMissionBuilder")
        self.gui.configure(bg="orange")

        self.disabledEntryStyle = ttk.Style()
        self.disabledEntryStyle.configure('D.TEntry', background='#D3D3D3')
        self.disabledComboboxStyle = ttk.Style()
        self.disabledComboboxStyle.configure('D.TCombobox', background='#D3D3D3')

        self.ofWidth = None
        self.cfWidth = None
        self.mfWidth = None

        # Declare the frames
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

        # Build the different parts of the main window
        #self.buildMenu(self.gui)
        self.buildMainView(self.gui)

        self.activeMission = None
        if self.debugging:
            self.activeMission = self.missionList[0]
        # Run the program
        self.gui.mainloop()
    #end init

    # This may be used later, after shortcuts are introduced
    '''
    def buildMenu(self, window):
        #TODO: IMPLEMENT THIS
        # creating a menu instance
        menu = Menu()
        window.config(menu=menu)

        # create the file object
        file = Menu(menu)
        edit = Menu(menu)

        # adds a command to the menu option, names it, and set the command to run
        file.add_command(label="New", command=lambda: newFile(self))
        file.add_command(label="Open", command=lambda: openFile(self))
        file.add_command(label="Save", command=lambda: saveFile(self))
        file.add_command(label="Exit", command=exit)

        # added "File" to our menu
        menu.add_cascade(label="File", menu=file)

        # adds a command to the menu option, names it, and set the command to run
        edit.add_command(label="Undo", command=lambda: undoAction(self))

        # added "Edit" to our menu
        menu.add_cascade(label="Edit", menu=edit)
    #end buildMenu
    '''

    def buildMainView(self, window):
        optionFrame  = ttk.Frame(window)
        centerFrame  = ScrollingCenterFrame(self, window)
        missionFrame = ttk.Frame(window)

        self.optionFrame  = optionFrame
        self.centerFrame  = centerFrame
        self.missionFrame = missionFrame

        # set up each of the frames
        self.buildOptionFrame()
        self.buildCenterFrame()
        self.buildMissionFrame()
    #end buildMainView


    ### BUILDING FRAMES ###


    def buildOptionFrame(self):
        print("Building optionFrame...", end="\t\t")
        self.optionFrame.grid(row=0, column=0, sticky="ns")

        ofTitle = ttk.Label(self.optionFrame, text="Mission")
        ofTitle.pack()

        # declare the combobox here, fill with missionNames
        self.missionComboBox = ttk.Combobox(self.optionFrame, state="readonly", values=self.missionNames)
        self.missionComboBox.bind("<<ComboboxSelected>>", self.missionSelected)
        self.missionComboBox.pack()

        if self.debugging:
            self.missionComboBox.current(0)

        # add function buttons
        newMissionButton = ttk.Button(self.optionFrame, text="New Mission", command=lambda: newMission(self))
        newMissionButton.pack(fill='x')

        saveMissionFileButton = ttk.Button(self.optionFrame, text="Save Mission File", command=lambda: saveFile(self))
        saveMissionFileButton.pack(fill='x')

        openMissionFileButton = ttk.Button(self.optionFrame, text="Open Mission File", command=lambda: openFile(self))
        openMissionFileButton.pack(fill='x')

        compileMissionFileButton = ttk.Button(self.optionFrame, text="Compile Mission", command=lambda: compileMission(self))
        compileMissionFileButton.pack(fill='x')

        helpButton = ttk.Button(self.optionFrame, text="Help", command=helpUser)
        helpButton.pack(fill='x')

        #TODO: Add functions to change missionName and delete mission. Also, update button grouping to reflect

        print("Done.")
    #end buildOptionFrame


    def buildCenterFrame(self):
        print("Building centerFrame...", end="\t\t")

        self.centerFrame.grid(row=0, column=1, sticky="ns")
        self.buildComponentsOnCenterFrame()

        print("Done.")
    #end buildCenterFrame


    def buildComponentsOnCenterFrame(self):
        print()
        print("\tRunning buildComponentsOnCenterFrame...", end="\t\t")

        cf = self.centerFrame.inner

        # Display name
        self.displayNameComponent = buildComponentFrame(cf, "Mission Display Name", 1, 0, ["<text>"])
        self.displayNameComponent.grid(row=0, column=0, sticky="ew")

        # Description
        self.descriptionComponent = buildComponentFrame(cf, "Description", 1, 0, ["<description>"])
        self.descriptionComponent.grid(row=1, column=0, sticky="ew")

        # isBlocked
        self.blockedComponent = buildComponentFrame(cf, "Blocked", 1, 0, ["<message>"])
        self.blockedComponent.grid(row=2, column=0, sticky="ew")

        # Deadline
        self.deadlineComponent = buildComponentFrame(cf, "Deadline", 0, 2, ["[<days#>]", "[<multiplier#>]"])
        self.deadlineComponent.grid(row=3, column=0, sticky="ew")

        # Cargo
        self.cargoComponent = buildComponentFrame(cf, "Cargo", 2, 2, ["(random | <name>)", "<number#>", "[<number#>]", "[<probability#>]"])
        self.cargoComponent.grid(row=4, column=0, sticky="ew")

        # Passengers
        self.passengersComponent = buildComponentFrame(cf, "Passengers", 1, 2, ["<number#>", "[<number#>]", "[<probability#>]"])
        self.passengersComponent.grid(row=5, column=0, sticky="ew")

        # Illegal
        self.illegalComponent = buildComponentFrame(cf, "Illegal", 1, 1, ["<fine#>", "[<message>]"])
        self.illegalComponent.grid(row=6, column=0, sticky="ew")

        # Stealth
        self.stealthComponent = buildComponentFrame(cf, "Stealth", 0, 0, [])
        self.stealthComponent.grid(row=7, column=0, sticky="ew")

        # Invisible
        self.invisibleComponent = buildComponentFrame(cf, "Invisible", 0, 0, [])
        self.invisibleComponent.grid(row=8, column=0, sticky="ew")

        # priorityLevel
        self.priorityLevelComponent = buildComboComponentFrame(cf, "Priority Level", ["Priority", "Minor"])
        self.priorityLevelComponent.grid(row=9, column=0, sticky="ew")

        # whereShown
        self.whereShownComponent = buildComboComponentFrame(cf, "Where Shown", ["Job", "Landing", "Assisting", "Boarding"])
        self.whereShownComponent.grid(row=10, column=0, sticky="ew")

        # Repeat
        self.repeatComponent = buildComponentFrame(cf, "Repeat", 0, 1, ["[<times#>]"])
        self.repeatComponent.grid(row=11, column=0, sticky="ew")

        # Clearance
        self.clearanceComponent = buildComponentFrame(cf, "Clearance", 0, 1, ["[<message>]"])
        self.clearanceComponent.grid(row=12, column=0, sticky="ew")

        # Infiltrating
        self.infiltratingComponent = buildComponentFrame(cf, "Infiltrating", 0, 0, [])
        self.infiltratingComponent.grid(row=13, column=0, sticky="ew")

        # Waypoint
        self.waypointComponent = buildComponentFrame(cf, "Waypoint", 1, 0, ["[<system>]"])
        self.waypointComponent.grid(row=14, column=0, sticky="ew")

        # Stopover
        self.stopoverComponent = buildComponentFrame(cf, "Stopover", 1, 0, ["[<planet>]"])
        self.stopoverComponent.grid(row=15, column=0, sticky="ew")

        # Source
        self.sourceComponent = buildComponentFrame(cf, "Source", 1, 0, ["[<planet>]"])
        self.sourceComponent.grid(row=16, column=0, sticky="ew")

        # Destination
        self.destinationComponent = buildComponentFrame(cf, "Destination", 1, 0, ["[<planet>]"])
        self.destinationComponent.grid(row=17, column=0, sticky="ew")


        # triggers
        self.triggersFrame = AggregatedTriggerFrame(self, cf)
        self.triggersFrame.grid(row=18, column=0, sticky="ew")


        print("Done.")
    #end buildComponentsOnCenterFrame


    def buildMissionFrame(self):
        print("Building missionFrame...", end="\t")

        #Display a default mission template on launch
        self.missionFrame.grid(row=0, column=2, sticky="nsew")
        mfTitle = ttk.Label(self.missionFrame, text="Mission Text")
        mfTitle.pack()

        # Populate the Text with a mission template
        self.missionTextBox = Text(self.missionFrame, wrap=WORD, height=50, width=100)
        self.missionTextBox.pack(expand=1, fill='both')
        welcome_message = "\n"
        welcome_message += "\t\t\tWelcome to Endless Sky Mission Builder!\n"
        welcome_message += "\n\t - Click \"New Mission\" to get started\n"
        welcome_message += "\n\t - Click \"Save Mission File\" to save all the missions to a text file\n"
        welcome_message += "\n\t - Click \"Open Mission File\" to open a mission file for editing\n"
        welcome_message += "\n\t - Click \"Compile Mission\" to save save the current mission\n"
        welcome_message += "\n\t - Click \"Help\" to be directed to the Mission Creation wiki\n"
        self.missionTextBox.insert(END, welcome_message)

        print("Done.")
    #end buildMissionFrame


    ### UPDATING FRAMES ###


    def updateOptionFrame(self):
        print("\nUpdating optionFrame...")

        ### Start updating combobox
        ml = self.missionList
        self.missionNames = []
        print("\tNew mission options:", end=" ")
        for m in ml:
            self.missionNames.append(m.missionName)
        print(self.missionNames)

        # update options in the combobox
        self.missionComboBox['values'] = self.missionNames
        self.missionComboBox.current(0)
        ### Finish updating combobox

        # update the other two frames to reflect the current mission
        self.updateCenterFrame()
        self.updateMissionFrame()

        print("Done.")
    #end updateOptionFrame


    def updateCenterFrame(self):
        print("\nUpdating centerFrame...")

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
        if components.deadline.isDeadline is True:
            self.deadlineComponent.set(0, None, "isDeadlineCheckbutton")
            if components.deadline.deadline[0] is not None:
                self.deadlineComponent.set(1, 0, components.deadline.deadline[0])
                if components.deadline.deadline[1] is not None:
                    self.deadlineComponent.set(2, 1, components.deadline.deadline[1])
            #end if
        #end if

        # cargo
        self.cargoComponent.reset()
        if components.cargo.isCargo is True:
            self.cargoComponent.set(0, 0, components.cargo.cargo[0])
            self.cargoComponent.set(0, 1, components.cargo.cargo[1])
            if components.cargo.cargo[2] is not None:
                self.cargoComponent.set(1, 2, components.cargo.cargo[2])
                if components.cargo.cargo[2] is not None:
                    self.cargoComponent.set(2, 3, components.cargo.cargo[3])
            #end if
        #end if

        # passengers
        if components.passengers.isPassengers is True:
            self.passengersComponent.set(0, 0, components.passengers.passengers[0])
            if components.passengers.passengers[1] is not None:
                self.passengersComponent.set(1, 1, components.passengers.passengers[1])
                if components.passengers.passengers[2] is not None:
                    self.passengersComponent.set(2, 2, components.passengers.passengers[2])
            #end if
        #end if

        # illegal
        if components.illegal.isIllegal is True:
            self.illegalComponent.set(0, 0, components.illegal.illegal[0])
            if components.illegal.illegal[1] is not None:
                self.illegalComponent.set(1, 1, components.illegal.illegal[1])
            # end if
        # end if

        # stealth
        if components.isStealth is True:
            self.stealthComponent.set(0, None, "stealthCheckbutton")

        # invisible
        if components.isInvisible is True:
            self.invisibleComponent.set(0, None, "isInvisibleCheckbutton")

        # priorityLevel
        if components.priorityLevel is not None:
            self.priorityLevelComponent.set(components.priorityLevel)

        # whereShown
        if components.whereShown is not None:
            self.whereShownComponent.set(components.whereShown)

        # repeat
        if components.isRepeat is True:
            self.repeatComponent.set(0, None, "isRepeatCheckbutton")
            if components.repeat is not None:
                self.repeatComponent.set(1, 0, components.repeat)
        #end if

        # clearance
        if components.clearance.isClearance is True:
            self.clearanceComponent.set(0, None, "isClearanceCheckbutton")
            if components.clearance.clearance is not None:
                self.clearanceComponent.set(1, 0, components.clearance.clearance)
        #end if

        # infiltrating
        if components.isInfiltrating is True:
            self.infiltratingComponent.set(0, None, "isInfiltratingCheckbutton")

        # waypoint
        if components.waypoint is not None:
            self.waypointComponent.set(0, 0, components.waypoint)


        # stopover
        if components.stopover.isStopover is True:
            self.stopoverComponent.set(0, 0, components.stopover.stopover)

        # source
        if components.source.isSource is True:
            self.sourceComponent.set(0, 0, components.source.source)

        # destination
        if components.destination.isDestination is True:
            self.destinationComponent.set(0, 0, components.destination.destination)

        # Triggers
        if components.triggerList:
            print("\tTriggers found")
            for trigger in components.triggerList:
                self.triggersFrame.populateTrigger(trigger)

    print("Done.")
    #end updateCenterFrame


    def updateMissionFrame(self):
        print("\nUpdating missionFrame...", end="\t")

        self.missionTextBox.forget()
        self.updateMissionTextBox()

        print("Done.")
    #end updateMissionFrame


    def updateMissionTextBox(self):
        self.missionTextBox = Text(self.missionFrame, height=50, width=100, wrap=WORD)
        self.missionTextBox.pack()
        self.missionTextBox.insert(END, self.activeMission.printMissionLinesToText())
    #end updateTextCanvas


    ### MISC METHODS ###

    def missionSelected(self, event):
        selectedMissionName = self.missionComboBox.get()
        print('\nOpening mission "%s"' % selectedMissionName)
        self.activeMission = self.missionNameToObjectDict.get(selectedMissionName)
        self.updateCenterFrame()
        self.updateMissionFrame()
    #end missionSelected

#end class GUI