""" ComponentMandOptFrame.py
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


class ComponentMandOptFrame(ttk.Frame):
    """This class extends ttk.Frame to create a custom GUI widget"""

    def __init__(self, parent, component_name, num_mandatory, num_optionals, list_default_entry_data):
        ttk.Frame.__init__(self, parent)
        # this line makes the frames with no mandatory or optionals fill the frame
        self.columnconfigure(0, weight=1)

        disabled_entry_style = ttk.Style()
        disabled_entry_style.configure('D.TEntry', background='#D3D3D3')

        self.componentName = component_name
        self.numMandatory = num_mandatory
        self.numOptionals = num_optionals
        self.listDefaultEntryData = list_default_entry_data

        self.rowNum = 0
        self.numMandatory = num_mandatory
        self.numOptionals = num_optionals
        self.numFields = num_mandatory + num_optionals

        self.listEntryStates = []
        self.listCheckbuttons = []
        self.listEntryData = []
        self.listEntries = []

        self._build()
    # end init


    def _build(self):
        """
        This function takes in the parameters passed into the object call, and executes different logic based on what
        it finds. Each mandatory entry will be slaved to a single checkbutton, whereas each optional entry will be
        slaved to it's own separate checkbutton

        For example:

        ComponentMandOptFrame(self.leftFrame, "fail", 2, 3, ["<test0>", "<test1>", "[<name>]", "[<test2>]", "[<test3>]"])

        becomes:

        +------------------------+
        | fail    [<test0>]   [] |
        |         [<test1>]      |
        |         [<name>]    [] |
        |         [<test2>]   [] |
        |         [<test3>]   [] |
        +------------------------+
        """
        logging.debug("\t\tBuilding \"%s\"" % self.componentName)
        label1 = ttk.Label(self, text=self.componentName)
        label1.grid(row=0, column=0, sticky="w", padx=(5, 0))
        self.rowNum += 1

        # all components need at least one entry state
        self.listEntryStates.append(BooleanVar())

        # Case 1: No mandatory fields
        if self.numMandatory is 0:
            logging.info("\t\t\tNo mandatory fields")

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].configure(command=partial(self.cb_value_changed,
                                                               self.listEntryStates[0],
                                                               [self.componentName]))
            self.listCheckbuttons[0].grid(row=0, column=1, sticky="e")

            self.rowNum += 1
        # Case 2: 1 mandatory field
        elif self.numMandatory is 1:
            logging.info("\t\t\t1 mandatory field")

            self.listEntryData.append(StringVar())
            self.listEntryData[0].set(self.listDefaultEntryData[0])

            self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[0], state=DISABLED, style='D.TEntry', width=30))
            self.listEntries[0].grid(row=self.rowNum, column=0, sticky="ew", padx=(20, 0))

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].configure(command=partial(self.cb_value_changed,
                                                               self.listEntryStates[0],
                                                               [self.listEntries[0]]))
            self.listCheckbuttons[0].grid(row=0, column=1, sticky="e")

            self.rowNum += 1
        # Case 3: More than 1 mandatory field
        elif self.numMandatory > 1:
            logging.info(str.format("\t\t\t%d mandatory fields" % self.numMandatory))

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

            self.listCheckbuttons[0].configure(command=partial(self.cb_value_changed,
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
            self.listCheckbuttons[-1].configure(command=partial(self.cb_value_changed,
                                                                self.listEntryStates[-1],
                                                                [self.listEntries[-1]]))
            self.listCheckbuttons[-1].grid(row=self.rowNum, column=1, sticky="e")

            self.rowNum += 1
        # end for
    # end _build


    @staticmethod
    def cb_value_changed(entry_state, modified_widgets):
        """
        Set each of the modified_widgets to entry_state

        :param entry_state: The boolean value of the entry
        :param modified_widgets: A list of widgets
        """
        for widget in modified_widgets:
            logging.debug("The value of %s is: %s" % (widget, entry_state.get()))
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

        :param entry_state_num: The entry state that will be changed
        :param entry_num: The entry the data will be stored in
        :param data: The data to be stored
        """
        if self.listEntryStates[entry_state_num].get() is False:
            self.listEntryStates[entry_state_num].set(1)

        if entry_num is None:
            self.cb_value_changed(self.listEntryStates[entry_state_num], [data])
        else:
            self.listEntryData[entry_num].set(data)
            self.cb_value_changed(self.listEntryStates[entry_state_num], [self.listEntries[entry_num]])
        #end if/else
    #end set


    def reset(self):
        """Reset the entry to the default format"""
        for entry in self.listEntryStates:
            entry.set(0)
        for i, entry in enumerate(self.listEntryData):
            entry.set(self.listDefaultEntryData[i])
        for entry in self.listEntries:
            entry.config(state='disabled', style='D.TEntry')
    #end reset


    def print_data(self):
        """Prints the data all fancy-like"""
        logging.debug("%s Data:" % self.componentName)
        logging.debug("\tlistEntryStates: ")
        for es in self.listEntryStates:
            logging.debug("\t\t%s" % str(es.get()))
        logging.debug("\tlistCheckbuttons: %s" % self.listCheckbuttons)
        logging.debug("\tlistEntryData: ")
        for ed in self.listEntryData:
            logging.debug("\t\t%s" % ed.get())
        logging.debug("\tlistEntries: %s" % self.listEntries)
    #end print_data

# end class ComponentMandOptFrame