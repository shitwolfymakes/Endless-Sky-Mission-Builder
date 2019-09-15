""" AggregatedTriggerFrame.py
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

from src.gui.guiutils import *
from src.widgets import TriggerWindow


class AggregatedTriggerFrame(ttk.Frame):
    """
    This class extends ttk.Frame, allowing the user to add an arbitrary number of TriggerFrame widgets to the GUI.
    """

    def __init__(self, app, parent):
        ttk.Frame.__init__(self, parent)

        self.app              = app
        self.parent           = parent
        self.triggerFrameList = []

        self.outer = ttk.Frame(self)
        self.outer.pack(expand=True, fill="x")

        section_name_label = ttk.Label(self.outer, text="Triggers", anchor="center")
        section_name_label.pack()

        self.inner = ttk.Frame(self.outer)
        self.inner.pack(expand=True, fill="x")

        add_button = ttk.Button(self.outer, text="Add Trigger", command=self._add_trigger)
        add_button.pack(expand=True, fill="x")
    #end init


    def _add_trigger(self):
        """Add a trigger to the activeMission"""
        logging.debug("Adding Trigger...")

        tf = TriggerFrame(self, self.app, "trigger")
        self.edit_trigger(self.triggerFrameList[-1])

        state = BooleanVar()
        cb = ttk.Checkbutton(tf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_trigger_state, state, self.triggerFrameList[-1].trigger))
        cb.grid(row=0, column=3, sticky="e")
    #end _add_trigger


    def delete_trigger(self, trigger_frame):
        """
        This method uses the data stored in the trigger_frame to remove the associated Trigger object from the
            activeMission. Once that is completed, it removes the trigger_frame TriggerFrame widget from the GUI.

        :param trigger_frame: The TriggerFrame to be removed
        """
        logging.debug(str.format("Removing %s from Triggers" % trigger_frame.trigger))

        self.app.activeMission.remove_trigger(trigger_frame.trigger)

        self.triggerFrameList.remove(trigger_frame)
        trigger_frame.frame.pack_forget()
        trigger_frame.frame.destroy()
    #end delete_trigger


    def edit_trigger(self, trigger_frame):
        """
        This method uses the data stored in the trigger_frame to edit the data stored in the associated
        Trigger object.

        :param trigger_frame: The TriggerFrame containing the trigger to be edited
        """
        logging.debug("Editing %s..." % str(trigger_frame.trigger))
        TriggerWindow(self.app, self.app.gui, trigger_frame.trigger)
    #end edit_trigger


    def populate_trigger(self, trigger):
        """
        This method populates the GUI with a TriggerFrame widget, then stores the data from trigger inside it

        :param trigger: the trigger containing the data to be populated
        """
        tf = TriggerFrame(self, self.app, "trigger", populating=True)
        tf.trigger = trigger

        state = BooleanVar()
        cb = ttk.Checkbutton(tf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_trigger_state, state, trigger))
        cb.grid(row=0, column=3, sticky="e")

        if trigger.isActive:
            state.set(1)
            self._change_trigger_state(state, trigger)
    #end populate_trigger


    @staticmethod
    def _change_trigger_state(state, trigger):
        """
        Set trigger to state
        :param state: the state of the trigger
        :param trigger: the trigger
        """
        trigger.isActive = state.get()
        logging.debug("%s is now %s" % (str(trigger), str(trigger.isActive)))
    #def _change_trigger_state

#end class AggregatedTriggerFrame


class TriggerFrame(ttk.Frame):
    """This class extends ttk.Frame to create a custom GUI widget"""

    def __init__(self, master, app, name, populating=False):
        ttk.Frame.__init__(self, master)
        self.trigger = None
        if not populating:
            self.trigger = app.activeMission.add_trigger()
        self.master  = master

        self.frame = ttk.Frame(master.inner)
        self.frame.pack(expand=True, fill="x")
        self.frame.grid_columnconfigure(0, weight=1)

        name = name.title()
        label = ttk.Label(self.frame, text=name)
        label.grid(row=0, column=0, sticky="ew", padx=(5, 0))

        self.master.triggerFrameList.append(self)

        edit_button = ttk.Button(self.frame, text="edit", width=3, command=partial(self.master.edit_trigger, self))
        edit_button.grid(row=0, column=1)

        delete_button = ttk.Button(self.frame, text="X", width=0, command=partial(self.master.delete_trigger, self))
        delete_button.grid(row=0, column=2)
    #end init

    def _cleanup(self):
        self.master.delete_trigger(self)
    #end _cleanup

#end class TriggerFrame


