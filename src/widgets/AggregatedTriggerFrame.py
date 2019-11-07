""" AggregatedTriggerFrame.py
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
from functools import partial
from tkinter import *
from tkinter import ttk

import src.widgets as widgets
from src import config


class AggregatedTriggerFrame(ttk.Frame):
    """
    This class extends ttk.Frame, allowing the user to add an arbitrary number of TriggerFrame widgets to the GUI.
    """

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.parent = parent
        self.trigger_frame_list = []

        self.outer = ttk.Frame(self)
        self.outer.pack(expand=True, fill="x")

        section_name_label = ttk.Label(self.outer, text="Triggers", anchor="center")
        section_name_label.pack()

        self.inner = ttk.Frame(self.outer)
        self.inner.pack(expand=True, fill="x")

        add_button = ttk.Button(self.outer, text="Add Trigger", command=self._add_trigger)
        add_button.pack(expand=True, fill="x")
    #end init


    def _add_trigger(self):
        """Add a trigger to the activeMission"""
        logging.debug("Adding Trigger...")

        tf = widgets.TriggerFrame(self, "trigger")
        self.edit_trigger(self.trigger_frame_list[-1])

        state = BooleanVar()
        cb = ttk.Checkbutton(tf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_trigger_state, state, self.trigger_frame_list[-1].trigger))
        cb.grid(row=0, column=3, sticky="e")
    #end _add_trigger


    def delete_trigger(self, trigger_frame):
        """
        This method uses the data stored in the trigger_frame to remove the associated Trigger object from the
            activeMission. Once that is completed, it removes the trigger_frame TriggerFrame widget from the GUI.

        :param trigger_frame: The TriggerFrame to be removed
        """
        logging.debug(str.format("Removing %s from Triggers" % trigger_frame.trigger))

        config.active_item.remove_trigger(trigger_frame.trigger)

        self.trigger_frame_list.remove(trigger_frame)
        trigger_frame.frame.pack_forget()
        trigger_frame.frame.destroy()
    #end delete_trigger


    def edit_trigger(self, trigger_frame):
        """
        This method uses the data stored in the trigger_frame to edit the data stored in the associated
        Trigger object.

        :param trigger_frame: The TriggerFrame containing the trigger to be edited
        """
        logging.debug("Editing %s..." % str(trigger_frame.trigger))
        widgets.TriggerWindow(self, trigger_frame.trigger)
    #end edit_trigger


    def populate_trigger(self, trigger):
        """
        This method populates the GUI with a TriggerFrame widget, then stores the data from trigger inside it

        :param trigger: the trigger containing the data to be populated
        """
        tf = widgets.TriggerFrame(self, "trigger", populating=True)
        tf.trigger = trigger

        state = BooleanVar()
        cb = ttk.Checkbutton(tf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_trigger_state, state, trigger))
        cb.grid(row=0, column=3, sticky="e")

        if trigger.is_active:
            state.set(1)
            self._change_trigger_state(state, trigger)
    #end populate_trigger


    @staticmethod
    def _change_trigger_state(state, trigger):
        """
        Set trigger to state
        :param state: the state of the trigger
        :param trigger: the trigger
        """
        trigger.is_active = state.get()
        logging.debug("%s is now %s" % (str(trigger), str(trigger.is_active)))
    #def _change_trigger_state
#end class AggregatedTriggerFrame
