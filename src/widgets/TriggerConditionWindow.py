""" TriggerConditionWindow.py
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
from tkinter import *
from tkinter import ttk

from ttkthemes import ThemedTk

import src.widgets as widgets


class TriggerConditionWindow(Toplevel):
    """
    This class creates a custom pop-up window to display and edit the data in an associated TriggerCondition object
    """

    def __init__(self, master, condition):
        logging.debug("\tBuilding TriggerConditionWindow...")
        super().__init__(master)

        self.condition = condition
        self.condition_type = condition.condition_type
        self.cond_data = StringVar()
        self.value = StringVar()
        self.selected_option = None

        self.title("Edit Condition")
        self.configure(bg="#ededed")
        self.grab_set()  # freezes the app until the user enters or cancels

        frame = ttk.Frame(self)
        frame.pack(side=TOP)
        self.options_combo = ttk.Combobox(frame, state="readonly")
        self.options_combo.bind("<<ComboboxSelected>>", self._combo_callback)

        self.cond_data.set("<condition>")
        if self.condition_type == 0:
            label = widgets.TooltipLabel(frame, "trigger_condition_0", text="Log")
            label.grid(row=0, column=0)
            entry = ttk.Entry(frame, textvariable=self.cond_data)
            entry.grid(row=1, column=0)

            self.selected_option = "="
            self.combo_options = ["=", "+=", "-="]
            self.options_combo.configure(values=self.combo_options, width=5)
            self.options_combo.current(0)
            self.options_combo.grid(row=1, column=1)
            self.value.set("<value>")

            entry2 = ttk.Entry(frame, textvariable=self.value, width=6)
            entry2.grid(row=1, column=2)
        elif self.condition_type == 1:
            label = widgets.TooltipLabel(frame, "trigger_condition_1", text="Log")
            label.grid(row=0, column=0)
            entry = ttk.Entry(frame, textvariable=self.cond_data)
            entry.grid(row=1, column=0)

            self.selected_option = "++"
            self.combo_options = ["++", "--"]
            self.options_combo.configure(values=self.combo_options, width=5)
            self.options_combo.current(0)
            self.options_combo.grid(row=1, column=1)
        elif self.condition_type == 2:
            label = widgets.TooltipLabel(frame, "trigger_condition_2", text="Log")
            label.grid(row=0, column=0)

            self.selected_option = "set"
            self.combo_options = ["set", "clear"]
            self.options_combo.configure(values=self.combo_options, width=5)
            self.options_combo.current(0)
            self.options_combo.grid(row=1, column=0)

            entry = ttk.Entry(frame, textvariable=self.cond_data)
            entry.grid(row=1, column=1)
        else:
            logging.error("Invalid condition_type!!")
        #end if/else

        self.closeButton = ttk.Button(self, text="Ok", command=self.cleanup)
        self.closeButton.pack(side=BOTTOM)

        self._populate_tc_window()
    #end init


    def cleanup(self):
        """Clean up whatever popups we've created"""
        self._store_data()
        self.grab_release()  # HAVE TO RELEASE
        self.destroy()
    #end _cleanup


    def _store_data(self):
        """Store the data from the GUI into the associated Log object"""
        logging.debug("\t\tStoring TriggerConditionWindow data...")
        self.condition.clear_condition()

        if self.condition_type == 0:
            self.condition.condition[0] = self.cond_data.get()
            self.condition.condition[1] = self.selected_option
            self.condition.condition[2] = self.value.get()
            logging.debug("\t\t\tCondition type %d: %s" % (self.condition_type, str(self.condition.condition)))
        elif self.condition_type == 1:
            self.condition.condition[0] = self.cond_data.get()
            self.condition.condition[1] = self.selected_option
            logging.debug("\t\t\tCondition type %d: %s" % (self.condition_type, str(self.condition.condition)))
        elif self.condition_type == 2:
            self.condition.condition[0] = self.selected_option
            self.condition.condition[1] = self.cond_data.get()
            logging.debug("\t\t\tCondition type %d: %s" % (self.condition_type, str(self.condition.condition)))
        else:
            logging.error("Invalid TriggerCondition condition_type!!!")
        #end if/else
    #end _store_data


    def _populate_tc_window(self):
        """
        Take the associated TriggerCondition object, and populate
        each of the widgets in the window with the data inside
        """
        logging.debug("\t\tPopulating TriggerWindow...")

        if self.condition_type == 0:
            if self.condition.condition[0] is not None:
                self.cond_data.set(self.condition.condition[0])
                index = self.combo_options.index(self.condition.condition[1])
                self.options_combo.current(index)
                self.value.set(self.condition.condition[2])

                self.selected_option = self.condition.condition[1]
            #end if
        elif self.condition_type == 1:
            if self.condition.condition[0] is not None:
                self.cond_data.set(self.condition.condition[0])
                index = self.combo_options.index(self.condition.condition[1])
                self.options_combo.current(index)

                self.selected_option = self.condition.condition[1]
            #end if
        elif self.condition_type == 2:
            if self.condition.condition[0] is not None:
                index = self.combo_options.index(self.condition.condition[0])
                self.options_combo.current(index)
                self.cond_data.set(self.condition.condition[1])

                self.selected_option = self.condition.condition[0]
            #end if
        else:
            logging.error("Data corrupted!!!")
        #end if/else
    #end _populate_log_window


    def _combo_callback(self, event=None):
        """Store the combobox option selected by the user"""
        self.selected_option = self.options_combo.get()
    #end _combo_callback
#end class TriggerConditionWindow
