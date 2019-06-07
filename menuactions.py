''' menuactions.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

This file contains the code for each menu action(open, save, undo, etc.)
'''

import re, shlex
import webbrowser

from tkinter import filedialog

from Mission import *
from MissionCompiler import MissionCompiler
from MissionFileParser import MissionFileParser
from PopupWindow import PopupWindow


def openFile(app):
    #TODO: IMPLEMENT THIS - ~99% completed (Won't be done until events are handled in version 3)

    #TODO: add handling for "event" items inside missionfile
    #    NOTE: EVENTS ARE STORED IN THE MISSION FILE, BUT ARE
    #    COMPLETELY SEPARATE FROM MISSIONS. SAVE HANDLING
    #    THESE FOR LATER

    #TODO: Add handling for mission preamble

    # empty the missionList
    app.missionList             = []
    app.missionNameToObjectDict = {}

    print("\nSelecting mission file...")
    f = filedialog.askopenfile()
    if f is None:  # askopenasfile return `None` if dialog closed with "cancel".
        return
    print("Opening file: %s\n" % f.name)

    with open(f.name) as missionfile:
        missionLines = missionfile.readlines()
        # Print the mission file to the console
        #printMissionFile(missionLines)

    # populate the missionList object
    i = 0
    eventLine = False
    matchMission = re.compile(r'^ *mission')
    matchEvent = re.compile(r'^ *event')
    for line in missionLines:
        # print(line, end="")
        line = line.rstrip()
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

        # EVENTLINE SENTINEL IS NECESSARY TO KEEP EVENT OBJECTS FROM BEING ADDED TO
        #     MISSIONFILE ERRONEOUSLY

        if re.search(matchMission, line):
            eventLine = False
            #print(line)
            tokens     = shlex.split(line)
            newMission = Mission(tokens[1])
            app.missionList.append(newMission)
            app.missionNameToObjectDict.update({newMission.missionName : newMission})
            app.missionList[i].addLine(line)
            i += 1
            continue
        elif re.search(matchEvent, line):
            print("EVENT FOUND IN FILE")
            eventLine = True
            continue
        else:
            if eventLine is True:
                continue
            app.missionList[i - 1].addLine(line)
        # end if/else
    # end for

    print()
    print("Missions loaded:")
    for mission in app.missionList:
        print("\t%s" % mission.missionName)
        #mission.printMission()
    # end for

    # close the file
    missionfile.close()

    parser = MissionFileParser(app)
    parser.run()

    app.activeMission = app.missionList[0]
    app.updateOptionFrame()
# end openFile


def printMissionFile(missionFile):
    for line in missionFile:
        print(line, end="")
    #end for
    print()
#end printMissionFile


def saveFile(app):
    #TODO: Implement this - ~99% completed
    #TODO: add preamble comments
    print("\nSaving selected file...")
    compileMission(app)
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    for mission in app.missionList:
        for line in mission.missionLines:
            f.write(line)
        f.write("\n\n\n")       # add whitespace between missions
    f.close()

    print("Done.")
# end saveFile


def newMission(app):
    print("\nCreating new mission...")
    PopupWindow(app, app.gui, "Enter new mission name:")
# end newFile


def compileMission(app):
    compiler = MissionCompiler(app)
    compiler.run()
    app.updateMissionFrame()
# end compileMission


def helpUser():
    webbrowser.open_new(r"https://github.com/endless-sky/endless-sky/wiki/CreatingMissions")
#end helpUser