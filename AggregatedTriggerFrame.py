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

This library contains classes and methods that extend ttk widgets
"""

from guiutils import *


class AggregatedTriggerFrame(ttk.Frame):
    """
    This class extends ttk.Frame, allowing the user to add an arbitrary number of TriggerFrame widgets to the GUI.
    """

    def __init__(self, app, parent):
        ttk.Frame.__init__(self, parent)

        self.app              = app
        self.parent           = parent
        self.triggerFrameList = []

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
        print("Adding Trigger...")

        tf = TriggerFrame(self, self.app, "trigger")
        self.edit_trigger(self.triggerFrameList[-1])

        state = BooleanVar()
        cb = ttk.Checkbutton(tf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_trigger_state, state, self.triggerFrameList[-1].trigger))
        cb.grid(row=0, column=3, sticky="e")

        print("Done.")
    #end _add_trigger


    def delete_trigger(self, trigger_frame):
        """
        This method uses the data stored in the trigger_frame to remove the associated Trigger object from the
            activeMission. Once that is completed, it removes the trigger_frame TriggerFrame widget from the GUI.

        :param trigger_frame: The TriggerFrame to be removed
        """
        print("Removing %s from Triggers" % trigger_frame.trigger)

        self.app.activeMission.remove_trigger(trigger_frame.trigger)

        self.triggerFrameList.remove(trigger_frame)
        trigger_frame.frame.pack_forget()
        trigger_frame.frame.destroy()

        print("Done.")
    #end delete_trigger


    def edit_trigger(self, trigger_frame):
        """
        This method uses the data stored in the trigger_frame to edit the data stored in the associated
        Trigger object.

        :param trigger_frame: The TriggerFrame containing the trigger to be edited
        """
        print("Editing ", end="")
        print(trigger_frame.trigger, end="")
        print("...")

        TriggerWindow(self.app, self.app.gui, trigger_frame.trigger)
    #end edit_trigger


    def populate_trigger(self, trigger):
        """
        This method populates the GUI with a TriggerFrame widget, then stores the data from trigger inside it

        :param trigger: the trigger containing the data to be populated
        """
        tf = TriggerFrame(self, self.app, "trigger", populating=True)
        tf.trigger = trigger

        state = BooleanVar()
        cb = ttk.Checkbutton(tf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_trigger_state, state, trigger))
        cb.grid(row=0, column=3, sticky="e")

        if trigger.isActive:
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
        trigger.isActive = state.get()
        print(trigger, "is now", trigger.isActive)
    #def _change_trigger_state

#end class AggregatedTriggerFrame


class TriggerFrame(ttk.Frame):
    """This class extends ttk.Frame to create a custom GUI widget"""

    def __init__(self, master, app, name, populating=False):
        ttk.Frame.__init__(self, master)
        self.trigger = None
        if not populating:
            self.trigger = app.activeMission.add_trigger()
        self.master  = master

        self.frame = ttk.Frame(master.inner)
        self.frame.pack(expand=True, fill="x")
        self.frame.grid_columnconfigure(0, weight=1)

        name = name.title()
        label = ttk.Label(self.frame, text=name)
        label.grid(row=0, column=0, sticky="ew", padx=(5, 0))

        self.master.triggerFrameList.append(self)

        edit_button = ttk.Button(self.frame, text="edit", width=3, command=partial(self.master.edit_trigger, self))
        edit_button.grid(row=0, column=1)

        delete_button = ttk.Button(self.frame, text="X", width=0, command=partial(self.master.delete_trigger, self))
        delete_button.grid(row=0, column=2)
    #end init

    def _cleanup(self):
        self.master.delete_trigger(self)
    #end _cleanup

#end class TriggerFrame


class TriggerWindow(object):
    """This class creates a custom pop-up window to display and edit the data in an associated Trigger object"""

    def __init__(self, app, master, trigger):
        print("\tBuilding TriggerWindow...")

        self.app          = app
        self.trigger      = trigger
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

        # declare all the variables in one place

        #TODO: find a way to support "on enter <system>"
        self.action = None
        self.actionsList = ["offer", "complete", "accept", "decline", "defer", "fail", "visit", "stopover"]

        ### BUILDING LEFT FRAME ###

        ## on action
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

        ### DONE BUILDING LEFT FRAME ###

        ### BUILDING RIGHT FRAME###

        # Conditions (inside Trigger)
        self.triggerConditionsSubComponent = AggregatedTriggerConditionsFrame(self.app, self.rightFrame, self.trigger)
        self.triggerConditionsSubComponent.grid(row=0, column=0, columnspan=2, sticky="ew")

        self._populate_trigger_window()

        print("\tDone.")
    #end init


    def _action_selected(self, event=None):
        """Store the combobox option selected by the user"""
        self.action = self.onActionCombobox.get()
        print('\nTrigger action selected: "on %s"' % self.action)
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
        print("\nStoring TriggerWindow data...")
        self.trigger.clear_trigger()

        # action
        if self.action is not None:
            print("\tOn:", self.action)
            self.trigger.triggerType = self.action
        #end if

        # dialog
        if self.dialogSubComponent.listEntryStates[0].get():
            print("\tDialog:", self.dialogSubComponent.listEntryData[0].get())
            self.trigger.dialog = self.dialogSubComponent.listEntryData[0].get()
        #end if

        # outfit
        if self.outfitSubComponent.listEntryStates[0].get():
            print("\tOutfit:", self.outfitSubComponent.listEntryData[0].get())
            self.trigger.outfit[0] = self.outfitSubComponent.listEntryData[0].get()
            if self.outfitSubComponent.listEntryStates[1].get():
                print("\tOutfit Optional:", self.outfitSubComponent.listEntryData[1].get())
                self.trigger.outfit[1] = self.outfitSubComponent.listEntryData[1].get()
            #end if
        #end if

        # require
        if self.requireSubComponent.listEntryStates[0].get():
            print("\tRequire:", self.requireSubComponent.listEntryData[0].get())
            self.trigger.require[0] = self.requireSubComponent.listEntryData[0].get()
            if self.requireSubComponent.listEntryStates[1].get():
                print("\tRequire Optional:", self.requireSubComponent.listEntryData[1].get())
                self.trigger.require[1] = self.requireSubComponent.listEntryData[1].get()
            # end if
        # end if

        # payment
        if self.paymentSubComponent.listEntryStates[0].get():
            print("\tPayment:", self.paymentSubComponent.subComponentName)
            self.trigger.isPayment = True
            if self.paymentSubComponent.listEntryStates[1].get():
                print("\tPayment Optional 1:", self.paymentSubComponent.listEntryData[0].get())
                self.trigger.payment[0] = self.paymentSubComponent.listEntryData[0].get()
                if self.paymentSubComponent.listEntryStates[2].get():
                    print("\tPayment Optional 2:", self.paymentSubComponent.listEntryData[1].get())
                    self.trigger.payment[1] = self.paymentSubComponent.listEntryData[1].get()
                #end if
            #end if
        #end if

        # event
        if self.eventSubComponent.listEntryStates[0].get():
            print("\tEvent:", self.eventSubComponent.listEntryData[0].get())
            self.trigger.event[0] = self.eventSubComponent.listEntryData[0].get()
            if self.eventSubComponent.listEntryStates[1].get():
                print("\tEvent Optional 1:", self.eventSubComponent.listEntryData[1].get())
                self.trigger.event[1] = self.eventSubComponent.listEntryData[1].get()
                if self.eventSubComponent.listEntryStates[2].get():
                    print("\tEvent Optional 2:", self.eventSubComponent.listEntryData[2].get())
                    self.trigger.event[2] = self.eventSubComponent.listEntryData[2].get()
                # end if
            # end if
        # end if

        # fail
        if self.failSubComponent.listEntryStates[0].get():
            print("\tPayment:", self.failSubComponent.subComponentName)
            self.trigger.isFail = True
            if self.failSubComponent.listEntryStates[1].get():
                print("\tPayment Optional 1:", self.failSubComponent.listEntryData[0].get())
                self.trigger.fail = self.failSubComponent.listEntryData[0].get()
            #end if
        #end if

        self.trigger.print_trigger()

        print("Done.")
    #end _store_data

    def _populate_trigger_window(self):
        """Take the associated Trigger object, and populate each of the widgets in the window with the data inside"""
        print("\t\tPopulating TriggerWindow...", end="\t")

        # action
        if self.trigger.triggerType is not None:
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
            #print
        #end if

        # Conditions
        component = self.triggerConditionsSubComponent
        if self.trigger.conditions:
            for condition in self.trigger.conditions:
                component.populate_trigger_condition(condition)
            # print
        # end if

        print("Done.")
    #end _populate_trigger_window

#end class TriggerWindow


class AggregatedLogFrame(ttk.Frame):
    """This class extends ttk.Frame, allowing the user to add an arbitrary number of LogFrame widgets to the GUI."""

    def __init__(self, app, parent, trigger):
        ttk.Frame.__init__(self, parent)

        self.app          = app
        self.parent       = parent
        self.trigger      = trigger
        self.logFrameList = []

        self.outer = ttk.Frame(self)
        self.outer.pack(expand=True, fill="x")

        section_name_label = ttk.Label(self.outer, text="Logs", anchor="center")
        section_name_label.pack()

        self.inner = ttk.Frame(self.outer)
        self.inner.pack(expand=True, fill="x")

        add_button = ttk.Button(self.outer, text="Add Log", command=self._add_log)
        add_button.pack(expand=True, fill="x")
    #end init


    def _add_log(self):
        """
        Add a log to the current trigger. We can assume a specific trigger because these functions are only accessible
        after has opened the trigger they are adding this log to.
        """
        print("Adding Trigger...")

        lf = LogFrame(self, self.trigger, "log")
        TypeSelectorWindow(self, ["<type> <name> <message>", "<message>"], self._set_format_type)
        print(lf.log.formatType)
        if lf.log.formatType == "cancelled":
            lf.cleanup()
            return
        #end if
        self.edit_log(self.logFrameList[-1])


        state = BooleanVar()
        cb = ttk.Checkbutton(lf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_log_state, state, self.logFrameList[-1].log))
        cb.grid(row=0, column=3, sticky="e")

        print("Done.")
    #end _add_log


    def edit_log(self, log_frame):
        """
        This method uses the data stored in the log_frame to edit the data stored in the associated
        Log object.

        :param log_frame: The LogFrame containing the log to be edited
        """
        print("Editing ", log_frame.log, "...")
        LogWindow(self.app, self.app.gui, log_frame.log, log_frame.log.formatType)
    #end edit_log


    def delete_log(self, log_frame):
        """
        This method uses the data stored in the log_frame to remove the associated Log object from the
        current trigger. Once that is completed, it removes the log_frame widget from the GUI.

        :param log_frame: The LogFrame to be removed
        """
        print("Removing %s from Triggers" % log_frame.log)

        self.trigger.remove_log(log_frame.log)

        self.logFrameList.remove(log_frame)
        log_frame.frame.pack_forget()
        log_frame.frame.destroy()

        print("Done.")
    #end delete_log


    def populate_log(self, log):
        """
        This method populates the GUI with a LogFrame widget, then stores the data from log inside it

        :param log: the log containing the data to be populated
        """
        lf = LogFrame(self, self.trigger, "log", populating=True)
        lf.log = log

        state = BooleanVar()
        cb = ttk.Checkbutton(lf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_log_state, state, log))
        cb.grid(row=0, column=3, sticky="e")

        if log.isActive:
            state.set(1)
            self._change_log_state(state, log)
    #end populate_log


    @staticmethod
    def _change_log_state(state, log):
        """
        Set log to state
        :param state: the state of the log
        :param log: the log
        """
        log.isActive = state.get()
        print(log, "is now", log.isActive)
    #def _change_trigger_state


    def _set_format_type(self, format_type):
        """
        Set the format of the log, so the code knows what to look for
        :param format_type:
        :return:
        """
        self.logFrameList[-1].log.formatType = format_type
    #end _set_format_type

#end class AggregatedLogFrame


class LogFrame(object):
    """This class extends ttk.Frame to create a custom GUI widget"""

    def __init__(self, master, trigger, name, populating=False):
        self.log = None
        if not populating:
            self.log = trigger.add_log()
        self.master = master
        self.trigger = trigger

        self.frame = ttk.Frame(master.inner)
        self.frame.pack(expand=True, fill="x")
        self.frame.grid_columnconfigure(0, weight=1)

        label = ttk.Label(self.frame, text=name)
        label.grid(row=0, column=0, sticky="ew", padx=(5, 0))

        self.master.logFrameList.append(self)

        edit_button = ttk.Button(self.frame, text="edit", width=3, command=partial(self.master.edit_log, self))
        edit_button.grid(row=0, column=1)

        delete_button = ttk.Button(self.frame, text="X", width=0, command=partial(self.master.delete_log, self))
        delete_button.grid(row=0, column=2)
    #end init


    def cleanup(self):
        """Clean up whatever popups we've created"""
        self.master.delete_log(self)
    #end _cleanup

#end class LogFrame


class LogWindow(object):
    """This class creates a custom pop-up window to display and edit the data in an associated Log object"""

    def __init__(self, app, master, log, format_type):
        print("\tBuilding LogWindow...")

        self.app        = app
        self.log        = log
        self.formatType = format_type
        self.logGroup   = StringVar()
        self.name       = StringVar()
        self.message    = StringVar()

        self.top = Toplevel(master)
        self.top.title("Edit Log")
        self.top.configure(bg="#ededed")
        self.top.grab_set()  # freezes the app until the user enters or cancels

        frame = ttk.Frame(self.top)
        frame.pack(side=TOP)

        if format_type == "<message>":
            self.message.set("<message>")
            entry = ttk.Entry(frame, textvariable=self.message)
            entry.grid(row=0, column=0)
        else:
            self.logGroup.set("<type>")
            entry = ttk.Entry(frame, textvariable=self.logGroup, width=10)
            entry.grid(row=0, column=0)

            self.name.set("<name>")
            entry2 = ttk.Entry(frame, textvariable=self.name, width=10)
            entry2.grid(row=0, column=1)

            self.message.set("<message>")
            entry3 = ttk.Entry(frame, textvariable=self.message, width=30)
            entry3.grid(row=0, column=2)
        #end if/else

        self.closeButton = ttk.Button(self.top, text="Ok", command=self.cleanup)
        self.closeButton.pack(side=BOTTOM)

        self.populate_log_window()

        print("\tDone.")
    #end init


    def cleanup(self):
        """Clean up whatever popups we've created"""
        self._store_data()
        self.top.grab_release()  # HAVE TO RELEASE
        self.top.destroy()
    #end _cleanup


    def _store_data(self):
        """Store the data from the GUI into the associated Log object"""
        print("\nStoring LogWindow data...", end="\t")
        self.log.clear_log()

        if self.formatType == "<message>":
            self.log.log[0] = self.message.get()
        else:
            self.log.log[0] = self.logGroup.get()
            self.log.log[1] = self.name.get()
            self.log.log[2] = self.message.get()
        #end if/else

        print("Done.")
    #end store_data


    def populate_log_window(self):
        """Take the associated Trigger object, and populate each of the widgets in the window with the data inside"""
        print("Populating TriggerWindow...", end="\t")

        if self.formatType == "<message>":
            if self.log.log[0] is not None:
                self.message.set(self.log.log[0].lstrip('`').rstrip('`'))
        else:
            if self.log.log[0] is not None:
                self.logGroup.set(self.log.log[0])
            if self.log.log[1] is not None:
                self.name.set(self.log.log[1])
            if self.log.log[2] is not None:
                self.message.set(self.log.log[2].lstrip('`').rstrip('`'))
        #end if/else

        print("Done.")
    #end populate_log_window

#end class LogWindow


class AggregatedTriggerConditionsFrame(ttk.Frame):
    """
    This class extends ttk.Frame, allowing the user to add an arbitrary
    number of TriggerConditionFrame widgets to the GUI.
    """

    def __init__(self, app, parent, trigger):
        ttk.Frame.__init__(self, parent)

        self.app          = app
        self.parent       = parent
        self.trigger      = trigger
        self.tcFrameList  = []

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
        print("Adding TriggerCondition...")

        tc = TriggerConditionFrame(self, self.trigger, "log")
        self.condTypes = ["<condition> (= | += | -=) <value>", "<condition> (++ | --)", "(set | clear) <condition>"]
        TypeSelectorWindow(self, self.condTypes, self._set_format_type)

        if tc.condition.conditionType == "cancelled":
            tc.cleanup()
            return
        #end if
        self.edit_trigger_condition(self.tcFrameList[-1])


        state = BooleanVar()
        cb = ttk.Checkbutton(tc.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_tc_state, state, self.tcFrameList[-1].condition))
        cb.grid(row=0, column=3, sticky="e")

        print("Done.")
    #end _add_trigger_condition


    def edit_trigger_condition(self, tc_frame):
        """
        This method uses the data stored in the tc_frame to edit the data stored in the associated
        TriggerCondition object.

        :param tc_frame: The TriggerConditionFrame containing the condition to be edited
        """
        print("Editing ", tc_frame.condition, "...")
        TriggerConditionWindow(self.app, self.app.gui, tc_frame.condition)
    #end edit_trigger_condition


    def delete_trigger_condition(self, tc_frame):
        """
        This method uses the data stored in the tc_frame to remove the associated TriggerCondition object from the
        current trigger. Once that is completed, it removes the tc_frame widget from the GUI.

        :param tc_frame: The TriggerConditionFrame to be removed
        """
        print("Removing %s from Triggers" % tc_frame.condition)

        self.trigger.remove_tc(tc_frame.condition)

        self.tcFrameList.remove(tc_frame)
        tc_frame.frame.pack_forget()
        tc_frame.frame.destroy()

        print("Done.")
    #end delete_trigger_condition


    def populate_trigger_condition(self, condition):
        """
        This method populates the GUI with a TriggerConditionFrame widget, then stores the data from condition inside it

        :param condition: the TriggerCondition containing the data to be populated
        """
        tc = TriggerConditionFrame(self, self.trigger, "log", populating=True)
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
        tc.isActive = state.get()
        print(tc, "is now", tc.isActive)
    #def changeTriggerConditionsState


    def _set_format_type(self, format_type):
        if format_type == "cancelled":
            self.tcFrameList[-1].condition.conditionType = "cancelled"
            return
        ft = self.condTypes.index(format_type)
        self.tcFrameList[-1].condition.conditionType = ft
    #end _set_format_type

#end class AggregatedTriggerConditionsFrame


class TriggerConditionFrame(object):

    def __init__(self, master, trigger, name, populating=False):
        self.condition = None
        if not populating:
            self.condition = trigger.add_tc()
        self.master  = master
        self.trigger = trigger

        self.frame = ttk.Frame(master.inner)
        self.frame.pack(expand=True, fill="x")
        self.frame.grid_columnconfigure(0, weight=1)

        label = ttk.Label(self.frame, text=name)
        label.grid(row=0, column=0, sticky="ew", padx=(5, 0))

        self.master.tcFrameList.append(self)

        edit_button = ttk.Button(self.frame, text="edit", width=3, command=partial(self.master.edit_trigger_condition, self))
        edit_button.grid(row=0, column=1)

        delete_button = ttk.Button(self.frame, text="X", width=0, command=partial(self.master.delete_trigger_condition, self))
        delete_button.grid(row=0, column=2)
    #end init


    def cleanup(self):
        self.master.delete_trigger_condition(self)
    #end _cleanup

#end class LogFrame


class TriggerConditionWindow(object):

    def __init__(self, app, master, condition):
        print("\tBuilding TriggerConditionWindow...")

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
            entry = ttk.Entry(frame, textvariable=self.condData)
            entry.grid(row=0, column=0)


            self.selectedOption = "="
            self.comboOptions = ["=", "+=", "-="]
            self.optionsCombo.configure(values=self.comboOptions, width=5)
            self.optionsCombo.current(0)
            self.optionsCombo.grid(row=0, column=1)

            self.value.set("<value>")
            entry2 = ttk.Entry(frame, textvariable=self.value, width=6)
            entry2.grid(row=0, column=2)
        elif self.conditionType == 1:
            entry = ttk.Entry(frame, textvariable=self.condData)
            entry.grid(row=0, column=0)

            self.selectedOption = "++"
            self.comboOptions = ["++", "--"]
            self.optionsCombo.configure(values=self.comboOptions, width=5)
            self.optionsCombo.current(0)
            self.optionsCombo.grid(row=0, column=1)
        elif self.conditionType == 2:
            self.selectedOption = "set"
            self.comboOptions = ["set", "clear"]
            self.optionsCombo.configure(values=self.comboOptions, width=5)
            self.optionsCombo.current(0)
            self.optionsCombo.grid(row=0, column=0)

            entry = ttk.Entry(frame, textvariable=self.condData)
            entry.grid(row=0, column=1)
        else:
            print("Invalid conditionType!!")
        #end if/else

        self.closeButton = ttk.Button(self.top, text="Ok", command=self.cleanup)
        self.closeButton.pack(side=BOTTOM)

        self._populate_tc_window()

        print("\tDone.")
    #end init


    def cleanup(self):
        self._store_data()
        self.top.grab_release()  # HAVE TO RELEASE
        self.top.destroy()
    #end _cleanup


    def _store_data(self):
        print("\nStoring TriggerConditionWindow data...", end="\t")
        self.condition.clear_condition()

        if self.conditionType == 0:
            self.condition.condition[0] = self.condData.get()
            self.condition.condition[1] = self.selectedOption
            self.condition.condition[2] = self.value.get()
        elif self.conditionType == 1:
            self.condition.condition[0] = self.condData.get()
            self.condition.condition[1] = self.selectedOption
        elif self.conditionType == 2:
            self.condition.condition[1] = self.selectedOption
            self.condition.condition[0] = self.condData.get()
        else:
            print("Invalid conditionType!!!")
        #end if/else

        print("Done.")
    #end _store_data


    def _populate_tc_window(self):
        print("\t\tPopulating TriggerWindow...", end="\t")

        if self.conditionType == 0:
            if self.condition.condition[0] is not None:
                self.condData.set(self.condition.condition[0])
                index = self.comboOptions.index(self.condition.condition[1])
                self.optionsCombo.current(index)
                self.value.set(self.condition.condition[2])
            #end if
        elif self.conditionType == 1:
            if self.condition.condition[0] is not None:
                self.condData.set(self.condition.condition[0])
                index = self.comboOptions.index(self.condition.condition[1])
                self.optionsCombo.current(index)
            #end if
        elif self.conditionType == 2:
            if self.condition.condition[0] is not None:
                print(self.condition.condition[1])
                index = self.comboOptions.index(self.condition.condition[0])
                self.optionsCombo.current(index)
                self.condData.set(self.condition.condition[1])
        else:
            print("Data corrupted")
        #end if/else

        print("Done.")
    #end _populate_log_window


    def _combo_callback(self, event=None):
        self.selectedOption = self.optionsCombo.get()
    #end _combo_callback

#end class LogWindow
