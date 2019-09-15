""" NewMissionPopup.py
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
from tkinter import ttk, Toplevel

from src.model import Mission


class NewMissionPopup(object):
    """This class creates a custom pop-up window for use when creating a new Mission object"""

    def __init__(self, app, master, text):
        self.app = app
        self.top = Toplevel(master)
        self.top.title("New Mission")
        self.top.grab_set()             # freezes the app until the user enters or cancels

        self.label = ttk.Label(self.top, text=text, background='white')
        self.label.pack()
        self.e = ttk.Entry(self.top)
        self.e.pack()
        self.b = ttk.Button(self.top, text='Ok', command=self._cleanup)
        self.b.pack()
    #end init


    def _cleanup(self):
        """Clean up the window we created"""
        name = self.e.get()
        self._add_to_mission_list(self.app, name)
        self.top.grab_release()         # HAVE TO RELEASE
        self.top.destroy()
    #end _cleanup

    @staticmethod
    def _add_to_mission_list(app, new_mission_name):
        logging.debug("Adding mission: \"%s\"..." % new_mission_name)

        mission = Mission(new_mission_name, default=True)
        app.missionList.append(mission)
        app.missionNameToObjectDict.update({mission.missionName: mission})
        app.activeMission = mission
        app.update_option_frame()
    # end add_mission
#end class NewMissionPopup
