""" openfile.py
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
import re
import shlex
from tkinter import filedialog

from src.model import Mission, MissionFileParser


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

    logging.debug("Selecting mission file...")
    f = filedialog.askopenfile()
    if f is None:  # askopenasfile return `None` if dialog closed with "cancel".
        return
    logging.debug("Opening file: %s" % f.name)

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

    logging.debug("\t\tMissions loaded:")
    for mission in app.missionList:
        logging.debug("\t\t%s" % mission.missionName)
        #mission.printMission()
    # end for

    missionfile.close()

    parser = MissionFileParser(app)
    parser.run()

    app.activeMission = app.missionList[0]
    app.update_option_frame()
#end open_file


def print_mission_file(mission_file):
    """
    Helper function to print the entire mission file

    :mission_file: the text data of the mission file
    """
    for line in mission_file:
        logging.debug(line, end="")
#end print_mission_file
