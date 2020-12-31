""" newmission.py
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

from widgets.NewMissionPopup import NewMissionPopup


def new_mission():
    """Prompt the user for the name of a new mission"""
    logging.debug("Creating new mission...")
    NewMissionPopup("Enter new mission name:")
#end new_mission
