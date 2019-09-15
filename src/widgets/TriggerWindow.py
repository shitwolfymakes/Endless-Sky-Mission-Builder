""" TriggerWindow.py
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

from src.gui import build_mand_opt_frame
from src.widgets import AggregatedLogFrame, AggregatedTriggerConditionFrame


class TriggerWindow(object):
    """This class creates a custom pop-up window to display and edit the data in an associated Trigger object"""

    def __init__(self, app, master, trigger):
        logging.debug("\tBuilding TriggerWindow...")

        self.app = app
        self.trigger = trigger
        app.activeTrigger = trigger

        self.top = Toplevel(master)
        self.top.title("Edit Trigger")
        self.top.configure(bg="#ededed")
        self.top.grab_set()  # freezes the app until the user enters or cancels

        outer = ttk.Frame(self.top)
        outer.pack(side=TOP)

        self.leftFrame = ttk.Frame(outer)
        self.leftFrame.pack(side=LEFT)

        self.rightFrame = ttk.Frame(outer)
        self.rightFrame.pack(side=RIGHT, anchor=N)

        self.closeButton = ttk.Button(self.top, text="Ok", command=self._cleanup)
        self.closeButton.pack(side=BOTTOM)

        #TODO: find a way to support "on enter <system>"
        self.action = None
        self.actionsList = ["offer", "complete", "accept", "decline", "defer", "fail", "visit", "stopover"]

        ### BUILDING LEFT FRAME ###
        on_label = ttk.Label(self.leftFrame, text="on", width=6)
        on_label.grid(row=0, column=0, sticky="w", padx=(5, 0))

        self.onActionCombobox = ttk.Combobox(self.leftFrame, state="readonly", values=self.actionsList)
        self.onActionCombobox.bind("<<ComboboxSelected>>", self._action_selected)
        self.onActionCombobox.grid(row=0, column=1, sticky="ew")

        self.dialogSubComponent = build_mand_opt_frame(self.leftFrame, "dialog", 1, 0, ["<text>"])
        self.dialogSubComponent.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.outfitSubComponent = build_mand_opt_frame(self.leftFrame, "outfit", 1, 1, ["<outfit>", "[<number#>]"])
        self.outfitSubComponent.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.requireSubComponent = build_mand_opt_frame(self.leftFrame, "require", 1, 1, ["<outfit>", "[<number#>]"])
        self.requireSubComponent.grid(row=3, column=0, columnspan=2, sticky="ew")

        self.paymentSubComponent = build_mand_opt_frame(self.leftFrame, "payment", 0, 2, ["[<base#>]", "[<multiplier#>]"])
        self.paymentSubComponent.grid(row=4, column=0, columnspan=2, sticky="ew")

        self.eventSubComponent = build_mand_opt_frame(self.leftFrame, "event", 1, 2, ["<name>", "[<delay#>]", "[<max#>]"])
        self.eventSubComponent.grid(row=5, column=0, columnspan=2, sticky="ew")

        self.failSubComponent = build_mand_opt_frame(self.leftFrame, "fail", 0, 1, ["[<name>]"])
        self.failSubComponent.grid(row=6, column=0, columnspan=2, sticky="ew")

        self.logsSubComponent = AggregatedLogFrame(self.app, self.leftFrame, self.trigger)
        self.logsSubComponent.grid(row=7, column=0, columnspan=2, sticky="ew")

        ### BUILDING RIGHT FRAME###
        self.triggerConditionsSubComponent = AggregatedTriggerConditionFrame(self.app, self.rightFrame, self.trigger)
        self.triggerConditionsSubComponent.grid(row=0, column=0, columnspan=2, sticky="ew")

        self._populate_trigger_window()
    #end init


    def _action_selected(self, event=None):
        """Store the combobox option selected by the user"""
        self.action = self.onActionCombobox.get()
        logging.debug("\tTrigger action selected: \"on %s\"" % self.action)
    #end _action_selected


    def _cleanup(self):
        """Clean up whatever popups we've created"""
        self._store_data()
        self.app.activeTrigger = None
        self.top.grab_release()  # HAVE TO RELEASE
        self.top.destroy()
    #end _cleanup


    def _store_data(self):
        """Store the data from the GUI into the associated Trigger object"""
        logging.debug("\tStoring TriggerWindow data...")
        self.trigger.clear_trigger()

        # action
        if self.action is not None:
            logging.debug("\t\tOn: %s" % self.action)
            self.trigger.triggerType = self.action
        #end if

        # dialog
        if self.dialogSubComponent.listEntryStates[0].get():
            logging.debug("\t\tDialog: %s" % self.dialogSubComponent.listEntryData[0].get())
            self.trigger.dialog = self.dialogSubComponent.listEntryData[0].get()
        #end if

        # outfit
        if self.outfitSubComponent.listEntryStates[0].get():
            logging.debug("\t\tOutfit: %s" % self.outfitSubComponent.listEntryData[0].get())
            self.trigger.outfit[0] = self.outfitSubComponent.listEntryData[0].get()
            if self.outfitSubComponent.listEntryStates[1].get():
                logging.debug("\t\t\tOutfit Optional: %s" % self.outfitSubComponent.listEntryData[1].get())
                self.trigger.outfit[1] = self.outfitSubComponent.listEntryData[1].get()
            #end if
        #end if

        # require
        if self.requireSubComponent.listEntryStates[0].get():
            logging.debug("\t\tRequire: %s" % self.requireSubComponent.listEntryData[0].get())
            self.trigger.require[0] = self.requireSubComponent.listEntryData[0].get()
            if self.requireSubComponent.listEntryStates[1].get():
                logging.debug("\t\t\tRequire Optional: %s" % self.requireSubComponent.listEntryData[1].get())
                self.trigger.require[1] = self.requireSubComponent.listEntryData[1].get()
            # end if
        # end if

        # payment
        if self.paymentSubComponent.listEntryStates[0].get():
            logging.debug("\t\tPayment: %s" % self.paymentSubComponent.subComponentName)
            self.trigger.isPayment = True
            if self.paymentSubComponent.listEntryStates[1].get():
                logging.debug("\t\t\tPayment Optional 1: %s" % self.paymentSubComponent.listEntryData[0].get())
                self.trigger.payment[0] = self.paymentSubComponent.listEntryData[0].get()
                if self.paymentSubComponent.listEntryStates[2].get():
                    logging.debug("\t\t\tPayment Optional 2: %s" % self.paymentSubComponent.listEntryData[1].get())
                    self.trigger.payment[1] = self.paymentSubComponent.listEntryData[1].get()
                #end if
            #end if
        #end if

        # event
        if self.eventSubComponent.listEntryStates[0].get():
            logging.debug("\t\tEvent: %s" % self.eventSubComponent.listEntryData[0].get())
            self.trigger.event[0] = self.eventSubComponent.listEntryData[0].get()
            if self.eventSubComponent.listEntryStates[1].get():
                logging.debug("\t\t\tEvent Optional 1: %s" % self.eventSubComponent.listEntryData[1].get())
                self.trigger.event[1] = self.eventSubComponent.listEntryData[1].get()
                if self.eventSubComponent.listEntryStates[2].get():
                    logging.debug("\t\t\tEvent Optional 2: %s" % self.eventSubComponent.listEntryData[2].get())
                    self.trigger.event[2] = self.eventSubComponent.listEntryData[2].get()
                # end if
            # end if
        # end if

        # fail
        if self.failSubComponent.listEntryStates[0].get():
            logging.debug("\t\tPayment: %s" % self.failSubComponent.subComponentName)
            self.trigger.isFail = True
            if self.failSubComponent.listEntryStates[1].get():
                logging.debug("\t\t\tPayment Optional 1: %s" % self.failSubComponent.listEntryData[0].get())
                self.trigger.fail = self.failSubComponent.listEntryData[0].get()
            #end if
        #end if

        self.trigger.print_trigger()
    #end _store_data

    def _populate_trigger_window(self):
        """Take the associated Trigger object, and populate each of the widgets in the window with the data inside"""
        logging.debug("\t\tPopulating TriggerWindow...")

        # action
        if self.trigger.triggerType is not None:
            self.action = self.trigger.triggerType
            index = self.actionsList.index(self.trigger.triggerType)
            self.onActionCombobox.current(index)
        #end if

        # dialog
        component = self.dialogSubComponent
        if self.trigger.dialog is not None:
            component.listEntryStates[0].set(1)
            component.cb_value_changed(self.dialogSubComponent.listEntryStates[0], [self.dialogSubComponent.listEntries[0]])
            component.listEntryData[0].set(self.trigger.dialog.lstrip('`').rstrip('`'))
        #end if

        # outfit
        component = self.outfitSubComponent
        for i, data in enumerate(self.trigger.outfit):
            if data is not None:
                component.listEntryStates[i].set(1)
                component.cb_value_changed(component.listEntryStates[i], [component.listEntries[i]])
                component.listEntryData[i].set(data)
            #end if
        #end for

        # require
        component = self.requireSubComponent
        for i, data in enumerate(self.trigger.require):
            if data is not None:
                component.listEntryStates[i].set(1)
                component.cb_value_changed(component.listEntryStates[i], [component.listEntries[i]])
                component.listEntryData[i].set(data)
            #end if
        #end for

        # payment
        if self.trigger.isPayment:
            component = self.paymentSubComponent
            component.listEntryStates[0].set(1)
            component.cb_value_changed(component.listEntryStates[0], [component.subComponentName])

            for i, data in enumerate(self.trigger.payment):
                if data is not None:
                    component.listEntryStates[i+1].set(1)
                    component.cb_value_changed(component.listEntryStates[i + 1], [component.listEntries[i]])
                    component.listEntryData[i].set(data)
                # end if
            # end for
        #end if

        # event
        component = self.eventSubComponent
        for i, data in enumerate(self.trigger.event):
            if data is not None:
                component.listEntryStates[i].set(1)
                component.cb_value_changed(component.listEntryStates[i], [component.listEntries[i]])
                component.listEntryData[i].set(data)
            #end if
        #end for

        # fail
        component = self.failSubComponent
        if self.trigger.isFail:
            component.listEntryStates[0].set(1)
            component.cb_value_changed(component.listEntryStates[0], [component.subComponentName])

            if self.trigger.fail is not None:
                component.listEntryStates[1].set(1)
                component.cb_value_changed(component.listEntryStates[1], [component.listEntries[0]])
                component.listEntryData[0].set(self.trigger.fail)
            #end if
        #end if

        # Logs
        component = self.logsSubComponent
        if self.trigger.logs:
            for log in self.trigger.logs:
                component.populate_log(log)
        #end if

        # Conditions
        component = self.triggerConditionsSubComponent
        if self.trigger.conditions:
            for condition in self.trigger.conditions:
                component.populate_trigger_condition(condition)
        # end if
    #end _populate_trigger_window
#end class TriggerWindow
