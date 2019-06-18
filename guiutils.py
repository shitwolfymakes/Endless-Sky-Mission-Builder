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

def addMission(app, newMissionName):
    print("Adding mission: \"%s\"..." % newMissionName, end="\t\t")

    mission = Mission(newMissionName, default=True)
    app.missionList.append(mission)
    app.missionNameToObjectDict.update({mission.missionName: mission})
    app.activeMission = mission
    app.updateOptionFrame()
# end addMission


def buildMandOptFrame(parent, subComponentName, numMandatory, numOptionals, listDefaultEntryData):
    newFrame = _SubComponentMandOptFrame(parent, subComponentName, numMandatory, numOptionals, listDefaultEntryData)
    return newFrame
#end buildMandOptFrame


def buildComponentFrame(parent, componentName, numMandatory, numOptionals, listDefaultEntryData):
    newFrame = _ComponentMandOptFrame(parent, componentName, numMandatory, numOptionals, listDefaultEntryData)
    return newFrame
#end buildMandOptFrame


def buildComboComponentFrame(parent, componentName, listComboboxData):
    newFrame = _ComboComponentFrame(parent, componentName, listComboboxData)
    return newFrame
#end buildComboComponentFrame


class _ComboComponentFrame(ttk.Frame):

    def __init__(self, parent, componentName, listComboboxData):
        ttk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)

        print("\tBuilding \"%s\"" % componentName)
        label = ttk.Label(self, text=componentName)
        label.grid(row=0, column=0, sticky="w", padx=(5, 0))

        self.isActive = BooleanVar()
        self.option   = None

        self.button   = ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.isActive)
        self.combo    = ttk.Combobox(self, state="disabled", values=listComboboxData, style='D.TCombobox')
        self.combo.bind("<<ComboboxSelected>>", self.optionSelected)

        self.button.configure(command=partial(self.cbValueChanged, self.isActive, [self.combo]))
        self.button.grid(row=0, column=1, sticky="e")
        self.combo.grid(row=1, column=0, sticky="ew", padx=(20,0))

    #end init

    @staticmethod
    def cbValueChanged(entryState, modifiedWidgets):
        for widget in modifiedWidgets:
            print("The value of %s is:" % widget, end="\t\t")
            print(entryState.get())
            if type(widget) is str:
                break
            elif entryState.get() is True:
                widget.config(state='readonly', style='TCombobox')
            elif entryState.get() is False:
                widget.config(state='disabled', style='D.TCombobox')
            # end if/else
        # end for
    # end cbValueChanged

    def optionSelected(self, event=None):
        selectedOption = self.combo.get()
        print('\nOption selected: "%s"' % selectedOption)
    #end missionSelected

#end class _ComboComponentFrame


class _ComponentMandOptFrame(ttk.Frame):

    def __init__(self, parent, componentName, numMandatory, numOptionals, listDefaultEntryData):
        ttk.Frame.__init__(self, parent)
        # this line makes the frames with no mandatory or optionals fill the frame
        self.columnconfigure(0, weight=1)

        disabledEntryStyle = ttk.Style()
        disabledEntryStyle.configure('D.TEntry', background='#D3D3D3')

        self.componentName        = componentName
        self.numMandatory         = numMandatory
        self.numOptionals         = numOptionals
        self.listDefaultEntryData = listDefaultEntryData

        self.rowNum       = 0
        self.numMandatory = numMandatory
        self.numOptionals = numOptionals
        self.numFields    = numMandatory + numOptionals

        self.listEntryStates  = []
        self.listCheckbuttons = []
        self.listEntryData    = []
        self.listEntries      = []

        self.build()
    # end init


    '''
        This function takes in the parameters passed into the object call, 
        and executes different logic based on what it finds.

        e.g.: buildComponentFrame(parent, "fail", 2, 3, ["<test0>", "<test1>", "[<name>]", "[<test2>]", "[<test3>]"]) 

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
    def build(self):
        print("\t\tBuilding \"%s\"" % self.componentName)
        label1 = ttk.Label(self, text=self.componentName)
        label1.grid(row=0, column=0, sticky="w", padx=(5, 0))
        self.rowNum += 1

        # Case 1: No mandatory fields
        if self.numMandatory is 0:
            # print("\t\t\tNo mandatory fields")

            self.listEntryStates.append(BooleanVar())

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].configure(command=partial(self.cbValueChanged,
                                                               self.listEntryStates[0],
                                                               [self.componentName]))
            self.listCheckbuttons[0].grid(row=0, column=1, sticky="e")

            self.rowNum += 1
        # Case 2: 1 mandatory field
        elif self.numMandatory is 1:
            # print("\t\t\t1 mandatory field")

            self.listEntryStates.append(BooleanVar())
            self.listEntryData.append(StringVar())
            self.listEntryData[0].set(self.listDefaultEntryData[0])

            self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[0], state=DISABLED, style='D.TEntry'))
            self.listEntries[0].grid(row=self.rowNum, column=0, sticky="ew", padx=(20,0))

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].configure(command=partial(self.cbValueChanged,
                                                               self.listEntryStates[0],
                                                               [self.listEntries[0]]))
            self.listCheckbuttons[0].grid(row=0, column=1, sticky="e")

            self.rowNum += 1
        # Case 3: More than 1 mandatory field
        elif self.numMandatory > 1:
            # print("\t\t\t%d mandatory fields" % self.numMandatory)

            # add the first checkbutton
            self.listEntryStates.append(BooleanVar())
            self.listEntryData.append(StringVar())
            self.listEntryData[0].set(self.listDefaultEntryData[0])

            self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[0], state=DISABLED, style='D.TEntry'))
            self.listEntries[0].grid(row=self.rowNum, column=0, sticky="ew", padx=(20,0))

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].grid(row=0, column=1, sticky="e")

            self.rowNum += 1

            # loop through the remaining mandatory fields, slaving them to the first checkbutton
            for i in range(1, self.numMandatory):
                self.listEntryStates.append(BooleanVar())
                self.listEntryData.append(StringVar())
                self.listEntryData[-1].set(self.listDefaultEntryData[i])

                self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[-1], state=DISABLED, style='D.TEntry'))
                self.listEntries[-1].grid(row=self.rowNum, column=0, sticky="ew", padx=(20,0))

                self.rowNum += 1
            # end for

            self.listCheckbuttons[0].configure(command=partial(self.cbValueChanged,
                                                               self.listEntryStates[0],
                                                               self.listEntries[:self.numMandatory]))
        # end if/else

        # add the optional fields
        for i in range(self.numMandatory, self.numFields):
            self.listEntryStates.append(BooleanVar())
            self.listEntryData.append(StringVar())
            self.listEntryData[-1].set(self.listDefaultEntryData[i])

            self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[-1], state=DISABLED, style="D.TEntry"))
            self.listEntries[-1].grid(row=self.rowNum, column=0, sticky="ew", padx=(20,0))

            # We have to use functools.partial here because lambda can't be used
            # inside a loop(the bound lambda will use the last assigned values)
            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[-1]))
            self.listCheckbuttons[-1].configure(command=partial(self.cbValueChanged,
                                                                self.listEntryStates[-1],
                                                                [self.listEntries[-1]]))
            self.listCheckbuttons[-1].grid(row=self.rowNum, column=1, sticky="e")

            self.rowNum += 1
        # end for

    # end build


    @staticmethod
    def cbValueChanged(entryState, modifiedWidgets):
        for widget in modifiedWidgets:
            print("The value of %s is:" % widget, end="\t\t")
            print(entryState.get())
            if type(widget) is str:
                break
            elif entryState.get() is True:
                widget.config(state='enabled', style='TEntry')
            elif entryState.get() is False:
                widget.config(state='disabled', style='D.TEntry')
            #end if/else
        # end for
    # end cbValueChanged

# end class _ComponentMandOptFrame


class _SubComponentMandOptFrame(ttk.Frame):

    def __init__(self, parent, subComponentName, numMandatory, numOptionals, listDefaultEntryData):
        ttk.Frame.__init__(self, parent)

        disabledEntryStyle = ttk.Style()
        disabledEntryStyle.configure('D.TEntry', background='#D3D3D3')

        self.subComponentName     = subComponentName
        self.numMandatory         = numMandatory
        self.numOptionals         = numOptionals
        self.listDefaultEntryData = listDefaultEntryData

        self.rowNum       = 0
        self.numMandatory = numMandatory
        self.numOptionals = numOptionals
        self.numFields    = numMandatory + numOptionals

        self.listEntryStates  = []
        self.listCheckbuttons = []
        self.listEntryData    = []
        self.listEntries      = []

        self.build()
    # end init


    '''
        This function takes in the parameters passed into the object call, 
        and executes different logic based on what it finds.

        e.g.: buildMandOptFrame(self.leftFrame, "fail", 2, 3, ["<test0>", "<test1>", "[<name>]", "[<test2>]", "[<test3>]"]) 

        becomes:
        +------------------------+
        | fail    [<test0>]   [] |
        |         [<test1>]      |
        |         [<name>]    [] |
        |         [<test2>]   [] |
        |         [<test3>]   [] |
        +------------------------+
    '''
    def build(self):
        # print("\t\tBuilding \"%s\"" % self.subComponentName)
        label1 = ttk.Label(self, text=self.subComponentName, width=7)
        label1.grid(row=self.rowNum, column=0, sticky="w", padx=(5, 0))

        # Case 1: No mandatory fields
        if self.numMandatory is 0:
            # print("\t\t\tNo mandatory fields")

            self.listEntryStates.append(BooleanVar())

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].configure(command=partial(self.cbValueChanged,
                                                               self.listEntryStates[0],
                                                               [self.subComponentName]))
            self.listCheckbuttons[0].grid(row=self.rowNum, column=2, sticky="e")

            self.rowNum += 1
        # Case 2: 1 mandatory field
        elif self.numMandatory is 1:
            # print("\t\t\t1 mandatory field")

            self.listEntryStates.append(BooleanVar())
            self.listEntryData.append(StringVar())
            self.listEntryData[0].set(self.listDefaultEntryData[0])

            self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[0], state=DISABLED, style='D.TEntry'))
            self.listEntries[0].grid(row=0, column=1, sticky="ew")

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].configure(command=partial(self.cbValueChanged,
                                                               self.listEntryStates[0],
                                                               [self.listEntries[0]]))
            self.listCheckbuttons[0].grid(row=self.rowNum, column=2, sticky="e")

            self.rowNum += 1
        # Case 3: More than 1 mandatory field
        elif self.numMandatory > 1:
            # print("\t\t\t%d mandatory fields" % self.numMandatory)

            # add the first checkbutton
            self.listEntryStates.append(BooleanVar())
            self.listEntryData.append(StringVar())
            self.listEntryData[0].set(self.listDefaultEntryData[0])

            self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[0], state=DISABLED, style='D.TEntry'))
            self.listEntries[0].grid(row=0, column=1, sticky="ew")

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].grid(row=self.rowNum, column=2, sticky="e")

            self.rowNum += 1

            # loop through the remaining mandatory fields, slaving them to the first checkbutton
            for i in range(1, self.numMandatory):
                self.listEntryStates.append(BooleanVar())
                self.listEntryData.append(StringVar())
                self.listEntryData[-1].set(self.listDefaultEntryData[i])

                self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[-1], state=DISABLED, style='D.TEntry'))
                self.listEntries[-1].grid(row=self.rowNum, column=1, sticky="ew")

                self.rowNum += 1
            # end for

            self.listCheckbuttons[0].configure(command=partial(self.cbValueChanged,
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
            self.listCheckbuttons[-1].configure(command=partial(self.cbValueChanged,
                                                                self.listEntryStates[-1],
                                                                [self.listEntries[-1]]))
            self.listCheckbuttons[-1].grid(row=self.rowNum, column=2, sticky="e")

            self.rowNum += 1
        # end for

    # end build


    @staticmethod
    def cbValueChanged(entryState, modifiedWidgets):
        for widget in modifiedWidgets:
            print("The value of %s is:" % widget, end="\t\t")
            print(entryState.get())
            if type(widget) is str:
                break
            elif entryState.get() is True:
                widget.config(state='enabled', style='TEntry')
            elif entryState.get() is False:
                widget.config(state='disabled', style='D.TEntry')
            #end if/else
        # end for
    # end cbValueChanged

# end class _SubComponentMandOptFrame


class TypeSelectorWindow(Toplevel):

    def __init__(self, master, options, callback, **kwargs):
        self.callback = callback
        super().__init__(master, **kwargs)

        self.optionList = ttk.Combobox(self, values=options, state="readonly", width=25)
        self.optionList.current(0)
        self.optionList.pack()

        buttons = ttk.Frame(self)
        ok = ttk.Button(buttons, text="OK", command=self.cleanup)
        ok.pack(side=LEFT, fill="x")
        cxl = ttk.Button(buttons, text="Cancel", command=self.cancelled)
        cxl.pack(fill="x")
        buttons.pack()

        # these commands make the parent window inactive
        self.transient(master)
        self.grab_set()
        master.wait_window(self)
    #end init


    def cleanup(self):
        self.callback(self.optionList.get())
        self.destroy()
    #end cleanup


    def cancelled(self):
        self.callback("cancelled")
        self.destroy()
    #end cancelled

#end class TypeSelectorWindow