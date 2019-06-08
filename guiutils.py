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


class TriggerWindow(object):

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

        self.closeButton = ttk.Button(self.top, text="Ok", command=self.cleanup)
        self.closeButton.pack(side=BOTTOM)

        # declare all the variables in one place

        #TODO: find a way to support "on enter <system>"
        self.action = None
        self.actionsList = ["offer", "complete", "accept", "decline", "defer", "fail", "visit", "stopover"]



        ### BUILDING LEFT FRAME ###

        ## on action
        onLabel = ttk.Label(self.leftFrame, text="on", width=6)
        onLabel.grid(row=0, column=0, sticky="w", padx=(5,0))

        self.onActionCombobox = ttk.Combobox(self.leftFrame, state="readonly", values=self.actionsList)
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

        self.logsSubComponent = AggregatedLogFrame(self.app, self.leftFrame, self.trigger)
        self.logsSubComponent.grid(row=7, column=0, columnspan=2, sticky="ew")

        ### DONE BUILDING LEFT FRAME ###

        ### BUILDING RIGHT FRAME###

        # Conditions (inside Trigger)
        self.triggerConditionsSubComponent = AggregatedTriggerConditionsFrame(self.app, self.rightFrame, self.trigger)
        self.triggerConditionsSubComponent.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.populateTriggerWindow()

        print("\tDone.")
    #end init


    def actionSelected(self, event):
        self.action = self.onActionCombobox.get()
        print('\nTrigger action selected: "on %s"' % self.action)
    #end actionSelected


    def cleanup(self):
        self.storeData()
        self.app.activeTrigger = None
        self.top.grab_release()  # HAVE TO RELEASE
        self.top.destroy()
    #end cleanup


    def storeData(self):
        print("\nStoring TriggerWindow data...")
        self.trigger.clearTrigger()

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

        self.trigger.printTrigger()

        print("Done.")
    #end storeData

    def populateTriggerWindow(self):
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
            component.cbValueChanged(self.dialogSubComponent.listEntryStates[0], [self.dialogSubComponent.listEntries[0]])
            component.listEntryData[0].set(self.trigger.dialog)
        #end if

        # outfit
        component = self.outfitSubComponent
        for i, data in enumerate(self.trigger.outfit):
            if data is not None:
                component.listEntryStates[i].set(1)
                component.cbValueChanged(component.listEntryStates[i], [component.listEntries[i]])
                component.listEntryData[i].set(data)
            #end if
        #end for

        # require
        component = self.requireSubComponent
        for i, data in enumerate(self.trigger.require):
            if data is not None:
                component.listEntryStates[i].set(1)
                component.cbValueChanged(component.listEntryStates[i], [component.listEntries[i]])
                component.listEntryData[i].set(data)
            #end if
        #end for

        # payment
        if self.trigger.isPayment:
            component = self.paymentSubComponent
            component.listEntryStates[0].set(1)
            component.cbValueChanged(component.listEntryStates[0], [component.subComponentName])

            for i, data in enumerate(self.trigger.payment):
                if data is not None:
                    component.listEntryStates[i+1].set(1)
                    component.cbValueChanged(component.listEntryStates[i+1], [component.listEntries[i]])
                    component.listEntryData[i].set(data)
                # end if
            # end for

        # event
        component = self.eventSubComponent
        for i, data in enumerate(self.trigger.event):
            if data is not None:
                component.listEntryStates[i].set(1)
                component.cbValueChanged(component.listEntryStates[i], [component.listEntries[i]])
                component.listEntryData[i].set(data)
            #end if
        #end for

        # fail
        component = self.failSubComponent
        if self.trigger.isFail:
            component.listEntryStates[0].set(1)
            component.cbValueChanged(component.listEntryStates[0], [component.subComponentName])

            if self.trigger.fail is not None:
                component.listEntryStates[1].set(1)
                component.cbValueChanged(component.listEntryStates[1], [component.listEntries[0]])
                component.listEntryData[0].set(self.trigger.fail)
            #end if
        #end if

        # Logs
        component = self.logsSubComponent
        if self.trigger.logs:
            for log in self.trigger.logs:
                component.populateLog(log)
            #print
        #end if

        print("Done.")
    #end populateTriggerWindow

#end class TriggerWindow


class AggregatedLogFrame(ttk.Frame):

    def __init__(self, app, parent, trigger):
        ttk.Frame.__init__(self, parent)

        self.app          = app
        self.parent       = parent
        self.trigger      = trigger
        self.logFrameList = []

        self.outer = ttk.Frame(self)
        self.outer.pack(expand=True, fill="x")

        sectionNameLabel = ttk.Label(self.outer, text="Logs", anchor="center")
        sectionNameLabel.pack()

        self.inner = ttk.Frame(self.outer)
        self.inner.pack(expand=True, fill="x")

        addButton = ttk.Button(self.outer, text="Add Log", command=self.__addLog)
        addButton.pack(expand=True, fill="x")
    #end init


    def __addLog(self):
        print("Adding Trigger...")

        lf = LogFrame(self, self.trigger, "log")
        TypeSelectorWindow(self, ["<type> <name> <message>", "<message>"], self.setFormatType)

        if lf.log.formatType == "cancelled":
            lf.cleanup()
            return
        #end if
        self.editLog(self.logFrameList[-1])


        state = BooleanVar()
        cb = ttk.Checkbutton(lf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self.changeLogState, state, self.logFrameList[-1].log))
        cb.grid(row=0, column=3, sticky="e")

        print("Done.")
    #end __addLog


    def editLog(self, logFrame):
        print("Editing ", logFrame.log, "...")
        LogWindow(self.app, self.app.gui, logFrame.log, logFrame.log.formatType)
    #end editLog


    def deleteLog(self, logFrame):
        print("Removing %s from Triggers" % logFrame.log)

        self.trigger.removeLog(logFrame.log)

        self.logFrameList.remove(logFrame)
        logFrame.frame.pack_forget()
        logFrame.frame.destroy()

        print("Done.")
    #end deleteLog


    def populateLog(self, log):
        lf = LogFrame(self, self.trigger, "log", populating=True)
        lf.log = log

        state = BooleanVar()
        cb = ttk.Checkbutton(lf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self.changeLogState, state, log))
        cb.grid(row=0, column=3, sticky="e")

        if log.isActive:
            state.set(1)
            self.changeLogState(state, log)
    #end populateLog


    @staticmethod
    def changeLogState(state, log):
        log.isActive = state.get()
        print(log, "is now", log.isActive)
    #def changeTriggerState


    def setFormatType(self, formatType):
        self.logFrameList[-1].log.formatType = formatType
    #end setFormatType

#end class AggregatedLogFrame


class LogFrame(object):

    def __init__(self, master, trigger, name, populating=False):
        self.log = None
        if not populating:
            self.log = trigger.addLog()
        self.master = master
        self.trigger = trigger

        self.frame = ttk.Frame(master.inner)
        self.frame.pack(expand=True, fill="x")
        self.frame.grid_columnconfigure(0, weight=1)

        label = ttk.Label(self.frame, text=name)
        label.grid(row=0, column=0, sticky="ew", padx=(5,0))

        self.master.logFrameList.append(self)

        editButton = ttk.Button(self.frame, text="edit", width=3, command=partial(self.master.editLog, self))
        editButton.grid(row=0, column=1)

        deleteButton = ttk.Button(self.frame, text="X", width=0, command=partial(self.master.deleteLog, self))
        deleteButton.grid(row=0, column=2)
    #end init


    def cleanup(self):
        self.master.deleteLog(self)

#end class LogFrame


class TypeSelectorWindow(Toplevel):

    def __init__(self, master, options, callback, **kwargs):
        self.callback = callback
        super().__init__(master, **kwargs)

        self.optionList = ttk.Combobox(self, values=options, state="readonly")
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


class LogWindow(object):

    def __init__(self, app, master, log, formatType):
        print("\tBuilding LogWindow...")

        self.app        = app
        self.log        = log
        self.formatType = formatType
        self.logGroup   = StringVar()
        self.name       = StringVar()
        self.message    = StringVar()

        self.top = Toplevel(master)
        self.top.title("Edit Log")
        self.top.configure(bg="#ededed")
        self.top.grab_set()  # freezes the app until the user enters or cancels

        frame = ttk.Frame(self.top)
        frame.pack(side=TOP)

        if formatType == "<message>":
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

        self.populateLogWindow()

        print("\tDone.")
    #end init


    def cleanup(self):
        self.storeData()
        self.top.grab_release()  # HAVE TO RELEASE
        self.top.destroy()
    #end cleanup


    def storeData(self):
        print("\nStoring LogWindow data...", end="\t")
        self.log.clearLog()

        if self.formatType == "<message>":
            self.log.log[0] = self.message.get()
        else:
            self.log.log[0] = self.logGroup.get()
            self.log.log[1] = self.name.get()
            self.log.log[2] = self.message.get()
        #end if/else

        self.log.printLog()

        print("Done.")
    #end storeData


    def populateLogWindow(self):
        print("Populating TriggerWindow...", end="\t")

        if self.formatType == "<message>":
            if self.log.log[0] is not None:
                self.message.set(self.log.log[0])
        else:
            if self.log.log[0] is not None:
                self.logGroup.set(self.log.log[0])
            if self.log.log[1] is not None:
                self.name.set(self.log.log[1])
            if self.log.log[2] is not None:
                self.message.set(self.log.log[2])
        #end if/else

        print("Done.")
    #end populateLogWindow

#end class LogWindow


class AggregatedTriggerConditionsFrame(ttk.Frame):

    def __init__(self, app, parent, trigger):
        ttk.Frame.__init__(self, parent)

        self.app          = app
        self.parent       = parent
        self.trigger      = trigger
        self.tcFrameList  = []

        self.outer = ttk.Frame(self)
        self.outer.pack(expand=True, fill="x")

        sectionNameLabel = ttk.Label(self.outer, text="Conditions", anchor="center")
        sectionNameLabel.pack()

        self.inner = ttk.Frame(self.outer)
        self.inner.pack(expand=True, fill="x")

        addButton = ttk.Button(self.outer, text="Add Condition", command=self.__addTC)
        addButton.pack(expand=True, fill="x")
    #end init


    def __addTC(self):
        print("Adding TriggerCondition...")

        tc = TriggerConditionFrame(self, self.trigger, "log")
        TypeSelectorWindow(self, ["<type> <name> <message>", "<message>"], self.setFormatType)

        if tc.condition.conditionType == "cancelled":
            tc.cleanup()
            return
        #end if
        self.editTC(self.tcFrameList[-1])


        state = BooleanVar()
        cb = ttk.Checkbutton(tc.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self.changeTCState, state, self.tcFrameList[-1].log))
        cb.grid(row=0, column=3, sticky="e")

        print("Done.")
    #end __addTC


    def editTC(self, tcFrame):
        print("Editing ", tcFrame.condition, "...")
        TriggerConditionWindow(self.app, self.app.gui, tcFrame.condition, tcFrame.condition.conditionType)
    #end editTC


    def deleteTC(self, tcFrame):
        print("Removing %s from Triggers" % tcFrame.condition)

        self.trigger.removeLog(tcFrame.condition)

        self.tcFrameList.remove(tcFrame)
        tcFrame.frame.pack_forget()
        tcFrame.frame.destroy()

        print("Done.")
    #end deleteTC


    def populateTC(self, tc):
        tc = TriggerConditionFrame(self, self.trigger, "log", populating=True)
        tc.condition = tc

        state = BooleanVar()
        cb = ttk.Checkbutton(tc.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self.changeTCState, state, tc))
        cb.grid(row=0, column=3, sticky="e")

        if tc.isActive:
            state.set(1)
            self.changeTCState(state, tc)
    #end populateTC


    @staticmethod
    def changeTCState(state, tc):
        tc.isActive = state.get()
        print(tc, "is now", tc.isActive)
    #def changeTriggerConditionsState


    def setFormatType(self, formatType):
        self.tcFrameList[-1].condition.conditionType = formatType
    #end setFormatType

#end class AggregatedTriggerConditionsFrame