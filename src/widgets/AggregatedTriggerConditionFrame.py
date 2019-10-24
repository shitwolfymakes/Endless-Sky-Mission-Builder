""" AggregatedTriggerConditionFrame.py
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

from src import widgets as widgets


class AggregatedTriggerConditionFrame(ttk.Frame):
    """
    This class extends ttk.Frame, allowing the user to add an arbitrary
    number of TriggerConditionFrame widgets to the GUI.
    """

    def __init__(self, parent, trigger):
        ttk.Frame.__init__(self, parent)

        self.parent = parent
        self.trigger = trigger
        self.tc_frame_list = []

        self.outer = ttk.Frame(self)
        self.outer.pack(expand=True, fill="x")

        section_name_label = ttk.Label(self.outer, text="Conditions", anchor="center")
        section_name_label.pack()

        self.inner = ttk.Frame(self.outer)
        self.inner.pack(expand=True, fill="x")

        add_button = ttk.Button(self.outer, text="Add Condition", command=self._add_trigger_condition)
        add_button.pack(expand=True, fill="x")
    #end init


    def _add_trigger_condition(self):
        """Add a condition to the current trigger"""
        logging.debug("Adding TriggerCondition...")

        tc = widgets.TriggerConditionFrame(self, self.trigger, "log")
        self.condTypes = ["<condition> (= | += | -=) <value>", "<condition> (++ | --)", "(set | clear) <condition>"]
        widgets.TypeSelectorWindow(self, self.condTypes, self._set_format_type)

        if tc.condition.conditionType == "cancelled":
            tc.cleanup()
            return
        #end if
        self.edit_trigger_condition(self.tc_frame_list[-1])


        state = BooleanVar()
        cb = ttk.Checkbutton(tc.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_tc_state, state, self.tc_frame_list[-1].condition))
        cb.grid(row=0, column=3, sticky="e")
    #end _add_trigger_condition


    def edit_trigger_condition(self, tc_frame):
        """
        This method uses the data stored in the tc_frame to edit the data stored in the associated
        TriggerCondition object.

        :param tc_frame: The TriggerConditionFrame containing the condition to be edited
        """
        logging.debug("Editing  %s" % str(tc_frame.condition))
        widgets.TriggerConditionWindow(tc_frame.condition)
    #end edit_trigger_condition


    def delete_trigger_condition(self, tc_frame):
        """
        This method uses the data stored in the tc_frame to remove the associated TriggerCondition object from the
        current trigger. Once that is completed, it removes the tc_frame widget from the GUI.

        :param tc_frame: The TriggerConditionFrame to be removed
        """
        self.trigger.remove_tc(tc_frame.condition)
        self.tc_frame_list.remove(tc_frame)
        tc_frame.frame.pack_forget()
        tc_frame.frame.destroy()

        logging.debug("Removed %s from Triggers" % tc_frame.condition)
    #end delete_trigger_condition


    def populate_trigger_condition(self, condition):
        """
        This method populates the GUI with a TriggerConditionFrame widget, then stores the data from condition inside it

        :param condition: the TriggerCondition containing the data to be populated
        """
        tc = widgets.TriggerConditionFrame(self, self.trigger, "log", populating=True)
        tc.condition = condition

        state = BooleanVar()
        cb = ttk.Checkbutton(tc.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_tc_state, state, tc))
        cb.grid(row=0, column=3, sticky="e")

        if condition.isActive:
            state.set(1)
            self._change_tc_state(state, condition)
    #end populate_trigger_condition


    @staticmethod
    def _change_tc_state(state, tc):
        """
        Set tc to state

        :param state: the state of the condition
        :param tc: the trigger condition
        """
        tc.isActive = state.get()
        logging.debug("%s is now %s", str(tc), str(tc.isActive))
    #def changeTriggerConditionsState


    def _set_format_type(self, format_type):
        """
        Set the format of the condition, so the code knows what to look for

        :param format_type: the format type
        """
        if format_type == "cancelled":
            self.tc_frame_list[-1].condition.conditionType = "cancelled"
            return
        ft = self.condTypes.index(format_type)
        self.tc_frame_list[-1].condition.conditionType = ft
    #end _set_format_type
#end class AggregatedTriggerConditionFrame
