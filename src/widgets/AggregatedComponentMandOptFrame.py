""" AggregatedComponentMandOptFrame.py
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


class AggregatedComponentMandOptFrame(ttk.Frame):
    """
    This class extends ttk.Frame, allowing the user to add an arbitrary
    number of ComponentMandOptFrame widgets to the GUI.
    """

    def __init__(self, parent, title):
        ttk.Frame.__init__(self, parent)

        self.parent = parent
        self.cmof_frame_list = []
        self.entry_state = BooleanVar()

        self.outer = ttk.Frame(self)
        self.outer.grid()
        self.outer.grid_columnconfigure(0, weight=1)

        section_name_label = ttk.Label(self.outer, text=title, anchor="w", width=30)
        section_name_label.grid(row=0, column=0, sticky="ew")

        cb = ttk.Checkbutton(self.outer, onvalue=1, offvalue=0, variable=self.entry_state)
        cb.configure(command=partial(self.cb_value_changed, self.entry_state, self))
        cb.grid(row=0, column=1, sticky="e", padx=(20, 0))

        self.inner = ttk.Frame(self.outer)
        self.inner.grid(row=1, column=0, columnspan=2, sticky="nsew")

        add_button = ttk.Button(self.outer, text="Add %s" % title, command=self._add_cmof)
        add_button.grid(row=2, column=0, columnspan=2, sticky="ew")
    #end init


    def _add_cmof(self):
        pass
    #end _add_cmof


    def remove_cmof(self):
        pass
    #end remove_cmof


    @staticmethod
    def cb_value_changed(entry_state, modified_widget):
        """
        Log the change of the entry_state of a given widget

        :param entry_state: The boolean value of the entry
        :param modified_widget: The widget modified
        """
        logging.debug("The value of %s is: %s" % (modified_widget, entry_state.get()))
    # end cb_value_changed
#end AggregatedComponentMandOptFrame
