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
from src.model.Mission import *


def add_mission(app, new_mission_name):
    """
    Helper method that creates a new mission, then updates the data model and GUI

    :param app: The ESMB object
    :param new_mission_name: A string containing the name of the new mission
    """
    logging.debug("Adding mission: \"%s\"..." % new_mission_name)

    mission = Mission(new_mission_name, default=True)
    app.missionList.append(mission)
    app.missionNameToObjectDict.update({mission.missionName: mission})
    app.activeMission = mission
    app.update_option_frame()
# end add_mission


def build_mand_opt_frame(parent, sub_component_name, num_mandatory, num_optionals, list_default_entry_data):
    """
    This method returns a SubComponentMandOptFrame object

    :param parent: The parent widget of this one
    :param sub_component_name: The name of the mission component
    :param num_mandatory: The number of must-use mission subcomponents
    :param num_optionals: The number of optional-use mission subcomponents
    :param list_default_entry_data: The default data to be stored in the entries that will be created
    """
    new_frame = _SubComponentMandOptFrame(parent, sub_component_name, num_mandatory, num_optionals, list_default_entry_data)
    return new_frame
#end build_mand_opt_frame


def build_combo_component_frame(parent, component_name, list_combobox_data):
    """
    This method returns a SubComponentMandOptFrame object

    :param parent: The parent widget of this one
    :param component_name: The name of the mission component
    :param list_combobox_data: The data that the combobox will contain
    """
    new_frame = _ComboComponentFrame(parent, component_name, list_combobox_data)
    return new_frame
#end build_combo_component_frame


class _SubComponentMandOptFrame(ttk.Frame):
    """This class extends ttk.Frame to create a custom GUI widget"""

    def __init__(self, parent, sub_component_name, num_mandatory, num_optionals, list_default_entry_data):
        ttk.Frame.__init__(self, parent)

        disabled_entry_style = ttk.Style()
        disabled_entry_style.configure('D.TEntry', background='#D3D3D3')

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


    def _build(self):
        """
        This function takes in the parameters passed into the object call, and executes different logic based on what
        it finds. Each mandatory entry will be slaved to a single checkbutton, whereas each optional entry will be
        slaved to it's own separate checkbutton

        For example:

        build_mand_opt_frame(self.leftFrame, "fail", 2, 3, ["<test0>", "<test1>", "[<name>]", "[<test2>]", "[<test3>]"])

        becomes:

        +------------------------+
        | fail    [<test0>]   [] |
        |         [<test1>]      |
        |         [<name>]    [] |
        |         [<test2>]   [] |
        |         [<test3>]   [] |
        +------------------------+
        """
        logging.debug("\t\tBuilding \"%s\"" % self.subComponentName)
        label1 = ttk.Label(self, text=self.subComponentName, width=7)
        label1.grid(row=self.rowNum, column=0, sticky="w", padx=(5, 0))

        # all components need at least one entry state
        self.listEntryStates.append(BooleanVar())

        # Case 1: No mandatory fields
        if self.numMandatory is 0:
            logging.info("\t\t\tNo mandatory fields")

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].configure(command=partial(self.cb_value_changed,
                                                               self.listEntryStates[0],
                                                               [self.subComponentName]))
            self.listCheckbuttons[0].grid(row=self.rowNum, column=2, sticky="e")

            self.rowNum += 1
        # Case 2: 1 mandatory field
        elif self.numMandatory is 1:
            logging.info("\t\t\t1 mandatory field")

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
            logging.info("\t\t\t%d mandatory fields" % self.numMandatory)

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

# end class _SubComponentMandOptFrame
