''' GUI.py
Created by wolfy

This handles the GUI for ESMB

'''
from tkinter import *
from tkinter import ttk
from menuactions import *

class GUI(object):

    def __init__(self):
        print("Building GUI...")
        self.missionList   = [Mission("Default")]       #TODO: Initialize with template mission on launch
        self.missionNames  = []

        # Build the application window
        self.gui = Tk()

        # Set the attributes of the main window
        windowWidth = 140 * 6
        windowHeight = 80 * 6

        sWidth = self.gui.winfo_screenwidth()
        sHeight = self.gui.winfo_screenheight()

        x = (sWidth / 2) - (windowWidth / 2)
        y = (sHeight / 2) - (windowHeight / 2)

        self.gui.title("ESMissionBuilder")
        self.gui.configure(bg="orange")
        self.gui.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, x, y))

        self.ofWidth = None
        self.cfWidth = None
        self.mfWidth = None

        self.missionComboBox = None

        # Build the different parts of the main window
        self.buildMenu(self.gui)
        self.optionFrame, self.centerFrame, self.missionFrame = self.buildMainView(self.gui,
                                                                                   windowWidth,
                                                                                   str(windowHeight))

        # Run the program
        self.gui.mainloop()
    #end init


    # COMPLETE, WORKING
    def buildMenu(self, window):
        # creating a menu instance
        menu = Menu()
        window.config(menu=menu)

        # create the file object
        file = Menu(menu)
        edit = Menu(menu)

        # adds a command to the menu option, names it, and set the command to run
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


    #COMPLETE, WORKING
    def buildMainView(self, window, windowWidth, windowHeight):
        # build the Options bar on the far left
        self.ofWidth = str(windowWidth * .2)
        optionFrame = ttk.Frame(window, width=self.ofWidth, height=windowHeight)

        # build used component list
        self.cfWidth = str(windowWidth * .4)
        centerFrame = ttk.Frame(window, width=self.cfWidth, height=windowHeight)

        # build the mission text box on the far right
        self.mfWidth = str(windowWidth * .4)
        missionFrame = ttk.Frame(window, width=self.mfWidth, height=windowHeight)

        # set up each of the frames
        self.buildOptionFrame(optionFrame)
        self.buildCenterFrame(centerFrame)
        self.buildMissionFrame(missionFrame)

        return optionFrame, centerFrame, missionFrame
    #end buildMainView


    ### BUILDING FRAMES ###


    def buildOptionFrame(self, optionFrame):
        print("Building optionFrame...", end="\t\t")
        #TODO: Add combobox to list missions - DO THIS SECOND
        optionFrame.grid(row=0, column=0)

        # build default values here
        label1 = ttk.Label(optionFrame, text="Mission")
        label1.pack()

        self.missionNames.append("Default")

        # declare the combobox here, fill with missionNames
        self.missionComboBox = ttk.Combobox(optionFrame, state="readonly", values=self.missionNames)
        self.missionComboBox.bind("<<ComboboxSelected>>", self.missionSelected)
        self.missionComboBox.pack()
        self.missionComboBox.current(0)

        # set default values here

        print("Done.")
    #end buildOptionFrame


    def buildCenterFrame(self, centerFrame):
        print("Building centerFrame...", end="\t\t")
        #TODO: Populate frame
        centerFrame.grid(row=0, column=1)

        print("Done.")
    #end buildCenterFrame


    def buildMissionFrame(self, missionFrame):
        print("Building missionFrame...", end="\t")
        #TODO: Display a default mission template on launch
        missionFrame.grid(row=0, column=2)

        # create a label to print the mission text

        # make the label fill the frame

        #TODO: Temp printing the mission from missionLines, replace with formatted output(toString?) from Mission obj

        print("Done.")
    #end buildMissionFrame


    ### UPDATING FRAMES ###


    def updateOptionFrame(self):
        #TODO: Implement this - ~50% Completed
        print("\nUpdating optionFrame...")

        ### Start updating combobox
        ml = self.missionList
        self.missionNames = []
        print("New mission options:", end=" ")
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
    #end updateOptionFrame


    def updateCenterFrame(self, activeM):
        #TODO: Implement this
        print("Updating centerFrame...")
        labelCF1 = ttk.Label(self.centerFrame, text=activeM.missionName)
        labelCF1.pack()
        print("Done.")
    #end updateCenterFrame


    def updateMissionFrame(self, activeM):
        #TODO: Implement this
        print("Updating missionFrame")
        labelMF1 = ttk.Label(self.missionFrame, text=activeM.missionName)
        labelMF1.pack()

        # print mission text to a Canvas in the missionFrame
        #TODO: make this pretty
        missionTextBox = Canvas(self.missionFrame, bg='#FFFFFF',
                                width=self.mfWidth,
                                height=self.missionFrame.winfo_height(),
                                scrollregion=(0, 0, 500, 500) )
        missionTextBox.create_text(0, 0, anchor='nw', text=activeM.missionLines, state=DISABLED, justify=LEFT)

        # add scrollbars
        hbar = Scrollbar(self.missionFrame, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=missionTextBox.xview)
        vbar = Scrollbar(self.missionFrame, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=missionTextBox.yview)
        missionTextBox.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        missionTextBox.pack(side=LEFT, expand=True, fill=BOTH)

        print("Done.")
    #end updateMissionFrame


    ### MISC METHODS ###


    def missionSelected(self, event):
        #TODO: Implement this
        print('Opening mission "%s"' % self.missionComboBox.get())
    #end missionSelected

#end class GUI