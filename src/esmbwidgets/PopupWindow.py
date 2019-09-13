""" PopupWindow.py
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

from tkinter import Toplevel, ttk
from src.gui.guiutils import add_mission


class PopupWindow(object):
    """This class creates a custom pop-up window to display and edit the data in an associated Log object"""

    #TODO: Refactor to pass "New Mission as a parameter"
    #TODO: Refactor to pass "add_mission(self.app, name)"
    def __init__(self, app, master, text):
        self.app = app
        self.top = Toplevel(master)
        self.top.title("New Mission")
        self.top.grab_set()             # freezes the app until the user enters or cancels

        # build the widgets
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
        add_mission(self.app, name)
        self.top.grab_release()         # HAVE TO RELEASE
        self.top.destroy()
    #end _cleanup

#end class popupWindow
