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
from tkinter import BooleanVar
from tkinter import ttk

import src.widgets as widgets


class AggregatedDialogFrame(ttk.Frame):
    """
    This class extends ttk.Frame, allowing the user to add an arbitrary number of TriggerFrame widgets to the GUI.
    """

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        logging.debug("\t\tBuilding AggregatedDialogFrame")
        self.dialog_list = []
        self.entry_state = BooleanVar()

        self.outer = ttk.Frame(self)
        self.outer.grid()
        self.outer.grid_columnconfigure(0, weight=1)

        section_name_label = ttk.Label(self.outer, text="  Dialog", anchor="w", width=30)
        section_name_label.grid(row=0, column=0, sticky="ew")

        cb = ttk.Checkbutton(self.outer, onvalue=1, offvalue=0, variable=self.entry_state)
        cb.configure(command=partial(self.cb_value_changed, self.entry_state, self))
        cb.grid(row=0, column=1, sticky="e", padx=(20, 0))

        self.inner = ttk.Frame(self.outer)
        self.inner.grid(row=1, column=0, columnspan=2, sticky="nsew")

        add_button = ttk.Button(self.outer, text="Add Dialog", command=self._add_dialog)
        add_button.grid(row=2, column=0, columnspan=2, sticky="ew")
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


    @staticmethod
    def cb_value_changed(entry_state, modified_widget):
        """
        Log the change of the entry_state of a given widget

        :param entry_state: The boolean value of the entry
        :param modified_widget: The widget modified
        """
        logging.debug("The value of %s is: %s" % (modified_widget, entry_state.get()))
    # end cb_value_changed
#end class
