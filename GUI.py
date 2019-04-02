''' GUI.py
Created by wolfy

This handles the GUI for ESMB

'''
from tkinter import *
from tkinter import ttk, StringVar
from menuactions import *

class GUI(object):

    def __init__(self):
        print("Building GUI...")
        self.missionList             = [Mission("Default")]       #TODO: Initialize with template mission on launch
        self.missionNameToObjectDict = {"Default" : self.missionList[0]}
        self.missionNames            = []

        # Build the application window
        self.gui = Tk()
        self.gui.title("ESMissionBuilder")
        self.gui.configure(bg="orange")

        self.ofWidth = None
        self.cfWidth = None
        self.mfWidth = None

        # Declare the frames
        self.optionFrame  = None
        self.centerFrame  = None
        self.missionFrame = None

        # declare optionFrame components
        self.missionComboBox = None


        # declare centerFrame components
        self.cfTitle     = ""
        self.cfTitleText = StringVar()

        self.entryState = BooleanVar()

        self.displayNameCheckbutton = None
        self.displayName            = None
        self.displayNameEntry       = None

        self.description = ""


        # declare missionFrame components
        self.mfTitle        = ""
        self.missionTextBox = None
        self.hbar           = None
        self.vbar           = None

        # Build the different parts of the main window
        #self.buildMenu(self.gui)
        self.buildMainView(self.gui)

        # Run the program
        self.gui.mainloop()
    #end init

    # This may be used later, after shortcuts are introduced
    '''
    # COMPLETE, WORKING
    def buildMenu(self, window):
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

    #COMPLETE, WORKING
    def buildMainView(self, window):

        optionFrame  = ttk.Frame(window)
        centerFrame  = ttk.Frame(window)
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
        #TODO: Implement this - ~50% Completed
        print("Building optionFrame...", end="\t\t")
        self.optionFrame.grid(row=0, column=0, sticky="ns")

        # build default values here
        label1 = ttk.Label(self.optionFrame, text="Mission")
        label1.pack()

        self.missionNames.append("Default")

        # declare the combobox here, fill with missionNames
        self.missionComboBox = ttk.Combobox(self.optionFrame, state="readonly", values=self.missionNames)
        self.missionComboBox.bind("<<ComboboxSelected>>", self.missionSelected)
        self.missionComboBox.pack()
        self.missionComboBox.current(0)

        # set default values here

        #add "new mission" button
        newMission = ttk.Button(self.optionFrame, text="New Mission", command=lambda: newFile(self))
        newMission.pack(fill='x')

        #add "save mission" button
        saveMission = ttk.Button(self.optionFrame, text="Save Mission", command=lambda: saveFile(self))
        saveMission.pack(fill='x')

        #add "open mission" button
        openMission = ttk.Button(self.optionFrame, text="Open Mission", command=lambda: openFile(self))
        openMission.pack(fill='x')

        compileMission = ttk.Button(self.optionFrame, text="Compile Mission", command=lambda: compileMissionFile(self))
        compileMission.pack(fill='x')

        print("Done.")
    #end buildOptionFrame


    def buildCenterFrame(self):
        print("Building centerFrame...", end="\t\t")
        self.centerFrame.grid(row=0, column=1, sticky="ns")

        # TODO: Populate frame
        self.buildComponentsOnCenterFrame()

        print("Done.")
    #end buildCenterFrame


    def buildComponentsOnCenterFrame(self):
        print()
        print("\tRunning buildComponentsOnCenterFrame...", end="\t\t")

        indent = 20
        off = "disabled"

        # Print the default mission name
        self.cfTitleText.set("Mission Options")
        self.cfTitle = ttk.Label(self.centerFrame, text=self.cfTitleText.get())
        self.cfTitle.grid(row=0, column=0, sticky="ew")

        #TODO: break these of into separate functions once everything's working

        # Display name
        displayNameLabel = ttk.Label(self.centerFrame, text="Mission Display Name")
        displayNameLabel.grid(row=1, column=0, sticky="ew")

        self.displayNameCheckbutton = ttk.Checkbutton(self.centerFrame,
                                                      command=lambda: self.cbValueChanged(self.displayNameEntry),
                                                      variable=self.entryState, onvalue=1, offvalue=0)
        self.displayNameCheckbutton.grid(row=1, column=1)

        self.displayName = StringVar()
        self.displayNameEntry = ttk.Entry(self.centerFrame, textvariable=self.displayName, state=off)
        self.displayNameEntry.grid(row=2, column=0, sticky="ew", padx=(indent,0))

        # Description
        descriptionLabel = ttk.Label(self.centerFrame, text="Description")
        descriptionLabel.grid(row=3, column=0, sticky="ew")

        descriptionCheckbutton = ttk.Checkbutton(self.centerFrame)
        descriptionCheckbutton.grid(row=3, column=1)

        self.description = StringVar()          # GOTTA KEEP DESCRIPTION AS AN INSTANCE VARIABLE,
        self.description.set("<description>")   #     BECAUSE FUCK YOU, GARBAGE COLLECTION.
        descriptionEntry = ttk.Entry(self.centerFrame, textvariable=self.description, state=off)
        descriptionEntry.grid(row=4, column=0, sticky="ew", padx=(indent,0))

        # isBlocked
        isBlockedLabel = ttk.Label(self.centerFrame, text="Blocked")
        isBlockedLabel.grid(row=5, column=0, sticky="ew")

        isBlockedCheckbutton = ttk.Checkbutton(self.centerFrame)
        isBlockedCheckbutton.grid(row=5, column=1)

        isBlockedMessage = StringVar()
        isBlockedMessageEntry = ttk.Entry(self.centerFrame, textvariable=isBlockedMessage, state=off)
        isBlockedMessageEntry.grid(row=6, column=0, sticky="ew", padx=(indent,0))

        isBlockedMessageCheckbutton = ttk.Checkbutton(self.centerFrame)
        isBlockedMessageCheckbutton.grid(row=6, column=1)

        # Deadline
        deadlineLabel = ttk.Label(self.centerFrame, text="Deadline")
        deadlineLabel.grid(row=7, column=0, sticky="ew")

        deadlineCheckbutton = ttk.Checkbutton(self.centerFrame)
        deadlineCheckbutton.grid(row=7, column=1)

        deadlineDays = StringVar()
        deadlineDaysEntry = ttk.Entry(self.centerFrame, textvariable=deadlineDays, state=off)
        deadlineDaysEntry.grid(row=8, column=0, sticky="ew", padx=(indent, 0))

        deadlineDaysCheckbutton = ttk.Checkbutton(self.centerFrame)
        deadlineDaysCheckbutton.grid(row=8, column=1)

        deadlineMultiplier = StringVar()
        deadlineMultiplierEntry = ttk.Entry(self.centerFrame, textvariable=deadlineMultiplier, state=off)
        deadlineMultiplierEntry.grid(row=9, column=0, sticky="ew", padx=(indent, 0))

        deadlineMultiplierCheckbutton = ttk.Checkbutton(self.centerFrame)
        deadlineMultiplierCheckbutton.grid(row=9, column=1)

        # cargo
        '''
        cargoLabel = ttk.Label(self.centerFrame, text="Cargo")
        cargoLabel.grid(row=10, column=0, sticky="ew")

        cargoCheckbutton = ttk.Checkbutton(self.centerFrame)
        cargoCheckbutton.grid(row=10, column=1)
        '''
        print("Done.")
        self.populateComponentSelections()
    #end buildComponentsOnCenterFrame

    def cbValueChanged(self, modifiedEntrybox):
        print("test, value of %s is:" % modifiedEntrybox.__str__(), end="\t\t")
        print(self.entryState.get())
        if self.entryState.get() is True:
            modifiedEntrybox.config(state='enabled')
        if self.entryState.get() is False:
            modifiedEntrybox.config(state='disabled')
    #end cbValueChanged


    def populateComponentSelections(self):
        print("\tTesting populateComponentSelections...", end="\t\t")

        print("Done.")
    #end populateComponentSelections


    def buildMissionFrame(self):
        #TODO: Implement this - ~75% Completed
        print("Building missionFrame...", end="\t")

        #TODO: Display a default mission template on launch
        self.missionFrame.grid(row=0, column=2, sticky="nsew")
        self.mfTitle = Label(self.missionFrame, text="Mission Text")
        self.mfTitle.pack(expand=1, fill='x')

        #TODO: Populate the Text with a mission template
        self.missionTextBox = Text(self.missionFrame, height=30, width=100, wrap=WORD)
        self.missionTextBox.pack(expand=1, fill='x')
        self.missionTextBox.insert(END, "TEMP FILTER TEXT")

        print("Done.")
    #end buildMissionFrame


    ### UPDATING FRAMES ###


    def updateOptionFrame(self):
        #TODO: Implement this - ~50% Completed
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
        self.updateCenterFrame(self.missionList[0])
        self.updateMissionFrame(self.missionList[0])

        print("Done.")
    #end updateOptionFrame


    def updateCenterFrame(self, activeM):
        #TODO: Implement this
        print("Updating centerFrame...", end="\t\t")
        self.cfTitleText.set(str(activeM.missionName))
        print("Done.")
    #end updateCenterFrame


    def updateMissionFrame(self, activeM):
        #TODO: Implement this - ~75% Completed
        print("Updating missionFrame...", end="\t")

        # delete the old Canvas and ScrollBars
        self.missionTextBox.forget()

        # print mission text to a Canvas in the missionFrame
        self.updateTextCanvas(activeM)

        print("Done.")
    #end updateMissionFrame

    def updateTextCanvas(self, activeM):
        #TODO: Implement this
        self.missionTextBox = Text(self.missionFrame, height=30, width=100, wrap=WORD)
        self.missionTextBox.pack()
        self.missionTextBox.insert(END, activeM.printMissionLinesToText())

        # add scrollbars
        #self.addScrollbars(self.missionFrame)
    #end updateTextCanvas


    ### MISC METHODS ###

    # COMPLETE, BUGGY
    def missionSelected(self, event):
        #TODO: Fix Bug!
        selectedMissionName = self.missionComboBox.get()
        print('Opening mission "%s"' % selectedMissionName)

        newActiveMission = self.missionNameToObjectDict.get(selectedMissionName)
        self.updateCenterFrame(newActiveMission)
        self.updateMissionFrame(newActiveMission)
    #end missionSelected


    def addScrollbars(self, missionFrame):
        #TODO: Implement this
        self.hbar = Scrollbar(missionFrame, orient=HORIZONTAL)
        self.hbar.pack(side=BOTTOM, fill=X)
        self.hbar.config(command=self.missionTextBox.xview)
        self.vbar = Scrollbar(missionFrame, orient=VERTICAL)
        self.vbar.pack(side=RIGHT, fill=Y)
        self.vbar.config(command=self.missionTextBox.yview)
        self.missionTextBox.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.missionTextBox.pack(side=LEFT, expand=True, fill=BOTH)
    #end addScrollbars

#end class GUI