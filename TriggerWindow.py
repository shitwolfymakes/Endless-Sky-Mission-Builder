''' TriggerWindow.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

This class creates a new window, wherein the user enters all the data they want to use for the
    Trigger object that is passed in.

'''

from tkinter import *
from tkinter import ttk

from guiutils import buildMandOptFrame
from AggregatedComponentFrame import AggregatedComponentFrame

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