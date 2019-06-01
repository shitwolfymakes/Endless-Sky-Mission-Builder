''' guiutils.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

This file contains helper functions for the ESMB gui, so that they don't need to be rewritten,
    or worse, imported from the gui components themselves

'''
from Mission import *

def addMission(app, newMissionName):
    print("Adding mission: \"%s\"..." % newMissionName, end="\t\t")

    mission = Mission(newMissionName, default=True)
    app.missionList.append(mission)
    app.missionNameToObjectDict.update({mission.missionName: mission})
    app.activeMission = mission
    app.updateOptionFrame()
# end addMission