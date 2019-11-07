""" TypeSelectorWindow.py
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

from tkinter import *
from tkinter import ttk


class TypeSelectorWindow(Toplevel):
    """This class creates a custom pop-up window this allows the user to select a given data format"""

    def __init__(self, master, options, callback, **kwargs):
        self.callback = callback
        super().__init__(master, **kwargs)

        self.option_list = ttk.Combobox(self, values=options, state="readonly", width=25)
        self.option_list.current(0)
        self.option_list.pack()

        buttons = ttk.Frame(self)
        ok = ttk.Button(buttons, text="OK", command=self._cleanup)
        ok.pack(side=LEFT, fill="x")
        cxl = ttk.Button(buttons, text="Cancel", command=self._cancelled)
        cxl.pack(fill="x")
        buttons.pack()

        # these commands make the parent window inactive
        self.transient(master)
        self.grab_set()
        master.wait_window(self)
    #end init


    def _cleanup(self):
        """Clean up whatever popups we've created"""
        self.callback(self.option_list.get())
        self.destroy()
    #end _cleanup


    def _cancelled(self):
        """Close the window"""
        self.callback("cancelled")
        self.destroy()
    #end _cancelled
#end class TypeSelectorWindow
