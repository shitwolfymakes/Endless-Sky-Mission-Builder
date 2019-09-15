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

import src.widgets as widgets


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

        self.dialogComponent = widgets.ComponentMandOptFrame(self.leftFrame, "dialog", 1, 0, ["<text>"])
        self.dialogComponent.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.outfitComponent = widgets.ComponentMandOptFrame(self.leftFrame, "outfit", 1, 1, ["<outfit>", "[<number#>]"])
        self.outfitComponent.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.requireComponent = widgets.ComponentMandOptFrame(self.leftFrame, "require", 1, 1, ["<outfit>", "[<number#>]"])
        self.requireComponent.grid(row=3, column=0, columnspan=2, sticky="ew")

        self.paymentComponent = widgets.ComponentMandOptFrame(self.leftFrame, "payment", 0, 2, ["[<base#>]", "[<multiplier#>]"])
        self.paymentComponent.grid(row=4, column=0, columnspan=2, sticky="ew")

        self.eventComponent = widgets.ComponentMandOptFrame(self.leftFrame, "event", 1, 2, ["<name>", "[<delay#>]", "[<max#>]"])
        self.eventComponent.grid(row=5, column=0, columnspan=2, sticky="ew")

        self.failComponent = widgets.ComponentMandOptFrame(self.leftFrame, "fail", 0, 1, ["[<name>]"])
        self.failComponent.grid(row=6, column=0, columnspan=2, sticky="ew")

        self.logsComponent = widgets.AggregatedLogFrame(self.app, self.leftFrame, self.trigger)
        self.logsComponent.grid(row=7, column=0, columnspan=2, sticky="ew")

        ### BUILDING RIGHT FRAME###
        self.triggerConditionsSubComponent = widgets.AggregatedTriggerConditionFrame(self.app, self.rightFrame, self.trigger)
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
        if self.dialogComponent.listEntryStates[0].get():
            logging.debug("\t\tDialog: %s" % self.dialogComponent.listEntryData[0].get())
            self.trigger.dialog = self.dialogComponent.listEntryData[0].get()
        #end if

        # outfit
        if self.outfitComponent.listEntryStates[0].get():
            logging.debug("\t\tOutfit: %s" % self.outfitComponent.listEntryData[0].get())
            self.trigger.outfit[0] = self.outfitComponent.listEntryData[0].get()
            if self.outfitComponent.listEntryStates[1].get():
                logging.debug("\t\t\tOutfit Optional: %s" % self.outfitComponent.listEntryData[1].get())
                self.trigger.outfit[1] = self.outfitComponent.listEntryData[1].get()
            #end if
        #end if

        # require
        if self.requireComponent.listEntryStates[0].get():
            logging.debug("\t\tRequire: %s" % self.requireComponent.listEntryData[0].get())
            self.trigger.require[0] = self.requireComponent.listEntryData[0].get()
            if self.requireComponent.listEntryStates[1].get():
                logging.debug("\t\t\tRequire Optional: %s" % self.requireComponent.listEntryData[1].get())
                self.trigger.require[1] = self.requireComponent.listEntryData[1].get()
            # end if
        # end if

        # payment
        if self.paymentComponent.listEntryStates[0].get():
            logging.debug("\t\tPayment: %s" % self.paymentComponent.componentName)
            self.trigger.isPayment = True
            if self.paymentComponent.listEntryStates[1].get():
                logging.debug("\t\t\tPayment Optional 1: %s" % self.paymentComponent.listEntryData[0].get())
                self.trigger.payment[0] = self.paymentComponent.listEntryData[0].get()
                if self.paymentComponent.listEntryStates[2].get():
                    logging.debug("\t\t\tPayment Optional 2: %s" % self.paymentComponent.listEntryData[1].get())
                    self.trigger.payment[1] = self.paymentComponent.listEntryData[1].get()
                #end if
            #end if
        #end if

        # event
        if self.eventComponent.listEntryStates[0].get():
            logging.debug("\t\tEvent: %s" % self.eventComponent.listEntryData[0].get())
            self.trigger.event[0] = self.eventComponent.listEntryData[0].get()
            if self.eventComponent.listEntryStates[1].get():
                logging.debug("\t\t\tEvent Optional 1: %s" % self.eventComponent.listEntryData[1].get())
                self.trigger.event[1] = self.eventComponent.listEntryData[1].get()
                if self.eventComponent.listEntryStates[2].get():
                    logging.debug("\t\t\tEvent Optional 2: %s" % self.eventComponent.listEntryData[2].get())
                    self.trigger.event[2] = self.eventComponent.listEntryData[2].get()
                # end if
            # end if
        # end if

        # fail
        if self.failComponent.listEntryStates[0].get():
            logging.debug("\t\tPayment: %s" % self.failComponent.componentName)
            self.trigger.isFail = True
            if self.failComponent.listEntryStates[1].get():
                logging.debug("\t\t\tPayment Optional 1: %s" % self.failComponent.listEntryData[0].get())
                self.trigger.fail = self.failComponent.listEntryData[0].get()
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
        component = self.dialogComponent
        if self.trigger.dialog is not None:
            component.listEntryStates[0].set(1)
            component.cb_value_changed(self.dialogComponent.listEntryStates[0], [self.dialogComponent.listEntries[0]])
            component.listEntryData[0].set(self.trigger.dialog.lstrip('`').rstrip('`'))
        #end if

        # outfit
        component = self.outfitComponent
        for i, data in enumerate(self.trigger.outfit):
            if data is not None:
                component.listEntryStates[i].set(1)
                component.cb_value_changed(component.listEntryStates[i], [component.listEntries[i]])
                component.listEntryData[i].set(data)
            #end if
        #end for

        # require
        component = self.requireComponent
        for i, data in enumerate(self.trigger.require):
            if data is not None:
                component.listEntryStates[i].set(1)
                component.cb_value_changed(component.listEntryStates[i], [component.listEntries[i]])
                component.listEntryData[i].set(data)
            #end if
        #end for

        # payment
        if self.trigger.isPayment:
            component = self.paymentComponent
            component.listEntryStates[0].set(1)
            component.cb_value_changed(component.listEntryStates[0], [component.componentName])

            for i, data in enumerate(self.trigger.payment):
                if data is not None:
                    component.listEntryStates[i+1].set(1)
                    component.cb_value_changed(component.listEntryStates[i + 1], [component.listEntries[i]])
                    component.listEntryData[i].set(data)
                # end if
            # end for
        #end if

        # event
        component = self.eventComponent
        for i, data in enumerate(self.trigger.event):
            if data is not None:
                component.listEntryStates[i].set(1)
                component.cb_value_changed(component.listEntryStates[i], [component.listEntries[i]])
                component.listEntryData[i].set(data)
            #end if
        #end for

        # fail
        component = self.failComponent
        if self.trigger.isFail:
            component.listEntryStates[0].set(1)
            component.cb_value_changed(component.listEntryStates[0], [component.componentName])

            if self.trigger.fail is not None:
                component.listEntryStates[1].set(1)
                component.cb_value_changed(component.listEntryStates[1], [component.listEntries[0]])
                component.listEntryData[0].set(self.trigger.fail)
            #end if
        #end if

        # Logs
        component = self.logsComponent
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
