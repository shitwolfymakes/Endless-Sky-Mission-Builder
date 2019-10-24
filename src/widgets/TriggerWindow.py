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

from ttkthemes import ThemedTk

import src.widgets as widgets
from src import config


class TriggerWindow(object):
    """This class creates a custom pop-up window to display and edit the data in an associated Trigger object"""

    def __init__(self, trigger):
        logging.debug("\tBuilding TriggerWindow...")

        self.trigger = trigger
        config.active_trigger = trigger

        self.top = ThemedTk(theme="plastik")
        self.top.title("Edit Trigger")
        self.top.configure(bg="#ededed")
        self.top.grab_set()  # freezes the app until the user enters or cancels

        outer = ttk.Frame(self.top)
        outer.pack(side=TOP)

        self.left_frame = ttk.Frame(outer)
        self.left_frame.pack(side=LEFT)

        self.right_frame = ttk.Frame(outer)
        self.right_frame.pack(side=RIGHT, anchor=N)

        self.close_button = ttk.Button(self.top, text="Ok", command=self._cleanup)
        self.close_button.pack(side=BOTTOM)

        #TODO: find a way to support "on enter <system>"
        self.action = None
        self.actions_list = ["offer", "complete", "accept", "decline", "defer", "fail", "visit", "stopover"]

        ### BUILDING LEFT FRAME ###
        on_label = widgets.TooltipLabel(self.left_frame, "trigger_on_action", text="on", width=6)
        on_label.grid(row=0, column=0, sticky="w", padx=(5, 0))

        self.on_action_combobox = ttk.Combobox(self.left_frame, state="readonly", values=self.actions_list)
        self.on_action_combobox.bind("<<ComboboxSelected>>", self._action_selected)
        self.on_action_combobox.grid(row=0, column=1, sticky="ew")

        self.dialog_component = widgets.ComponentMandOptFrame(self.left_frame, "dialog", 1, 0, ["<text>"], "trigger_dialog")
        self.dialog_component.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.outfit_component = widgets.ComponentMandOptFrame(self.left_frame, "outfit", 1, 1, ["<outfit>", "[<number#>]"], "trigger_outfit")
        self.outfit_component.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.require_component = widgets.ComponentMandOptFrame(self.left_frame, "require", 1, 1, ["<outfit>", "[<number#>]"], "trigger_require")
        self.require_component.grid(row=3, column=0, columnspan=2, sticky="ew")

        self.payment_component = widgets.ComponentMandOptFrame(self.left_frame, "payment", 0, 2, ["[<base#>]", "[<multiplier#>]"], "trigger_payment")
        self.payment_component.grid(row=4, column=0, columnspan=2, sticky="ew")

        self.event_component = widgets.ComponentMandOptFrame(self.left_frame, "event", 1, 2, ["<name>", "[<delay#>]", "[<max#>]"], "trigger_event")
        self.event_component.grid(row=5, column=0, columnspan=2, sticky="ew")

        self.fail_component = widgets.ComponentMandOptFrame(self.left_frame, "fail", 0, 1, ["[<name>]"], "trigger_fail")
        self.fail_component.grid(row=6, column=0, columnspan=2, sticky="ew")

        self.logs_component = widgets.AggregatedLogFrame(self.left_frame, self.trigger)
        self.logs_component.grid(row=7, column=0, columnspan=2, sticky="ew")

        ### BUILDING RIGHT FRAME###
        self.trigger_conditions_sub_component = widgets.AggregatedTriggerConditionFrame(self.right_frame, self.trigger)
        self.trigger_conditions_sub_component.grid(row=0, column=0, columnspan=2, sticky="ew")

        self._populate_trigger_window()
    #end init


    def _action_selected(self, event=None):
        """Store the combobox option selected by the user"""
        self.action = self.on_action_combobox.get()
        logging.debug("\tTrigger action selected: \"on %s\"" % self.action)
    #end _action_selected


    def _cleanup(self):
        """Clean up whatever popups we've created"""
        self._store_data()
        config.active_trigger = None
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
            self.trigger.trigger_type = self.action
        #end if

        # dialog
        if self.dialog_component.listEntryStates[0].get():
            logging.debug("\t\tDialog: %s" % self.dialog_component.listEntryData[0].get())
            self.trigger.dialog = self.dialog_component.listEntryData[0].get()
        #end if

        # outfit
        if self.outfit_component.listEntryStates[0].get():
            logging.debug("\t\tOutfit: %s" % self.outfit_component.listEntryData[0].get())
            self.trigger.outfit[0] = self.outfit_component.listEntryData[0].get()
            if self.outfit_component.listEntryStates[1].get():
                logging.debug("\t\t\tOutfit Optional: %s" % self.outfit_component.listEntryData[1].get())
                self.trigger.outfit[1] = self.outfit_component.listEntryData[1].get()
            #end if
        #end if

        # require
        if self.require_component.listEntryStates[0].get():
            logging.debug("\t\tRequire: %s" % self.require_component.listEntryData[0].get())
            self.trigger.require[0] = self.require_component.listEntryData[0].get()
            if self.require_component.listEntryStates[1].get():
                logging.debug("\t\t\tRequire Optional: %s" % self.require_component.listEntryData[1].get())
                self.trigger.require[1] = self.require_component.listEntryData[1].get()
            # end if
        # end if

        # payment
        if self.payment_component.listEntryStates[0].get():
            logging.debug("\t\tPayment: %s" % self.payment_component.componentName)
            self.trigger.is_payment = True
            if self.payment_component.listEntryStates[1].get():
                logging.debug("\t\t\tPayment Optional 1: %s" % self.payment_component.listEntryData[0].get())
                self.trigger.payment[0] = self.payment_component.listEntryData[0].get()
                if self.payment_component.listEntryStates[2].get():
                    logging.debug("\t\t\tPayment Optional 2: %s" % self.payment_component.listEntryData[1].get())
                    self.trigger.payment[1] = self.payment_component.listEntryData[1].get()
                #end if
            #end if
        #end if

        # event
        if self.event_component.listEntryStates[0].get():
            logging.debug("\t\tEvent: %s" % self.event_component.listEntryData[0].get())
            self.trigger.event[0] = self.event_component.listEntryData[0].get()
            if self.event_component.listEntryStates[1].get():
                logging.debug("\t\t\tEvent Optional 1: %s" % self.event_component.listEntryData[1].get())
                self.trigger.event[1] = self.event_component.listEntryData[1].get()
                if self.event_component.listEntryStates[2].get():
                    logging.debug("\t\t\tEvent Optional 2: %s" % self.event_component.listEntryData[2].get())
                    self.trigger.event[2] = self.event_component.listEntryData[2].get()
                # end if
            # end if
        # end if

        # fail
        if self.fail_component.listEntryStates[0].get():
            logging.debug("\t\tPayment: %s" % self.fail_component.componentName)
            self.trigger.is_fail = True
            if self.fail_component.listEntryStates[1].get():
                logging.debug("\t\t\tPayment Optional 1: %s" % self.fail_component.listEntryData[0].get())
                self.trigger.fail = self.fail_component.listEntryData[0].get()
            #end if
        #end if

        self.trigger.print_trigger()
    #end _store_data

    def _populate_trigger_window(self):
        """Take the associated Trigger object, and populate each of the widgets in the window with the data inside"""
        logging.debug("\t\tPopulating TriggerWindow...")

        # action
        if self.trigger.trigger_type is not None:
            self.action = self.trigger.trigger_type
            index = self.actions_list.index(self.trigger.trigger_type)
            self.on_action_combobox.current(index)
        #end if

        # dialog
        component = self.dialog_component
        if self.trigger.dialog is not None:
            component.listEntryStates[0].set(1)
            component.cb_value_changed(self.dialog_component.listEntryStates[0], [self.dialog_component.listEntries[0]])
            component.listEntryData[0].set(self.trigger.dialog.lstrip('`').rstrip('`'))
        #end if

        # outfit
        component = self.outfit_component
        for i, data in enumerate(self.trigger.outfit):
            if data is not None:
                component.listEntryStates[i].set(1)
                component.cb_value_changed(component.listEntryStates[i], [component.listEntries[i]])
                component.listEntryData[i].set(data)
            #end if
        #end for

        # require
        component = self.require_component
        for i, data in enumerate(self.trigger.require):
            if data is not None:
                component.listEntryStates[i].set(1)
                component.cb_value_changed(component.listEntryStates[i], [component.listEntries[i]])
                component.listEntryData[i].set(data)
            #end if
        #end for

        # payment
        if self.trigger.is_payment:
            component = self.payment_component
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
        component = self.event_component
        for i, data in enumerate(self.trigger.event):
            if data is not None:
                component.listEntryStates[i].set(1)
                component.cb_value_changed(component.listEntryStates[i], [component.listEntries[i]])
                component.listEntryData[i].set(data)
            #end if
        #end for

        # fail
        component = self.fail_component
        if self.trigger.is_fail:
            component.listEntryStates[0].set(1)
            component.cb_value_changed(component.listEntryStates[0], [component.componentName])

            if self.trigger.fail is not None:
                component.listEntryStates[1].set(1)
                component.cb_value_changed(component.listEntryStates[1], [component.listEntries[0]])
                component.listEntryData[0].set(self.trigger.fail)
            #end if
        #end if

        # Logs
        component = self.logs_component
        if self.trigger.logs:
            for log in self.trigger.logs:
                component.populate_log(log)
        #end if

        # Conditions
        component = self.trigger_conditions_sub_component
        if self.trigger.conditions:
            for condition in self.trigger.conditions:
                component.populate_trigger_condition(condition)
        # end if
    #end _populate_trigger_window
#end class TriggerWindow
