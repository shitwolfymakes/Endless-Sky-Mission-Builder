""" guiutils.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

This file contains helper functions and custom widgets for the ESMB gui
"""

from src.model.Mission import *


def add_mission(app, new_mission_name):
    """
    Helper method that creates a new mission, then updates the data model and GUI

    :param app: The ESMB object
    :param new_mission_name: A string containing the name of the new mission
    """
    logging.debug("Adding mission: \"%s\"..." % new_mission_name)

    mission = Mission(new_mission_name, default=True)
    app.missionList.append(mission)
    app.missionNameToObjectDict.update({mission.missionName: mission})
    app.activeMission = mission
    app.update_option_frame()
# end add_mission
