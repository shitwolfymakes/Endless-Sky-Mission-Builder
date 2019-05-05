''' GUI.py
Created by wolfy

This handles the GUI for ESMB

'''
from tkinter import *
from tkinter import ttk, StringVar
from menuactions import *
from ScrollingCenterFrame import ScrollingCenterFrame

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
        self.gui = Tk()
        self.gui.title("ESMissionBuilder")
        self.gui.configure(bg="orange")

        self.ofWidth = None
        self.cfWidth = None
        self.mfWidth = None

        # Declare the frames
        self.optionFrame  = None
        self.centerFrameWrapper = None
        self.centerFrame  = None
        self.missionFrame = None

        # declare optionFrame components
        self.missionComboBox = None
        self.activeMission   = None

        # declare centerFrame components

        ## displayName
        self.displayNameEntryState  = BooleanVar()
        self.displayNameCheckbutton = None
        self.displayName            = StringVar()
        self.displayNameEntry       = None


        ## description
        self.descriptionEntryState  = BooleanVar()
        self.descriptionCheckbutton = None
        self.description            = StringVar()
        self.descriptionEntry       = None


        ## isBlocked
        self.isBlockedEntryState         = BooleanVar()
        self.isBlockedCheckbutton        = None
        self.isBlockedMessage            = StringVar()
        self.isBlockedMessageEntry       = None


        ## deadline
        self.deadlineEntryState           = BooleanVar()
        self.deadlineOptionalsEntryState  = BooleanVar()
        self.deadlineCheckbutton          = None

        self.deadlineOptionals            = StringVar()
        self.deadlineOptionalsEntry       = None
        self.deadlineOptionalsCheckbutton = None


        ## cargo
        self.cargoEntryState            = BooleanVar()
        self.cargoOptionalsEntryState   = BooleanVar()
        self.cargoIllegalEntryState     = BooleanVar()
        self.cargoFineMessageEntryState = BooleanVar()
        self.cargoStealthEntryState     = BooleanVar()

        self.cargoCheckbutton          = None
        self.cargo                     = StringVar()
        self.cargoEntry                = None

        self.cargoOptionals            = StringVar()
        self.cargoOptionalsEntry       = None
        self.cargoOptionalsCheckbutton = None

        self.cargoFine               = StringVar()
        self.cargoFineEntry          = None
        self.cargoIllegalCheckbutton = None

        self.cargoFineMessage            = StringVar()
        self.cargoFineMessageEntry       = None
        self.cargoFineMessageCheckbutton = None

        self.cargoStealthCheckbutton = None


        ## Passengers
        self.passengersEntryState          = BooleanVar()
        self.passengersOptionalsEntryState = BooleanVar()

        self.passengers               = StringVar()
        self.passengersEntry          = None
        self.passengersCheckbutton    = None

        self.passengersOptionals            = StringVar()
        self.passengersOptionalsEntry       = None
        self.passengersOptionalsCheckbutton = None


        ## isInvisible
        self.isInvisibleEntryState  = BooleanVar()
        self.isInvisibleCheckbutton = None


        ## priorityLevel
        self.priorityLevelEntryState = BooleanVar()
        self.rbPriorityValue         = StringVar()

        self.priorityLevelCheckbutton = None
        self.rbPriority               = None
        self.rbMinor                  = None


        ## whereShown
        self.whereShownEntryState  = BooleanVar()
        self.rbWhereShownValue     = StringVar()
        self.whereShownCheckbutton = None

        self.rbJob       = None
        self.rbLanding   = None
        self.rbAssisting = None
        self.rbBoarding  = None


        ## repeat
        self.repeatEntryState          = BooleanVar()
        self.repeatOptionalsEntryState = BooleanVar()
        self.repeatCheckbutton         = None

        self.repeatOptionals            = StringVar()
        self.repeatOptionalsEntry       = None
        self.repeatOptionalsCheckbutton = None


        ## Clearance
        self.clearanceEntryState          = BooleanVar()
        self.clearanceOptionalsEntryState = BooleanVar()

        self.clearanceCheckbutton    = None
        self.clearanceOptionals      = StringVar()
        self.clearanceOptionalsEntry = None


        ## isInfiltrating
        self.isInfiltratingEntryState  = BooleanVar()
        self.isInfiltratingCheckbutton = None


        ## waypoint
        self.waypointEntryState = BooleanVar()
        self.waypoint           = StringVar()

        self.waypointCheckbutton = None
        self.waypointEntry       = None


        ## stopover
        self.stopoverEntryState = BooleanVar()
        self.stopover           = StringVar()

        self.stopoverCheckbutton = None
        self.stopoverEntry       = None


        ## source
        self.sourceEntryState = BooleanVar()
        self.source           = StringVar()

        self.sourceCheckbutton = None
        self.sourceEntry       = None


        ## source
        self.destinationEntryState = BooleanVar()
        self.destination           = StringVar()

        self.destinationCheckbutton = None
        self.destinationEntry       = None


        # declare missionFrame components
        self.missionTextBox = None

        # Build the different parts of the main window
        #self.buildMenu(self.gui)
        self.buildMainView(self.gui)

        self.activeMission = None
        if self.debugging:
            self.activeMission = self.missionList[0]            #TAKE THIS OUT EVENTUALLY
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
        centerFrame  = ScrollingCenterFrame(window)
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
        self.populateComponentSelections()

        print("Done.")
    #end buildCenterFrame


    def buildComponentsOnCenterFrame(self):
        #TODO: Implement this - ~75% completed
        print()
        print("\tRunning buildComponentsOnCenterFrame...", end="\t\t")

        indent = 20
        off = "disabled"
        cf = self.centerFrame

        # Display name
        displayNameLabel = ttk.Label(cf, text="Mission Display Name")
        displayNameLabel.grid(row=1, column=0, sticky="ew")
        self.displayNameCheckbutton = ttk.Checkbutton(cf,
                                                      command=lambda: self.cbValueChanged(self.displayNameEntryState,
                                                                                          self.displayNameEntry),
                                                      variable=self.displayNameEntryState, onvalue=1, offvalue=0)
        self.displayNameCheckbutton.grid(row=1, column=1)

        self.displayName.set("<name>")
        self.displayNameEntry = ttk.Entry(cf, textvariable=self.displayName, state=off, width=20) # setting the width to 30 here widens the rest of them
        self.displayNameEntry.grid(row=2, column=0, sticky="ew", padx=(indent,0))


        # Description
        descriptionLabel = ttk.Label(cf, text="Description")
        descriptionLabel.grid(row=3, column=0, sticky="ew")
        self.descriptionCheckbutton = ttk.Checkbutton(cf,
                                                      command=lambda: self.cbValueChanged(self.descriptionEntryState,
                                                                                          self.descriptionEntry),
                                                      variable=self.descriptionEntryState, onvalue=1, offvalue=0)
        self.descriptionCheckbutton.grid(row=3, column=1)

        self.description.set("<description>")
        self.descriptionEntry = ttk.Entry(cf, textvariable=self.description, state=off)
        self.descriptionEntry.grid(row=4, column=0, sticky="ew", padx=(indent,0))


        # isBlocked
        isBlockedLabel = ttk.Label(cf, text="Blocked")
        isBlockedLabel.grid(row=5, column=0, sticky="ew")
        self.isBlockedCheckbutton = ttk.Checkbutton(cf,
                                                    command=lambda: self.cbValueChanged(self.isBlockedEntryState,
                                                                                        self.isBlockedMessageEntry),
                                                    variable=self.isBlockedEntryState, onvalue=1, offvalue=0)
        self.isBlockedCheckbutton.grid(row=5, column=1)

        self.isBlockedMessage.set("<message>")
        self.isBlockedMessageEntry = ttk.Entry(cf, textvariable=self.isBlockedMessage, state=off)
        self.isBlockedMessageEntry.grid(row=6, column=0, sticky="ew", padx=(indent,0))


        # Deadline
        deadlineLabel = ttk.Label(cf, text="Deadline")
        deadlineLabel.grid(row=7, column=0, sticky="ew")
        self.deadlineCheckbutton = ttk.Checkbutton(cf,
                                                   command=lambda: self.cbValueChanged(self.deadlineEntryState,
                                                                                       self.deadlineOptionalsCheckbutton),
                                                   variable=self.deadlineEntryState, onvalue=1, offvalue=0)
        self.deadlineCheckbutton.grid(row=7, column=1)

        self.deadlineOptionals.set("[<days#> [<multiplier#>]]")
        self.deadlineOptionalsEntry = ttk.Entry(cf, textvariable=self.deadlineOptionals, state=off)
        self.deadlineOptionalsEntry.grid(row=8, column=0, sticky="ew", padx=(indent, 0))
        self.deadlineOptionalsCheckbutton = ttk.Checkbutton(cf,
                                                            command=lambda: self.cbValueChanged(self.deadlineOptionalsEntryState,
                                                                                                self.deadlineOptionalsEntry),
                                                            variable=self.deadlineOptionalsEntryState, onvalue=1, offvalue=0)
        self.deadlineOptionalsCheckbutton.grid(row=8, column=1)


        #TODO: Cargo - may still need some work
        cargoLabel = ttk.Label(cf, text="Cargo")
        cargoLabel.grid(row=9, column=0, sticky="ew")
        self.cargoCheckbutton = ttk.Checkbutton(cf,
                                                command=lambda: self.cbValueChanged(self.cargoEntryState,
                                                                                    self.cargoEntry),
                                                variable=self.cargoEntryState, onvalue=1, offvalue=0)
        self.cargoCheckbutton.grid(row=9, column=1)

        self.cargo.set("(random | <name>) <number#>")
        self.cargoEntry = ttk.Entry(cf, textvariable=self.cargo, state=off)
        self.cargoEntry.grid(row=10, column=0, sticky="ew", padx=(indent, 0))

        self.cargoOptionals.set("[<number#> [<probability#>]]")
        self.cargoOptionalsEntry = ttk.Entry(cf, textvariable=self.cargoOptionals, state=off)
        self.cargoOptionalsEntry.grid(row=11, column=0, sticky="ew", padx=(indent, 0))
        self.cargoOptionalsCheckbutton = ttk.Checkbutton(cf,
                                                         command=lambda: self.cbValueChanged(self.cargoOptionalsEntryState,
                                                                                             self.cargoOptionalsEntry),
                                                         variable=self.cargoOptionalsEntryState, onvalue=1, offvalue=0)
        self.cargoOptionalsCheckbutton.grid(row=11, column=1)

        cargoIllegalLabel = ttk.Label(cf, text="Illegal")
        cargoIllegalLabel.grid(row=12, column=0, sticky="ew", padx=(indent, 0))
        self.cargoIllegalCheckbutton = ttk.Checkbutton(cf,
                                                       command=lambda: self.cbValueChanged(self.cargoIllegalEntryState,
                                                                                           self.cargoFineEntry),
                                                       variable=self.cargoIllegalEntryState, onvalue=1, offvalue=0)
        self.cargoIllegalCheckbutton.grid(row=12, column=1)

        self.cargoFine.set("<fine#>")
        self.cargoFineEntry = ttk.Entry(cf, textvariable=self.cargoFine, state=off)
        self.cargoFineEntry.grid(row=13, column=0, sticky="ew", padx=(indent*2, 0))

        self.cargoFineMessage.set("[<message>]")
        self.cargoFineMessageEntry = ttk.Entry(cf, textvariable=self.cargoFineMessage, state=off)
        self.cargoFineMessageEntry.grid(row=14, column=0, sticky="ew", padx=(indent*2, 0))
        self.cargoFineMessageCheckbutton = ttk.Checkbutton(cf,
                                                           command=lambda: self.cbValueChanged(self.cargoFineMessageEntryState,
                                                                                               self.cargoFineMessageEntry),
                                                           variable=self.cargoFineMessageEntryState, onvalue=1, offvalue=0)
        self.cargoFineMessageCheckbutton.grid(row=14, column=1)

        cargoStealthLabel = ttk.Label(cf, text="Stealth")
        cargoStealthLabel.grid(row=15, column=0, sticky="ew", padx=(indent, 0))
        self.cargoStealthCheckbutton = ttk.Checkbutton(cf,
                                                       command=lambda: self.cbValueChanged(self.cargoStealthEntryState,
                                                                                           "cargoStealthCheckButton"),
                                                       variable=self.cargoStealthEntryState, onvalue=1, offvalue=0)
        self.cargoStealthCheckbutton.grid(row=15, column=1)


        # Passengers
        passengersLabel = ttk.Label(cf, text="Passengers")
        passengersLabel.grid(row=16, column=0, sticky="ew")
        self.passengersCheckbutton = ttk.Checkbutton(cf,
                                                     command=lambda: self.cbValueChanged(self.passengersEntryState,
                                                                                         self.passengersEntry),
                                                     variable=self.passengersEntryState, onvalue=1, offvalue=0)
        self.passengersCheckbutton.grid(row=16, column=1)

        self.passengers.set("<number#>")
        self.passengersEntry = ttk.Entry(cf, textvariable=self.passengers, state=off)
        self.passengersEntry.grid(row=17, column=0, sticky="ew", padx=(indent, 0))

        self.passengersOptionals.set("[<number#> [<probability#>]]")
        self.passengersOptionalsEntry = ttk.Entry(cf, textvariable=self.passengersOptionals, state=off)
        self.passengersOptionalsEntry.grid(row=18, column=0, sticky="ew", padx=(indent, 0))
        self.passengersOptionalsCheckbutton = ttk.Checkbutton(cf,
                                                              command=lambda: self.cbValueChanged(self.passengersOptionalsEntryState,
                                                                                                  self.passengersOptionalsEntry),
                                                              variable=self.passengersOptionalsEntryState, onvalue=1, offvalue=0)
        self.passengersOptionalsCheckbutton.grid(row=18, column=1)


        # isInvisible
        isInvisibleLabel = ttk.Label(cf, text="Invisible")
        isInvisibleLabel.grid(row=19, column=0, sticky="ew")
        self.isInvisibleCheckbutton = ttk.Checkbutton(cf,
                                                      command=lambda: self.cbValueChanged(self.isInvisibleEntryState,
                                                                                          "isInvisibleCheckbutton"),
                                                      variable=self.isInvisibleEntryState, onvalue=1, offvalue=0)
        self.isInvisibleCheckbutton.grid(row=19, column=1)


        # priorityLevel
        priorityLevelLabel = ttk.Label(cf, text="Priority Level")
        priorityLevelLabel.grid(row=20, column=0, sticky="ew")
        self.priorityLevelCheckbutton = ttk.Checkbutton(cf,
                                                        command=lambda: self.cbValueChanged(self.priorityLevelEntryState,
                                                                                            "priorityLevelCheckbutton"),
                                                        variable=self.priorityLevelEntryState, onvalue=1, offvalue=0)
        self.priorityLevelCheckbutton.grid(row=20, column=1)
        self.rbPriority = ttk.Radiobutton(cf, text="Priority", variable=self.rbPriorityValue, value="priority",
                                          command=lambda: self.rbValueChanged(self.rbPriorityValue, self.rbPriority))
        self.rbPriority.grid(row=21, column=0, sticky="w", padx=(indent, 0))
        self.rbMinor = ttk.Radiobutton(cf, text="Minor", variable=self.rbPriorityValue, value="minor",
                                       command=lambda: self.rbValueChanged(self.rbPriorityValue, self.rbMinor))
        self.rbMinor.grid(row=22, column=0, sticky="w", padx=(indent, 0))


        # whereShown
        whereShownLabel = ttk.Label(cf, text="Where to show")
        whereShownLabel.grid(row=23, column=0, sticky="ew")
        self.whereShownCheckbutton = ttk.Checkbutton(cf,
                                                     command=lambda: self.cbValueChanged(self.whereShownEntryState,
                                                                                         "whereShownCheckbutton"),
                                                     variable=self.whereShownEntryState, onvalue=1, offvalue=0)
        self.whereShownCheckbutton.grid(row=23, column=1)
        self.rbJob = ttk.Radiobutton(cf, text="Job", variable=self.rbWhereShownValue, value="job",
                                     command=lambda: self.rbValueChanged(self.rbWhereShownValue, self.rbJob))
        self.rbJob.grid(row=24, column=0, sticky="w", padx=(indent, 0))
        self.rbLanding = ttk.Radiobutton(cf, text="Landing", variable=self.rbWhereShownValue, value="landing",
                                         command=lambda: self.rbValueChanged(self.rbWhereShownValue, self.rbLanding))
        self.rbLanding.grid(row=25, column=0, sticky="w", padx=(indent, 0))
        self.rbAssisting = ttk.Radiobutton(cf, text="Assisting", variable=self.rbWhereShownValue, value="assisting",
                                           command=lambda: self.rbValueChanged(self.rbWhereShownValue, self.rbAssisting))
        self.rbAssisting.grid(row=26, column=0, sticky="w", padx=(indent, 0))
        self.rbBoarding = ttk.Radiobutton(cf, text="Boarding", variable=self.rbWhereShownValue, value="boarding",
                                          command=lambda: self.rbValueChanged(self.rbWhereShownValue, self.rbBoarding))
        self.rbBoarding.grid(row=27, column=0, sticky="w", padx=(indent, 0))


        # repeat
        repeatLabel = ttk.Label(cf, text="Repeat")
        repeatLabel.grid(row=28, column=0, sticky="ew")
        self.repeatCheckbutton = ttk.Checkbutton(cf,
                                                 command=lambda: self.cbValueChanged(self.repeatEntryState,
                                                                                     self.repeatOptionalsCheckbutton),
                                                 variable=self.repeatEntryState, onvalue=1, offvalue=0)
        self.repeatCheckbutton.grid(row=28, column=1)

        self.repeatOptionals.set("[<times#>]")
        self.repeatOptionalsEntry = ttk.Entry(cf, textvariable=self.repeatOptionals, state=off)
        self.repeatOptionalsEntry.grid(row=29, column=0, sticky="ew", padx=(indent, 0))
        self.repeatOptionalsCheckbutton = ttk.Checkbutton(cf,
                                                          command=lambda: self.cbValueChanged(self.repeatOptionalsEntryState,
                                                                                              self.repeatOptionalsEntry),
                                                          variable=self.repeatOptionalsEntryState, onvalue=1, offvalue=0)
        self.repeatOptionalsCheckbutton.grid(row=29, column=1)


        # Clearance
        clearanceLabel = ttk.Label(cf, text="Clearance")
        clearanceLabel.grid(row=30, column=0, sticky="ew")
        self.clearanceCheckbutton = ttk.Checkbutton(cf,
                                                    command=lambda: self.cbValueChanged(self.clearanceEntryState,
                                                                                        self.clearanceOptionalsEntry),
                                                    variable=self.clearanceEntryState, onvalue=1, offvalue=0)
        self.clearanceCheckbutton.grid(row=30, column=1)

        self.clearanceOptionals.set("[<message>]")
        self.clearanceOptionalsEntry = ttk.Entry(cf, textvariable=self.clearanceOptionals, state=off)
        self.clearanceOptionalsEntry.grid(row=31, column=0, sticky="ew", padx=(indent, 0))


        # isInfiltrating
        isInfiltratingLabel = ttk.Label(cf, text="Infiltrating")
        isInfiltratingLabel.grid(row=32, column=0, sticky="ew")
        self.isInfiltratingCheckbutton = ttk.Checkbutton(cf,
                                                         command=lambda: self.cbValueChanged(self.isInfiltratingEntryState,
                                                                                             "isInfiltratingCheckbutton"),
                                                         variable=self.isInfiltratingEntryState, onvalue=1, offvalue=0)
        self.isInfiltratingCheckbutton.grid(row=32, column=1)


        # waypoint
        waypointLabel = ttk.Label(cf, text="Waypoint")
        waypointLabel.grid(row=33, column=0, sticky="ew")
        self.waypointCheckbutton = ttk.Checkbutton(cf,
                                                      command=lambda: self.cbValueChanged(self.waypointEntryState,
                                                                                          self.waypointEntry),
                                                      variable=self.waypointEntryState, onvalue=1, offvalue=0)
        self.waypointCheckbutton.grid(row=33, column=1)

        self.waypoint.set("<system>")
        self.waypointEntry = ttk.Entry(cf, textvariable=self.waypoint, state=off)
        self.waypointEntry.grid(row=34, column=0, sticky="ew", padx=(indent, 0))


        # stopover
        stopoverLabel = ttk.Label(cf, text="Stopover")
        stopoverLabel.grid(row=35, column=0, sticky="ew")
        self.stopoverCheckbutton = ttk.Checkbutton(cf,
                                                   command=lambda: self.cbValueChanged(self.stopoverEntryState,
                                                                                       self.stopoverEntry),
                                                   variable=self.stopoverEntryState, onvalue=1, offvalue=0)
        self.stopoverCheckbutton.grid(row=35, column=1)

        self.stopover.set("<planet>")
        self.stopoverEntry = ttk.Entry(cf, textvariable=self.stopover, state=off)
        self.stopoverEntry.grid(row=36, column=0, sticky="ew", padx=(indent, 0))


        # source
        sourceLabel = ttk.Label(cf, text="Source")
        sourceLabel.grid(row=37, column=0, sticky="ew")
        self.sourceCheckbutton = ttk.Checkbutton(cf,
                                                 command=lambda: self.cbValueChanged(self.sourceEntryState,
                                                                                     self.sourceEntry),
                                                 variable=self.sourceEntryState, onvalue=1, offvalue=0)
        self.sourceCheckbutton.grid(row=37, column=1)

        self.source.set("<planet>")
        self.sourceEntry = ttk.Entry(cf, textvariable=self.source, state=off)
        self.sourceEntry.grid(row=38, column=0, sticky="ew", padx=(indent, 0))


        # destination
        destinationLabel = ttk.Label(cf, text="Destination")
        destinationLabel.grid(row=39, column=0, sticky="ew")
        self.sourceCheckbutton = ttk.Checkbutton(cf,
                                                 command=lambda: self.cbValueChanged(self.destinationEntryState,
                                                                                     self.destinationEntry),
                                                 variable=self.destinationEntryState, onvalue=1, offvalue=0)
        self.sourceCheckbutton.grid(row=39, column=1)

        self.destination.set("<planet>")
        self.destinationEntry = ttk.Entry(cf, textvariable=self.destination, state=off)
        self.destinationEntry.grid(row=40, column=0, sticky="ew", padx=(indent, 0))


        #TODO: Add Triggers


        print("Done.")
    #end buildComponentsOnCenterFrame


    def cbValueChanged(self, entryState, modifiedWidget):
        print("The value of %s is:" % modifiedWidget.__str__(), end="\t\t")
        print(entryState.get())
        if type(modifiedWidget) is str:
            print("")
        elif entryState.get() is True:
            modifiedWidget.config(state='enabled')
        elif entryState.get() is False:
            modifiedWidget.config(state='disabled')
    #end cbValueChanged


    #TODO: display name, not "PY_VARXX" (pending SO question)
    def rbValueChanged(self, radioValue, modifiedWidget):
        print("The value of %s is now:" % radioValue.__str__(), end="\t\t")
        print(modifiedWidget.cget("value"))
    #end rbValueChanged


    def populateComponentSelections(self):
        print("\tTesting populateComponentSelections...", end="\t\t")

        print("Done.")
    #end populateComponentSelections

    # COMPLETE, WORKING
    def buildMissionFrame(self):
        print("Building missionFrame...", end="\t")

        #Display a default mission template on launch
        self.missionFrame.grid(row=0, column=2, sticky="nsew")
        mfTitle = ttk.Label(self.missionFrame, text="Mission Text")
        mfTitle.pack()

        #Populate the Text with a mission template
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
        #TODO: Implement this
        print("Updating centerFrame...", end="\t\t")

        #self.cfTitleText.set(str(self.activeMission.missionName))

        print("Done.")
    #end updateCenterFrame


    def updateMissionFrame(self):
        print("Updating missionFrame...", end="\t")

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

    # COMPLETE, WORKING
    def missionSelected(self, event):
        selectedMissionName = self.missionComboBox.get()
        print('\nOpening mission "%s"' % selectedMissionName)
        self.activeMission = self.missionNameToObjectDict.get(selectedMissionName)
        self.updateCenterFrame()
        self.updateMissionFrame()
    #end missionSelected


    def addMission(self, newMissionName):
        print("Adding mission: \"%s\"..." % newMissionName, end="\t\t")

        mission = Mission(newMissionName, default=True)
        self.missionList.append(mission)
        self.missionNameToObjectDict.update({mission.missionName: mission})
        self.activeMission = mission
        self.updateOptionFrame()
    #end addMission


#end class GUI