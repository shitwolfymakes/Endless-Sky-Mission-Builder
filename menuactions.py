''' menuactions.py
    This file contains the code for each menu action(open, save, undo, etc.)
'''

import re, shlex

from tkinter import filedialog

from Mission import *


def openFile(app):
    #TODO: IMPLEMENT THIS - ~99% completed (may need changes)

    # empty the missionList
    app.missionList             = []
    app.missionNameToObjectDict = {}

    print("Selecting mission file...")
    f = filedialog.askopenfile()
    if not f:
        print("No file selected...")
    print("Opening file: %s\n" % f.name)

    with open(f.name) as missionfile:
        missionLines = missionfile.readlines()
        # Print the mission file to the console
        #printMissionFile(missionLines)

    # populate the missionList object
    i = 0
    match = re.compile(r'^ *mission')
    for line in missionLines:
        # print(line, end="")
        # quick and dirty, may need validation later
        if "#" in line:
            # print(line, end="")
            continue
        # end if

        # quick and dirty, may need validation later
        if line == "" or line == "\n":
            # print(line, end="")
            continue
        # end if

        if re.search(match, line):
            # print(line, end="")
            tokens     = shlex.split(line)
            newMission = Mission(tokens[1])
            app.missionList.append(newMission)
            app.missionNameToObjectDict.update({newMission.missionName : newMission})
            i += 1
            continue
        else:
            app.missionList[i - 1].addLine(line)
        # end if/else

    # end for

    print("")
    print("Missions loaded:")
    for mission in app.missionList:
        print("\t%s" % mission.missionName)
        #mission.printMission()
    # end for

    #TODO: Store all the little pieces of the Mission in bespoke variables

    #TODO: Update the optionFrame in the gui
    app.updateOptionFrame()

    # close the file
    missionfile.close()
# end openFile

def printMissionFile(missionfile):
    for line in missionfile:
        print(line, end="")
    #end for
#end printMissionFile

def saveFile(app):
    #TODO: Implement this
    print("Saving selected file...")
# end saveFile


def newFile(app):
    #TODO: Implement this
    print("Creating new mission...")
# end newFile

def undoAction(app):
    #TODO: Implement this
    print("Undoing last action...")
# end undoAction
