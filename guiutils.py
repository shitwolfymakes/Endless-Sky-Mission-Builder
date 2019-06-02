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
        self.outer.pack()

        sectionNameLabel = ttk.Label(self.outer, text=self.sectionName, anchor="center")
        sectionNameLabel.pack()

        self.inner = ttk.Frame(self.outer)
        self.inner.pack()

        buttonText = "Add " + self.componentType
        addButton = ttk.Button(self.outer, text=buttonText, width=31, command=self.__addComponent)
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
        print(component.missionComponent)
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
        print("\tBuilding TriggerWindow...", end="\t\t")

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

        self.paymentSubComponent = buildMandOptFrame(self.leftFrame, "payment", 0, 2, ["<base#>", "[<multiplier#>]"])
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

        print("Done.")
    #end init


    def actionSelected(self, event):
        self.action = self.onActionCombobox.get()
        print('\nTrigger action selected: "on %s"' % self.action)
    #end actionSelected


    def cleanup(self):
        self.top.grab_release()  # HAVE TO RELEASE
        self.top.destroy()
    #end cleanup

#end class TriggerWindow


class _SubComponentMandOptFrame(ttk.Frame):

    def __init__(self, parent, subComponentName, numMandatory, numOptionals, listDefaultEntryData):
        ttk.Frame.__init__(self, parent)

        self.subComponentName     = subComponentName
        self.numMandatory         = numMandatory
        self.numOptionals         = numOptionals
        self.listDefaultEntryData = listDefaultEntryData

        self.rowNum     = 0
        self.numEntries = numMandatory + numOptionals


        self.listEntryStates  = []
        self.listCheckbuttons = []
        self.listEntryData    = []
        self.listEntries      = []

        self.build()

    #end init


    def build(self):
        label1 = ttk.Label(self, text=self.subComponentName, width=7)
        label1.grid(row=self.rowNum, column=0, sticky="w", padx=(5,0))
        if self.numMandatory is 0:
            self.listEntryStates.append(BooleanVar())

            cb = ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[0])
            cb.grid(row=self.rowNum, column=2, sticky="e")

            self.rowNum += 1
        #end if

        for i in range(0, self.numEntries):
            self.listEntryStates.append(BooleanVar())
            self.listEntryData.append(StringVar())
            self.listEntryData[i].set(self.listDefaultEntryData[i])

            entry = ttk.Entry(self, textvariable=self.listEntryData[i])
            entry.grid(row=self.rowNum, column=1, sticky="ew")

            cb = ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.listEntryStates[i])
            cb.grid(row=self.rowNum, column=2, sticky="e")

            self.rowNum += 1
        #end for

    #end build

    def addCheckbutton(self):
        print()
    #end addCheckbutton


    def addEntry(self):
        print()
    #end addEntry

#end class _SubComponentMandOptFrame