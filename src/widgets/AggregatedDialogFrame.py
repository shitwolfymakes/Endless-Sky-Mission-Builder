""" AggregatedDialogFrame.py
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

import logging
from functools import partial
from tkinter import *
from tkinter import ttk

import src.widgets as widgets
from src import config


class AggregatedDialogFrame(ttk.Frame):
    """
    This class extends ttk.Frame, allowing the user to add an arbitrary number of TriggerFrame widgets to the GUI.
    """

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        logging.debug("\t\tBuilding AggregatedDialogFrame")
        self.dialog_list = []

        self.outer = ttk.Frame(self)
        self.outer.pack(expand=True, fill="x")

        section_name_label = ttk.Label(self.outer, text="Dialog", anchor="w")
        section_name_label.pack(expand=True, fill="x", padx=(5, 0))

        self.inner = ttk.Frame(self.outer)
        self.inner.pack(expand=True, fill="x")

        add_button = ttk.Button(self.outer, text="Add Dialog", command=self._add_dialog)
        add_button.pack(expand=True, fill="x")
    #end init


    def _add_dialog(self):
        df = widgets.DialogFrame(self)
        self.dialog_list.append(df)
        print(self.dialog_list)
    #end _add_dialog


    def delete_dialog(self, dialog_frame):
        self.dialog_list.remove(dialog_frame)
        dialog_frame.frame.pack_forget()
        dialog_frame.frame.destroy()
        print(self.dialog_list)
        for d in self.dialog_list:
            print(d.data.get())
    #end _delete_dialog
#end class
