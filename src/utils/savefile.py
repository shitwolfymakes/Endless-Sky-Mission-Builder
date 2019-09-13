""" savefile.py
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

from src.utils.compilemission import compile_mission


def save_file(app):
    """
    This method saves the data to a mission file

    :param app: The instance of ESMB
    """
    #TODO: add preamble comments
    logging.debug("Saving selected file...")
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
