""" AggregatedTriggerFrame.py
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


class AggregatedCustomFleetFrame(ttk.Frame):
    """
    This class extends ttk.Frame, allowing the user to add an arbitrary number of CustomFleetFrame widgets to the GUI.
    """

    def __init__(self, parent, npc):
        ttk.Frame.__init__(self, parent)

        self.parent = parent
        self.npc = npc
        self.custom_fleet_frames = []

        self.outer = ttk.Frame(self)
        self.outer.pack(expand=True, fill="x")

        section_name_label = ttk.Label(self.outer, text="Custom Fleets", anchor="center")
        section_name_label.pack()

        self.inner = ttk.Frame(self.outer)
        self.inner.pack(expand=True, fill="x")

        add_button = ttk.Button(self.outer, text="Add Custom Fleet", command=self._add_fleet)
        add_button.pack(expand=True, fill="x")
    #end init


    def _add_fleet(self):
        """Add a fleet to the current npc"""
        logging.debug("Adding CustomFleet...")

        cf = widgets.CustomFleetFrame(self, self.npc)
        self.edit_fleet(self.custom_fleet_frames[-1])

        state = BooleanVar()
        cb = ttk.Checkbutton(cf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_fleet_state, state, self.custom_fleet_frames[-1].custom_fleet))
        cb.grid(row=0, column=3, sticky="e")
    #end _add_fleet


    def edit_fleet(self, cf_frame):
        """
        This method uses the data stored in the cf_frame to edit the data stored in the associated
        CustomFleet object.

        :param cf_frame: The CustomFleetFrame containing the CustomFleet to be edited
        """
        logging.debug("Editing  %s" % str(cf_frame.custom_fleet))
        widgets.CustomFleetWindow(self, cf_frame.custom_fleet)
    #end edit_fleet


    def delete_fleet(self, cf_frame):
        """
        This method uses the data stored in the cf_frame to remove the associated CustomFleet object from the
        current npc. Once that is completed, it removes the cf_frame widget from the GUI.

        :param cf_frame: The CustomFleetFrame to be removed
        """
        self.npc.remove_(cf_frame.custom_fleet)
        self.custom_fleet_frames.remove(cf_frame)
        cf_frame.frame.pack_forget()
        cf_frame.frame.destroy()

        logging.debug("Removed %s from NPC" % cf_frame.custom_fleet)
    #end delete_fleet


    def populate_fleet(self, custom_fleet):
        """
        This method populates the GUI with a CustomFleetFrame widget, then populates the data from custom_fleet

        :param custom_fleet: the CustomFleet containing the data to be populated
        """
        cf = widgets.CustomFleetFrame(self, self.npc, populating=True)
        cf.custom_fleet = custom_fleet

        state = BooleanVar()
        cb = ttk.Checkbutton(cf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_fleet_state, state, cf))
        cb.grid(row=0, column=3, sticky="e")

        if custom_fleet.is_active:
            state.set(1)
            self._change_fleet_state(state, custom_fleet)
    #end populate_fleet


    @staticmethod
    def _change_fleet_state(state, custom_fleet):
        """
        Set tc to state

        :param state: the state of the custom fleet
        :param custom_fleet: the CustomFleet object to be modified
        """
        custom_fleet.is_active = state.get()
        logging.debug("%s is now %s", str(custom_fleet), str(custom_fleet.is_active))
    #def _change_fleet_state
#end class AggregatedCustomFleetFrame
