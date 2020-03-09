""" MultiOptionFrame.py
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


class MultiOptionFrame(ttk.Frame):
    """This class extends ttk.Frame to create a custom GUI widget"""

    def __init__(self, parent, name, options_list):
        ttk.Frame.__init__(self, parent)

        self.name = name
        self.options_list = options_list

        self.row_num = 0
        self.list_entry_states = []
        self.list_checkbuttons = []

        self._build()
    #end init


    def _build(self):
        logging.debug("Creating MultiOptionFrame using: ", self.options_list)
        # add frame label and checkbutton
        self.label = ttk.Label(self, text=self.name, width=30)
        self.label.grid(row=self.row_num, column=0, sticky="w", padx=(5, 0))
        self.row_num += 1

        # add the options
        for option in self.options_list:
            label = ttk.Label(self, text=option)
            label.grid(row=self.row_num, column=0, sticky="ew", padx=(20, 0))
            self.list_entry_states.append(BooleanVar())
            self.list_checkbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0,
                                                          variable=self.list_entry_states[-1]))
            self.list_checkbuttons[-1].configure(command=partial(self.cb_value_changed,
                                                                 self.list_entry_states[-1],
                                                                 option))
            self.list_checkbuttons[-1].grid(row=self.row_num, column=1, sticky="e")
            self.row_num += 1
        #end for
    #end _build


    @staticmethod
    def cb_value_changed(entry_state, modified_widget):
        """
        Log the change of the entry_state of a given widget

        :param entry_state: The boolean value of the entry
        :param modified_widget: The widget modified
        """
        logging.debug("The value of %s is: %s" % (modified_widget, entry_state.get()))
    # end cb_value_changed
#end class MultiOptionFrame
