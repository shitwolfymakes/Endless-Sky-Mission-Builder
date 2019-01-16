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
        self.missionList = [Mission("Default")]       #TODO: Initialize with template mission on launch
        # Build the application window
        self.gui = Tk()

        # Set the attributes of the main window
        windowWidth = 140 * 5
        windowHeight = 80 * 5

        sWidth = self.gui.winfo_screenwidth()
        sHeight = self.gui.winfo_screenheight()

        x = (sWidth / 2) - (windowWidth / 2)
        y = (sHeight / 2) - (windowHeight / 2)

        self.gui.title("ESMissionBuilder")
        self.gui.configure(bg="orange")
        self.gui.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, x, y))

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
        ofWidth = str(windowWidth * .2)
        optionFrame = ttk.Frame(window, width=ofWidth, height=windowHeight, relief="raised")#, background="black")

        # build used component list
        cfWidth = str(windowWidth * .4)
        centerFrame = ttk.Frame(window, width=cfWidth, height=windowHeight, relief="raised")#, background="green")

        # build the mission text box on the far right
        mfWidth = str(windowWidth * .4)
        missionFrame = ttk.Frame(window, width=mfWidth, height=windowHeight, relief="raised")#, background="grey")

        # set up each of the frames
        self.buildOptionFrame(optionFrame)
        self.buildCenterFrame(centerFrame)
        self.buildMissionFrame(missionFrame)

        return optionFrame, centerFrame, missionFrame
    #end buildMainView


    def buildOptionFrame(self, optionFrame):
        print("Building optionFrame...", end="\t\t")
        #TODO: Add combobox to list missions - DO THIS SECOND
        optionFrame.grid(row=0, column=0)

        # build default values here

        # declare the combobox here

        # set default values here

        print("Done.")
    #end buildOptionFrame


    def updateOptionFrame(self, ml):
        #TODO: Implement this - ~25% Completed
        #print("\nUpdating optionFrame...")
        #ml = self.getMissionList()
        missionNames = []
        for m in ml:
            missionNames.append(m.missionName)
        print(missionNames)
    #end updateOptionFrame


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

#end class GUI