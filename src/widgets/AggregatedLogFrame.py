""" AggregatedLogFrame.py
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

import src.widgets as widgets


class AggregatedLogFrame(ttk.Frame):
    """This class extends ttk.Frame, allowing the user to add an arbitrary number of LogFrame widgets to the GUI."""

    def __init__(self, parent, trigger):
        ttk.Frame.__init__(self, parent)

        self.parent = parent
        self.trigger = trigger
        self.log_frame_list = []

        self.outer = ttk.Frame(self)
        self.outer.pack(expand=True, fill="x")

        section_name_label = ttk.Label(self.outer, text="Logs", anchor="center")
        section_name_label.pack()

        self.inner = ttk.Frame(self.outer)
        self.inner.pack(expand=True, fill="x")

        self.add_button = ttk.Button(self.outer, text="Add Log", command=self._add_log)
        self.add_button.pack(expand=True, fill="x")
    #end init


    def _add_log(self):
        """
        Add a log to the current trigger. We can assume a specific trigger because these functions are only accessible
        after has opened the trigger they are adding this log to.
        """
        logging.debug("Adding Trigger...")

        lf = widgets.LogFrame(self, self.trigger)
        widgets.TypeSelectorWindow(self, ["<type> <name> <message>", "<message>"], self._set_format_type)
        logging.debug("Log format type selected: %s" % lf.log.format_type)
        if lf.log.format_type == "cancelled":
            lf.cleanup()
            return
        #end if
        self.edit_log(self.log_frame_list[-1])

        state = BooleanVar()
        cb = ttk.Checkbutton(lf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_log_state, state, self.log_frame_list[-1].log))
        cb.grid(row=0, column=3, sticky="e")
    #end _add_log


    def edit_log(self, log_frame):
        """
        This method uses the data stored in the log_frame to edit the data stored in the associated
        Log object.

        :param log_frame: The LogFrame containing the log to be edited
        """
        logging.debug("Editing %s..." % str(log_frame.log))
        widgets.LogWindow(self, log_frame.log)
    #end edit_log


    def delete_log(self, log_frame):
        """
        This method uses the data stored in the log_frame to remove the associated Log object from the
        current trigger. Once that is completed, it removes the log_frame widget from the GUI.

        :param log_frame: The LogFrame to be removed
        """
        self.trigger.remove_log(log_frame.log)

        self.log_frame_list.remove(log_frame)
        log_frame.frame.pack_forget()
        log_frame.frame.destroy()

        logging.debug("Removed %s from Triggers" % str(log_frame.log))
    #end delete_log


    def populate_log(self, log):
        """
        This method populates the GUI with a LogFrame widget, then stores the data from log inside it

        :param log: the log containing the data to be populated
        """
        lf = widgets.LogFrame(self, self.trigger, populating=True)
        lf.log = log

        state = BooleanVar()
        cb = ttk.Checkbutton(lf.frame, onvalue=1, offvalue=0, variable=state)
        cb.configure(command=partial(self._change_log_state, state, log))
        cb.grid(row=0, column=3, sticky="e")

        if log.is_active:
            state.set(1)
            self._change_log_state(state, log)
    #end populate_log


    @staticmethod
    def _change_log_state(state, log):
        """
        Set log to state

        :param state: the state of the log
        :param log: the log
        """
        log.isActive = state.get()
        logging.debug("%s is now %s" % (str(log), str(log.isActive)))
    #def _change_trigger_state


    def _set_format_type(self, format_type):
        """
        Set the format of the log, so the code knows what to look for

        :param format_type:
        """
        self.log_frame_list[-1].log.format_type = format_type
    #end _set_format_type
# end class AggregatedLogFrame
