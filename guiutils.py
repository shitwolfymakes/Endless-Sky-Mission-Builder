""" guiutils.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

This file contains helper functions and custom widgets for the ESMB gui
"""
from tkinter import *
from tkinter import ttk
from functools import partial

from Mission import *


def add_mission(app, new_mission_name):
    print("Adding mission: \"%s\"..." % new_mission_name, end="\t\t")

    mission = Mission(new_mission_name, default=True)
    app.missionList.append(mission)
    app.missionNameToObjectDict.update({mission.missionName: mission})
    app.activeMission = mission
    app.update_option_frame()
# end add_mission


def build_mand_opt_frame(parent, sub_component_name, num_mandatory, num_optionals, list_default_entry_data):
    new_frame = _SubComponentMandOptFrame(parent, sub_component_name, num_mandatory, num_optionals, list_default_entry_data)
    return new_frame
#end build_mand_opt_frame


def build_component_frame(parent, component_name, num_mandatory, num_optionals, list_default_entry_data):
    new_frame = _ComponentMandOptFrame(parent, component_name, num_mandatory, num_optionals, list_default_entry_data)
    return new_frame
#end build_mand_opt_frame


def build_combo_component_frame(parent, component_name, list_combobox_data):
    new_frame = _ComboComponentFrame(parent, component_name, list_combobox_data)
    return new_frame
#end build_combo_component_frame


class _ComboComponentFrame(ttk.Frame):

    def __init__(self, parent, component_name, list_combobox_data):
        ttk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)

        print("\tBuilding \"%s\"" % component_name)
        label = ttk.Label(self, text=component_name)
        label.grid(row=0, column=0, sticky="w", padx=(5, 0))

        self.listComboboxData = list_combobox_data
        self.isActive = BooleanVar()
        self.option   = None

        self.button   = ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.isActive)
        self.combo    = ttk.Combobox(self, state="disabled", values=self.listComboboxData, style='D.TCombobox')
        self.combo.bind("<<ComboboxSelected>>", self.option_selected)

        self.button.configure(command=partial(self._cb_value_changed, self.isActive, [self.combo]))
        self.button.grid(row=0, column=1, sticky="e")
        self.combo.grid(row=1, column=0, sticky="ew", padx=(20,0))

    #end init

    @staticmethod
    def _cb_value_changed(entry_state, modified_widgets):
        for widget in modified_widgets:
            print("The value of %s is:" % widget, end="\t\t")
            print(entry_state.get())
            if type(widget) is str:
                break
            elif entry_state.get() is True:
                widget.config(state='readonly', style='TCombobox')
            elif entry_state.get() is False:
                widget.config(state='disabled', style='D.TCombobox')
            # end if/else
        # end for
    # end cb_value_changed

    def option_selected(self, event=None):
        selected_option = self.combo.get()
        print('\nOption selected: "%s"' % selected_option)
    #end mission_selected


    def set(self, data):
        """
            This method does the following:
                1) set the given entry state to 1
                2) set the combobox to the given data
                3) enable the given entry using cb_value_changed
        """

        self.isActive.set(1)
        self.combo.current(self.listComboboxData.index(data.title()))
        self._cb_value_changed(self.isActive, [self.combo])
    #end set


    def reset(self):
        self.isActive.set(0)
        self.combo.current(None)
        self.combo.config(state='disabled', style='D.TCombobox')
    #end reset

#end class _ComboComponentFrame


class _ComponentMandOptFrame(ttk.Frame):

    def __init__(self, parent, component_name, num_mandatory, num_optionals, list_default_entry_data):
        ttk.Frame.__init__(self, parent)
        # this line makes the frames with no mandatory or optionals fill the frame
        self.columnconfigure(0, weight=1)

        disabled_entry_style = ttk.Style()
        disabled_entry_style.configure('D.TEntry', background='#D3D3D3')

        self.componentName        = component_name
        self.numMandatory         = num_mandatory
        self.numOptionals         = num_optionals
        self.listDefaultEntryData = list_default_entry_data

        self.rowNum       = 0
        self.numMandatory = num_mandatory
        self.numOptionals = num_optionals
        self.numFields    = num_mandatory + num_optionals

        self.listEntryStates  = []
        self.listCheckbuttons = []
        self.listEntryData    = []
        self.listEntries      = []

        self._build()
    # end init


    '''
        This function takes in the parameters passed into the object call, 
        and executes different logic based on what it finds.

        e.g.: build_component_frame(parent, "fail", 2, 3, ["<test0>", "<test1>", "[<name>]", "[<test2>]", "[<test3>]"]) 

        becomes:
        +------------------------+
        | fail                [] |
        |         [<test0>]      |
        |         [<test1>]      |
        |         [<name>]    [] |
        |         [<test2>]   [] |
        |         [<test3>]   [] |
        +------------------------+
    '''
    def _build(self):
        print("\t\tBuilding \"%s\"" % self.componentName)
        label1 = ttk.Label(self, text=self.componentName)
        label1.grid(row=0, column=0, sticky="w", padx=(5, 0))
        self.rowNum += 1

        # all components need at least one entry state
        self.listEntryStates.append(BooleanVar())

        # Case 1: No mandatory fields
        if self.numMandatory is 0:
            # print("\t\t\tNo mandatory fields")

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].configure(command=partial(self._cb_value_changed,
                                                               self.listEntryStates[0],
                                                               [self.componentName]))
            self.listCheckbuttons[0].grid(row=0, column=1, sticky="e")

            self.rowNum += 1
        # Case 2: 1 mandatory field
        elif self.numMandatory is 1:
            # print("\t\t\t1 mandatory field")

            self.listEntryData.append(StringVar())
            self.listEntryData[0].set(self.listDefaultEntryData[0])

            self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[0], state=DISABLED, style='D.TEntry', width=30))
            self.listEntries[0].grid(row=self.rowNum, column=0, sticky="ew", padx=(20, 0))

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].configure(command=partial(self._cb_value_changed,
                                                               self.listEntryStates[0],
                                                               [self.listEntries[0]]))
            self.listCheckbuttons[0].grid(row=0, column=1, sticky="e")

            self.rowNum += 1
        # Case 3: More than 1 mandatory field
        elif self.numMandatory > 1:
            # print("\t\t\t%d mandatory fields" % self.numMandatory)

            # add the first checkbutton
            self.listEntryData.append(StringVar())
            self.listEntryData[0].set(self.listDefaultEntryData[0])

            self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[0], state=DISABLED, style='D.TEntry', width=30))
            self.listEntries[0].grid(row=self.rowNum, column=0, sticky="ew", padx=(20, 0))

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].grid(row=0, column=1, sticky="e")

            self.rowNum += 1

            # loop through the remaining mandatory fields, slaving them to the first checkbutton
            for i in range(1, self.numMandatory):
                self.listEntryData.append(StringVar())
                self.listEntryData[-1].set(self.listDefaultEntryData[i])

                self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[-1], state=DISABLED, style='D.TEntry', width=30))
                self.listEntries[-1].grid(row=self.rowNum, column=0, sticky="ew", padx=(20, 0))

                self.rowNum += 1
            # end for

            self.listCheckbuttons[0].configure(command=partial(self._cb_value_changed,
                                                               self.listEntryStates[0],
                                                               self.listEntries[:self.numMandatory]))
        # end if/else

        # add the optional fields
        for i in range(self.numMandatory, self.numFields):
            self.listEntryStates.append(BooleanVar())
            self.listEntryData.append(StringVar())
            self.listEntryData[-1].set(self.listDefaultEntryData[i])

            self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[-1], state=DISABLED, style="D.TEntry", width=30))
            self.listEntries[-1].grid(row=self.rowNum, column=0, sticky="ew", padx=(20, 0))

            # We have to use functools.partial here because lambda can't be used
            # inside a loop(the bound lambda will use the last assigned values)
            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[-1]))
            self.listCheckbuttons[-1].configure(command=partial(self._cb_value_changed,
                                                                self.listEntryStates[-1],
                                                                [self.listEntries[-1]]))
            self.listCheckbuttons[-1].grid(row=self.rowNum, column=1, sticky="e")

            self.rowNum += 1
        # end for
    # end _build


    @staticmethod
    def _cb_value_changed(entry_state, modified_widgets):
        for widget in modified_widgets:
            print("The value of %s is:" % widget, end="\t\t")
            print(entry_state.get())
            if type(widget) is str:
                break
            elif entry_state.get() is True:
                widget.config(state='enabled', style='TEntry')
            elif entry_state.get() is False:
                widget.config(state='disabled', style='D.TEntry')
            #end if/else
        # end for
    # end cb_value_changed


    def set(self, entry_state_num, entry_num, data):
        """
            This method does the following:
                1) set the given entry state to 1
                2) store data in the given entry
                3) enable the given entry using cb_value_changed
        """

        if self.listEntryStates[entry_state_num].get() is False:
            self.listEntryStates[entry_state_num].set(1)

        if entry_num is None:
            self._cb_value_changed(self.listEntryStates[entry_state_num], [data])
        else:
            self.listEntryData[entry_num].set(data)
            self._cb_value_changed(self.listEntryStates[entry_state_num], [self.listEntries[entry_num]])
        #end if/else
    #end set


    def reset(self):
        for entry in self.listEntryStates:
            entry.set(0)
        for i, entry in enumerate(self.listEntryData):
            entry.set(self.listDefaultEntryData[i])
        for entry in self.listEntries:
            entry.config(state='disabled', style='D.TEntry')
    #end reset


    def print_data(self):
        print("%s Data:" % self.componentName)
        print("\tlistEntryStates: ")
        for es in self.listEntryStates:
            print("\t\t%s" % str(es.get()))
        print("\tlistCheckbuttons: ", self.listCheckbuttons)
        print("\tlistEntryData: ")
        for ed in self.listEntryData:
            print("\t\t%s" % ed.get())
        print("\tlistEntries: ", self.listEntries)
    #end print_data

# end class _ComponentMandOptFrame


class _SubComponentMandOptFrame(ttk.Frame):

    def __init__(self, parent, sub_component_name, num_mandatory, num_optionals, list_default_entry_data):
        ttk.Frame.__init__(self, parent)

        disabledEntryStyle = ttk.Style()
        disabledEntryStyle.configure('D.TEntry', background='#D3D3D3')

        self.subComponentName     = sub_component_name
        self.numMandatory         = num_mandatory
        self.numOptionals         = num_optionals
        self.listDefaultEntryData = list_default_entry_data

        self.rowNum       = 0
        self.numMandatory = num_mandatory
        self.numOptionals = num_optionals
        self.numFields    = num_mandatory + num_optionals

        self.listEntryStates  = []
        self.listCheckbuttons = []
        self.listEntryData    = []
        self.listEntries      = []

        self._build()
    # end init


    '''
        This function takes in the parameters passed into the object call, 
        and executes different logic based on what it finds.

        e.g.: build_mand_opt_frame(self.leftFrame, "fail", 2, 3, ["<test0>", "<test1>", "[<name>]", "[<test2>]", "[<test3>]"]) 

        becomes:
        +------------------------+
        | fail    [<test0>]   [] |
        |         [<test1>]      |
        |         [<name>]    [] |
        |         [<test2>]   [] |
        |         [<test3>]   [] |
        +------------------------+
    '''
    def _build(self):
        # print("\t\tBuilding \"%s\"" % self.subComponentName)
        label1 = ttk.Label(self, text=self.subComponentName, width=7)
        label1.grid(row=self.rowNum, column=0, sticky="w", padx=(5, 0))

        # all components need at least one entry state
        self.listEntryStates.append(BooleanVar())

        # Case 1: No mandatory fields
        if self.numMandatory is 0:
            # print("\t\t\tNo mandatory fields")

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].configure(command=partial(self.cb_value_changed,
                                                               self.listEntryStates[0],
                                                               [self.subComponentName]))
            self.listCheckbuttons[0].grid(row=self.rowNum, column=2, sticky="e")

            self.rowNum += 1
        # Case 2: 1 mandatory field
        elif self.numMandatory is 1:
            # print("\t\t\t1 mandatory field")

            self.listEntryData.append(StringVar())
            self.listEntryData[0].set(self.listDefaultEntryData[0])

            self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[0], state=DISABLED, style='D.TEntry'))
            self.listEntries[0].grid(row=0, column=1, sticky="ew")

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].configure(command=partial(self.cb_value_changed,
                                                               self.listEntryStates[0],
                                                               [self.listEntries[0]]))
            self.listCheckbuttons[0].grid(row=self.rowNum, column=2, sticky="e")

            self.rowNum += 1
        # Case 3: More than 1 mandatory field
        elif self.numMandatory > 1:
            # print("\t\t\t%d mandatory fields" % self.numMandatory)

            # add the first checkbutton
            self.listEntryData.append(StringVar())
            self.listEntryData[0].set(self.listDefaultEntryData[0])

            self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[0], state=DISABLED, style='D.TEntry'))
            self.listEntries[0].grid(row=0, column=1, sticky="ew")

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].grid(row=self.rowNum, column=2, sticky="e")

            self.rowNum += 1

            # loop through the remaining mandatory fields, slaving them to the first checkbutton
            for i in range(1, self.numMandatory):
                self.listEntryData.append(StringVar())
                self.listEntryData[-1].set(self.listDefaultEntryData[i])

                self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[-1], state=DISABLED, style='D.TEntry'))
                self.listEntries[-1].grid(row=self.rowNum, column=1, sticky="ew")

                self.rowNum += 1
            # end for

            self.listCheckbuttons[0].configure(command=partial(self.cb_value_changed,
                                                               self.listEntryStates[0],
                                                               self.listEntries[:self.numMandatory]))
        # end if/else

        # add the optional fields
        for i in range(self.numMandatory, self.numFields):
            self.listEntryStates.append(BooleanVar())
            self.listEntryData.append(StringVar())
            self.listEntryData[-1].set(self.listDefaultEntryData[i])

            self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[-1], state=DISABLED, style="D.TEntry"))
            self.listEntries[-1].grid(row=self.rowNum, column=1, sticky="ew")

            # We have to use functools.partial here because lambda can't be used
            # inside a loop(the bound lambda will use the last assigned values)
            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[-1]))
            self.listCheckbuttons[-1].configure(command=partial(self.cb_value_changed,
                                                                self.listEntryStates[-1],
                                                                [self.listEntries[-1]]))
            self.listCheckbuttons[-1].grid(row=self.rowNum, column=2, sticky="e")

            self.rowNum += 1
        # end for

    # end _build


    @staticmethod
    def cb_value_changed(entry_state, modified_widgets):
        for widget in modified_widgets:
            print("The value of %s is:" % widget, end="\t\t")
            print(entry_state.get())
            if type(widget) is str:
                break
            elif entry_state.get() is True:
                widget.config(state='enabled', style='TEntry')
            elif entry_state.get() is False:
                widget.config(state='disabled', style='D.TEntry')
            #end if/else
        # end for
    # end cb_value_changed

# end class _SubComponentMandOptFrame


class TypeSelectorWindow(Toplevel):

    def __init__(self, master, options, callback, **kwargs):
        self.callback = callback
        super().__init__(master, **kwargs)

        self.optionList = ttk.Combobox(self, values=options, state="readonly", width=25)
        self.optionList.current(0)
        self.optionList.pack()

        buttons = ttk.Frame(self)
        ok = ttk.Button(buttons, text="OK", command=self._cleanup)
        ok.pack(side=LEFT, fill="x")
        cxl = ttk.Button(buttons, text="Cancel", command=self._cancelled)
        cxl.pack(fill="x")
        buttons.pack()

        # these commands make the parent window inactive
        self.transient(master)
        self.grab_set()
        master.wait_window(self)
    #end init


    def _cleanup(self):
        self.callback(self.optionList.get())
        self.destroy()
    #end _cleanup


    def _cancelled(self):
        self.callback("cancelled")
        self.destroy()
    #end _cancelled

#end class TypeSelectorWindow
