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

import src.widgets as widgets


class TriggerConditionWindow(object):
    """
    This class creates a custom pop-up window to display and edit the data in an associated TriggerCondition object
    """

    def __init__(self, app, master, condition):
        logging.debug("\tBuilding TriggerConditionWindow...")

        self.app            = app
        self.condition      = condition
        self.conditionType  = condition.conditionType
        self.condData       = StringVar()
        self.value          = StringVar()
        self.selectedOption = None

        self.top = Toplevel(master)
        self.top.title("Edit Condition")
        self.top.configure(bg="#ededed")
        self.top.grab_set()  # freezes the app until the user enters or cancels

        frame = ttk.Frame(self.top)
        frame.pack(side=TOP)
        self.optionsCombo  = ttk.Combobox(frame, state="readonly")
        self.optionsCombo.bind("<<ComboboxSelected>>", self._combo_callback)

        self.condData.set("<condition>")
        if self.conditionType == 0:
            label = widgets.TooltipLabel(frame, "trigger_condition_0", text="Log")
            label.grid(row=0, column=0)
            entry = ttk.Entry(frame, textvariable=self.condData)
            entry.grid(row=1, column=0)

            self.selectedOption = "="
            self.comboOptions = ["=", "+=", "-="]
            self.optionsCombo.configure(values=self.comboOptions, width=5)
            self.optionsCombo.current(0)
            self.optionsCombo.grid(row=1, column=1)
            self.value.set("<value>")

            entry2 = ttk.Entry(frame, textvariable=self.value, width=6)
            entry2.grid(row=1, column=2)
        elif self.conditionType == 1:
            label = widgets.TooltipLabel(frame, "trigger_condition_1", text="Log")
            label.grid(row=0, column=0)
            entry = ttk.Entry(frame, textvariable=self.condData)
            entry.grid(row=1, column=0)

            self.selectedOption = "++"
            self.comboOptions = ["++", "--"]
            self.optionsCombo.configure(values=self.comboOptions, width=5)
            self.optionsCombo.current(0)
            self.optionsCombo.grid(row=1, column=1)
        elif self.conditionType == 2:
            label = widgets.TooltipLabel(frame, "trigger_condition_2", text="Log")
            label.grid(row=0, column=0)

            self.selectedOption = "set"
            self.comboOptions = ["set", "clear"]
            self.optionsCombo.configure(values=self.comboOptions, width=5)
            self.optionsCombo.current(0)
            self.optionsCombo.grid(row=1, column=0)

            entry = ttk.Entry(frame, textvariable=self.condData)
            entry.grid(row=1, column=1)
        else:
            logging.error("Invalid conditionType!!")
        #end if/else

        self.closeButton = ttk.Button(self.top, text="Ok", command=self.cleanup)
        self.closeButton.pack(side=BOTTOM)

        self._populate_tc_window()
    #end init


    def cleanup(self):
        """Clean up whatever popups we've created"""
        self._store_data()
        self.top.grab_release()  # HAVE TO RELEASE
        self.top.destroy()
    #end _cleanup


    def _store_data(self):
        """Store the data from the GUI into the associated Log object"""
        logging.debug("\t\tStoring TriggerConditionWindow data...")
        self.condition.clear_condition()

        if self.conditionType == 0:
            self.condition.condition[0] = self.condData.get()
            self.condition.condition[1] = self.selectedOption
            self.condition.condition[2] = self.value.get()
            logging.debug("\t\t\tCondition type %d: %s" % (self.conditionType, str(self.condition.condition)))
        elif self.conditionType == 1:
            self.condition.condition[0] = self.condData.get()
            self.condition.condition[1] = self.selectedOption
            logging.debug("\t\t\tCondition type %d: %s" % (self.conditionType, str(self.condition.condition)))
        elif self.conditionType == 2:
            self.condition.condition[0] = self.selectedOption
            self.condition.condition[1] = self.condData.get()
            logging.debug("\t\t\tCondition type %d: %s" % (self.conditionType, str(self.condition.condition)))
        else:
            logging.error("Invalid TriggerCondition conditionType!!!")
        #end if/else
    #end _store_data


    def _populate_tc_window(self):
        """
        Take the associated TriggerCondition object, and populate
        each of the widgets in the window with the data inside
        """
        logging.debug("\t\tPopulating TriggerWindow...")

        if self.conditionType == 0:
            if self.condition.condition[0] is not None:
                self.condData.set(self.condition.condition[0])
                index = self.comboOptions.index(self.condition.condition[1])
                self.optionsCombo.current(index)
                self.value.set(self.condition.condition[2])

                self.selectedOption = self.condition.condition[1]
            #end if
        elif self.conditionType == 1:
            if self.condition.condition[0] is not None:
                self.condData.set(self.condition.condition[0])
                index = self.comboOptions.index(self.condition.condition[1])
                self.optionsCombo.current(index)

                self.selectedOption = self.condition.condition[1]
            #end if
        elif self.conditionType == 2:
            if self.condition.condition[0] is not None:
                index = self.comboOptions.index(self.condition.condition[0])
                self.optionsCombo.current(index)
                self.condData.set(self.condition.condition[1])

                self.selectedOption = self.condition.condition[0]
            #end if
        else:
            logging.error("Data corrupted!!!")
        #end if/else
    #end _populate_log_window


    def _combo_callback(self, event=None):
        """Store the combobox option selected by the user"""
        self.selectedOption = self.optionsCombo.get()
    #end _combo_callback
#end class TriggerConditionWindow
