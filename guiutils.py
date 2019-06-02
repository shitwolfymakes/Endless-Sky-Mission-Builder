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

This file contains helper functions for the ESMB gui, so that they don't need to be rewritten,
    or worse, imported from the gui components themselves

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
        label1 = ttk.Label(self, text=self.subComponentName, width=5)
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