''' AggregatedTriggerFrame.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

This frame allows the user to add an arbitrary number of Trigger objects to the activeMission,
    and manipulate the data therein.

'''

from guiutils import *

class AggregatedTriggerFrame(ttk.Frame):

    def __init__(self, app, parent):
        ttk.Frame.__init__(self, parent)

        self.app              = app
        self.parent           = parent
        self.triggerFrameList = []

        self.outer = ttk.Frame(self)
        self.outer.pack(expand=True, fill="x")

        sectionNameLabel = ttk.Label(self.outer, text="Triggers", anchor="center")
        sectionNameLabel.pack()

        self.inner = ttk.Frame(self.outer)
        self.inner.pack(expand=True, fill="x")

        addButton = ttk.Button(self.outer, text="Add Trigger", command=self.__addComponent)
        addButton.pack(expand=True, fill="x")
    #end init


    def __addComponent(self):
        print("Adding Trigger...")

        tf = TriggerFrame(self, self.app, "trigger")
        self.editTrigger(self.triggerFrameList[-1])

        state = BooleanVar()
        cb = ttk.Checkbutton(tf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self.changeTriggerState, state, self.triggerFrameList[-1].trigger))
        cb.grid(row=0, column=3, sticky="e")

        print("Done.")
    #end __addTrigger


    def deleteTrigger(self, triggerFrame):
        print("Removing %s from Triggers" % triggerFrame.trigger)

        self.app.activeMission.removeTrigger(triggerFrame.trigger)

        self.triggerFrameList.remove(triggerFrame)
        triggerFrame.frame.pack_forget()
        triggerFrame.frame.destroy()

        print("Done.")
    #end deleteTrigger


    def editTrigger(self, triggerFrame):
        print("Editing ", end="")
        print(triggerFrame.trigger, end="")
        print("...")

        TriggerWindow(self.app, self.app.gui, triggerFrame.trigger)
    #end editTrigger


    def changeTriggerState(self, state, trigger):
        trigger.isActive = state.get()
        print(trigger, "is now", trigger.isActive)
    #def changeTriggerState

#end class AggregatedTriggerFrame


class TriggerFrame(ttk.Frame):

    def __init__(self, master, app, name):
        ttk.Frame.__init__(self, master)
        self.trigger = app.activeMission.addTrigger()
        self.master  = master

        self.frame = ttk.Frame(master.inner)
        self.frame.pack(expand=True, fill="x")
        self.frame.grid_columnconfigure(0, weight=1)

        name = name.title()
        label = ttk.Label(self.frame, text=name)
        label.grid(row=0, column=0, sticky="ew", padx=(5,0))

        self.master.triggerFrameList.append(self)

        editButton = ttk.Button(self.frame, text="edit", width=3, command=partial(self.master.editTrigger, self))
        editButton.grid(row=0, column=1)

        deleteButton = ttk.Button(self.frame, text="X", width=0, command=partial(self.master.deleteTrigger, self))
        deleteButton.grid(row=0, column=2)
    #end init

    def cleanup(self):
        self.master.deleteTrigger(self)
    #end cleanup

#end class TriggerFrame