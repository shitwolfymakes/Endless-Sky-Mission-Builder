""" DialogFrame.py
# Copyright (c) 2020 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""

from functools import partial
from tkinter import StringVar
from tkinter import ttk

import src.widgets as widgets


class DialogFrame(ttk.Frame):
    """This class extends ttk.Frame to create a custom GUI widget"""

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.data = StringVar()

        self.frame = ttk.Frame(parent.inner)
        self.frame.pack(expand=True, fill="x")
        self.frame.grid_columnconfigure(0, weight=1)

        dialog_entry = widgets.DefaultTextEntry(self.frame, "dialog", textvariable=self.data, width=30)
        dialog_entry.grid(row=0, column=1, sticky="ew")

        delete_button = ttk.Button(self.frame, text="X", width=2, command=partial(self.parent.delete_frame, self))
        delete_button.grid(row=0, column=2, sticky="w")
    #end init
#end class DialogFrame
