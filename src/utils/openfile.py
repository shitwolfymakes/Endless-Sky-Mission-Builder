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
from tkinter import filedialog

from src.model import MissionFileParser


def open_file():
    """
    This method handles reading in Endless Sky mission files.
    It creates a mission object for each mission it finds,
    and then calls the parser to parse the data

    :param app: The instance of ESMB
    """
    #TODO: Add handling for mission preamble(license text)

    logging.debug("Selecting mission file...")
    f = filedialog.askopenfile()
    if f is None:  # askopenfile() returns `None` if dialog closed with "cancel".
        return
    logging.debug("Opening file: %s" % f.name)

    with open(f.name) as infile:
        mission_lines = infile.readlines()
    infile.close()

    parser = MissionFileParser(mission_lines)
    parser.run()
#end open_file


def print_mission_file(mission_file):
    """
    Helper function to print the entire mission file

    :mission_file: the text data of the mission file
    """
    for line in mission_file:
        logging.debug(line, end="")
#end print_mission_file
