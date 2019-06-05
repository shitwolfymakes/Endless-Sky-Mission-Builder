''' guiutils.py
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

'''
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


class AggregatedComponentFrame(ttk.Frame):

    def __init__(self, app, parent, sectionName, componentType):
        ttk.Frame.__init__(self, parent)

        self.app           = app
        self.sectionName   = sectionName
        self.componentType = componentType
        self.componentList = []

        self.outer = ttk.Frame(self)
        self.outer.pack(expand=True, fill="x")

        sectionNameLabel = ttk.Label(self.outer, text=self.sectionName, anchor="center")
        sectionNameLabel.pack()

        self.inner = ttk.Frame(self.outer)
        self.inner.pack()

        buttonText = "Add " + self.componentType
        addButton = ttk.Button(self.outer, text=buttonText, command=self.__addComponent)
        addButton.pack(expand=True, fill="x")
    #end init


    def __addComponent(self):
        print("Adding %s to %s..." % (self.componentType, self.sectionName))

        ComponentFrame(self)

        if self.componentType is "trigger":
            self.componentList[-1].missionComponent = self.app.activeMission.addTrigger()
            #print(self.componentList[-1].missionComponent)
            self.editComponent(self.componentList[-1])

        print("Done.")
    #end __addComponent


    def deleteComponent(self, component):
        print("Removing %s from %s..." % (self.componentType, self.sectionName))

        if self.componentType is "trigger":
            self.app.activeMission.removeTrigger(component.missionComponent)
        self.componentList.remove(component)
        component.pack_forget()
        component.destroy()

        print("Done.")
    #end deleteComponent


    def editComponent(self, component):
        print("Editing ", end="")
        print(component.missionComponent, end="")
        print("...")
        if self.componentType is "trigger":
            TriggerWindow(self.app, self.app.gui, component.missionComponent)
    #end editComponent

#end class AggregatedComponentFrame


class ComponentFrame(object):

    def __init__(self, master):
        self.missionComponent = None

        componentFrame = ttk.Frame(master.inner)
        componentFrame.pack()

        #labelText = "%s %d" % (master.componentType, len(master.componentList))
        label = ttk.Label(componentFrame, text=master.componentType, anchor="w")
        label.grid(row=0, column=0, sticky="ew")

        master.componentList.append(componentFrame)

        editButton = ttk.Button(componentFrame, text="edit", command=lambda: master.editComponent(componentFrame))
        editButton.grid(row=0, column=1)

        deleteButton = ttk.Button(componentFrame, text="X", command=lambda: master.deleteComponent(componentFrame))
        deleteButton.grid(row=0, column=2)
    #end init

#end class ComponentFrame


class TriggerWindow(object):

    def __init__(self, app, master, trigger):
        print("\tBuilding TriggerWindow...")

        self.app = app
        self.trigger = trigger

        self.top = Toplevel(master)
        self.top.title("Edit Trigger")
        self.top.configure(bg="#ededed")
        self.top.grab_set()  # freezes the app until the user enters or cancels

        outer = ttk.Frame(self.top)
        outer.pack(side=TOP)

        self.leftFrame = ttk.Frame(outer)
        self.leftFrame.pack(side=LEFT)

        self.rightFrame = ttk.Frame(outer)
        self.rightFrame.pack(side=RIGHT)

        self.closeButton = ttk.Button(self.top, text="Ok", command=self.cleanup)
        self.closeButton.pack(side=BOTTOM)

        # declare all the variables in one place

        #TODO: find a way to support "on enter <system>"
        self.action = None
        actionsList = ["offer", "complete", "accept", "decline", "defer", "fail", "visit", "stopover"]



        ### BUILDING LEFT FRAME ###

        ## on action
        onLabel = ttk.Label(self.leftFrame, text="on", width=6)
        onLabel.grid(row=0, column=0, sticky="w", padx=(5,0))

        self.onActionCombobox = ttk.Combobox(self.leftFrame, state="readonly", values=actionsList)
        self.onActionCombobox.bind("<<ComboboxSelected>>", self.actionSelected)
        self.onActionCombobox.grid(row=0, column=1, sticky="ew")

        self.dialogSubComponent = buildMandOptFrame(self.leftFrame, "dialog", 1, 0, ["<text>"])
        self.dialogSubComponent.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.outfitSubComponent = buildMandOptFrame(self.leftFrame, "outfit", 1, 1, ["<outfit>", "[<number#>]"])
        self.outfitSubComponent.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.requireSubComponent = buildMandOptFrame(self.leftFrame, "require", 1, 1, ["<outfit>", "[<number#>]"])
        self.requireSubComponent.grid(row=3, column=0, columnspan=2, sticky="ew")

        self.paymentSubComponent = buildMandOptFrame(self.leftFrame, "payment", 0, 2, ["[<base#>]", "[<multiplier#>]"])
        self.paymentSubComponent.grid(row=4, column=0, columnspan=2, sticky="ew")

        self.eventSubComponent = buildMandOptFrame(self.leftFrame, "event", 1, 2, ["<name>", "[<delay#>]", "[<max#>]"])
        self.eventSubComponent.grid(row=5, column=0, columnspan=2, sticky="ew")

        self.failSubComponent = buildMandOptFrame(self.leftFrame, "fail", 0, 1, ["[<name>]"])
        self.failSubComponent.grid(row=6, column=0, columnspan=2, sticky="ew")

        self.logs = AggregatedComponentFrame(self.app, self.leftFrame, "Logs", "log")
        self.logs.grid(row=7, column=0, columnspan=2, sticky="ew")

        ### DONE BUILDING LEFT FRAME ###


        # build the right frame
        testR = ttk.Label(self.rightFrame, text="RightSideFrame")
        testR.pack()

        print("\tDone.")
    #end init


    def actionSelected(self, event):
        self.action = self.onActionCombobox.get()
        print('\nTrigger action selected: "on %s"' % self.action)
    #end actionSelected


    def cleanup(self):
        self.storeData()
        self.top.grab_release()  # HAVE TO RELEASE
        self.top.destroy()
    #end cleanup


    def storeData(self):
        #TODO: IMPLEMENT THIS NEXT
        print("In Progress!")
    #end storeData

#end class TriggerWindow


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

    #end init

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
        print("\t\tBuilding \"%s\"" % self.subComponentName)
        label1 = ttk.Label(self, text=self.subComponentName, width=7)
        label1.grid(row=self.rowNum, column=0, sticky="w", padx=(5,0))

        # Case 1: No mandatory fields
        if self.numMandatory is 0:
            print("\t\t\tNo mandatory fields")

            self.listEntryStates.append(BooleanVar())
            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].configure(command=lambda: self.cbValueChanged(self.listEntryStates[0],
                                                                                   [self.subComponentName]))
            self.listCheckbuttons[0].grid(row=self.rowNum, column=2, sticky="e")
            self.rowNum += 1
        # Case 2: 1 mandatory field
        elif self.numMandatory is 1:
            print("\t\t\t1 mandatory field")

            self.listEntryStates.append(BooleanVar())
            self.listEntryData.append(StringVar())
            self.listEntryData[0].set(self.listDefaultEntryData[0])

            self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[0], state=DISABLED, style='D.TEntry'))
            self.listEntries[0].grid(row=0, column=1, sticky="ew")

            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0]))
            self.listCheckbuttons[0].configure(command=partial(self.cbValueChanged, self.listEntryStates[0], [self.listEntries[0]]))
            self.listCheckbuttons[0].grid(row=self.rowNum, column=2, sticky="e")
            self.rowNum += 1
        # Case 3: More than 1 mandatory field
        elif self.numMandatory > 1:
            print("\t\t\t%d mandatory fields" % self.numMandatory)

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
            #end for
            self.listCheckbuttons[0].configure(command=partial(self.cbValueChanged, self.listEntryStates[0], self.listEntries[:self.numMandatory]))
        #end if/else

        # add the optional fields
        for i in range(self.numMandatory, self.numFields):
            self.listEntryStates.append(BooleanVar())
            self.listEntryData.append(StringVar())
            self.listEntryData[-1].set(self.listDefaultEntryData[i])

            self.listEntries.append(ttk.Entry(self, textvariable=self.listEntryData[-1], state=DISABLED, style="D.TEntry"))
            self.listEntries[-1].grid(row=self.rowNum, column=1, sticky="ew")

            # We have to use functools.partial here because lambda can't be used inside a loop
            self.listCheckbuttons.append(ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[-1],
                                                         command=partial(self.cbValueChanged, self.listEntryStates[-1],
                                                                                             [self.listEntries[-1]])))
            self.listCheckbuttons[-1].grid(row=self.rowNum, column=2, sticky="e")

            self.rowNum += 1
        # end for

    #end build


    def cbValueChanged(self, entryState, modifiedWidgets):

        for widget in modifiedWidgets:
            print("The value of %s is:" % widget, end="\t\t")
            print(entryState.get())
            if type(widget) is str:
                break
            elif entryState.get() is True:
                widget.config(state='enabled', style='TEntry')
            elif entryState.get() is False:
                widget.config(state='disabled', style='D.TEntry')
        #end for

    #end cbValueChanged

#end class _SubComponentMandOptFrame