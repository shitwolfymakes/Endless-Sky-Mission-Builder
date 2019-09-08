""" menuactions.py
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
"""

import re
import shlex
import webbrowser
import logging

from tkinter import filedialog

from Mission import *
from MissionCompiler import MissionCompiler
from MissionFileParser import MissionFileParser
from PopupWindow import PopupWindow


def open_file(app):
    """
    This method handles reading in Endless Sky mission files.
    It creates a mission object for each mission it finds,
    and then calls the parser to parse the data

    :param app: The instance of ESMB
    """

    #TODO: add handling for "event" items inside missionfile
    #    NOTE: EVENTS ARE STORED IN THE MISSION FILE, BUT ARE
    #    COMPLETELY SEPARATE FROM MISSIONS. SAVE HANDLING
    #    THESE FOR LATER

    #TODO: Add handling for mission preamble(license text)

    # empty the missionList
    app.missionList             = []
    app.missionNameToObjectDict = {}

    logging.debug("\nSelecting mission file...")
    f = filedialog.askopenfile()
    if f is None:  # askopenasfile return `None` if dialog closed with "cancel".
        return
    logging.debug("Opening file: %s\n" % f.name)

    with open(f.name) as missionfile:
        mission_lines = missionfile.readlines()
        # Print the mission file to the console
        #print_mission_file(missionLines)

    # populate the missionList object
    #TODO: refactor this to use enumerate()
    i = 0
    event_line = False
    match_mission = re.compile(r'^ *mission')
    match_event = re.compile(r'^event')
    for line in mission_lines:
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

        if re.search(match_mission, line):
            event_line = False
            #print(line)
            tokens      = shlex.split(line)
            cur_mission = Mission(tokens[1])
            app.missionList.append(cur_mission)
            app.missionNameToObjectDict.update({cur_mission.missionName: cur_mission})
            app.missionList[i].add_line(line)
            i += 1
            continue
        elif re.search(match_event, line):
            logging.debug("EVENT FOUND IN FILE")
            event_line = True
            continue
        else:
            if event_line is True:
                continue
            app.missionList[i - 1].add_line(line)
        # end if/else
    # end for

    logging.debug("\nMissions loaded:")
    for mission in app.missionList:
        logging.debug("\t%s" % mission.missionName)
        #mission.printMission()
    # end for

    # close the file
    missionfile.close()

    parser = MissionFileParser(app)
    parser.run()

    app.activeMission = app.missionList[0]
    app.update_option_frame()
# end open_file


def print_mission_file(mission_file):
    """
    Helper function to print the entire mission file

    :mission_file: the text data of the mission file
    """
    for line in mission_file:
        logging.debug(line, end="")
    logging.debug()
#end print_mission_file


def save_file(app):
    """
    This method saves the data to a mission file

    :param app: The instance of ESMB
    """
    #TODO: add preamble comments
    logging.debug("\nSaving selected file...")
    compile_mission(app)
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    for mission in app.missionList:
        for line in mission.missionLines:
            f.write(line)
        f.write("\n\n\n")       # add whitespace between missions, per the Creating Missions guidelines
    f.close()

    logging.debug("Done.")
# end save_file


def new_mission(app):
    """
    Prompt the user for the name of a new mission

    :param app: The instance of ESMB
    """
    logging.debug("\nCreating new mission...")
    PopupWindow(app, app.gui, "Enter new mission name:")
# end newFile


def compile_mission(app):
    """
    Store the active working data to the data model.
    NOTE: This will not save any data to a file

    :param app: The instance of ESMB
    """
    compiler = MissionCompiler(app)
    compiler.run()
    app.update_mission_frame()
# end compile_mission


def help_user():
    """Open the Creating Mission documentation for Endless Sky"""
    #TODO: Replace this with a link to ESMB user documentation once it's completed
    webbrowser.open_new(r"https://github.com/endless-sky/endless-sky/wiki/CreatingMissions")
#end help_user
