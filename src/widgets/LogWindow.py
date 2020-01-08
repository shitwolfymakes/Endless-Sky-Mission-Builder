""" LogWindow.py
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
from tkinter import *
from tkinter import ttk

import src.widgets as widgets


class LogWindow(Toplevel):
    """This class creates a custom pop-up window to display and edit the data in an associated Log object"""

    def __init__(self, master, log):
        #TODO: replace format_type with an integer
        logging.debug("\tBuilding LogWindow...")
        super().__init__(master)

        self.log = log
        self.format_type = log.format_type
        self.log_group = StringVar()
        self.name = StringVar()
        self.message = StringVar()
        self.group_entry = None
        self.name_entry = None
        self.message_entry = None

        self.title("Edit Log")
        self.configure(bg="#ededed")
        self.grab_set()  # freezes the app until the user enters or cancels

        frame = ttk.Frame(self)
        frame.pack(side=TOP)
        if self.format_type == "<message>":
            print("in here")
            label = widgets.TooltipLabel(frame, "log_message_only", text="Log")
            label.grid(row=0, column=0)

            self.message_entry = widgets.DefaultTextEntry(frame, "message", textvariable=self.message, width=30)
            self.message_entry.grid(row=1, column=0)
        else:
            label = widgets.TooltipLabel(frame, "log_complex", text="Log")
            label.grid(row=0, column=0)

            self.group_entry = widgets.DefaultTextEntry(frame, "<type>", textvariable=self.log_group, width=10)
            self.group_entry.grid(row=1, column=0)

            self.name_entry = widgets.DefaultTextEntry(frame, "name", textvariable=self.name, width=10)
            self.name_entry.grid(row=1, column=1)

            self.message_entry = widgets.DefaultTextEntry(frame, "message", textvariable=self.message, width=30)
            self.message_entry.grid(row=1, column=2)
        #end if/else

        self.close_button = ttk.Button(self, text="Ok", command=self.cleanup)
        self.close_button.pack(side=BOTTOM)

        self.populate_log_window()
    #end init


    def cleanup(self):
        """Clean up whatever popups we've created"""
        self._store_data()
        self.grab_release()  # HAVE TO RELEASE
        self.destroy()
    #end _cleanup


    def _store_data(self):
        """Store the data from the GUI into the associated Log object"""
        logging.debug("Storing LogWindow data...")
        self.log.clear_log()
        logging.debug("format_type: %s" % self.format_type)
        if self.format_type == "<message>":
            self.log.log[0] = self.message.get()
        else:
            self.log.log[0] = self.log_group.get()
            self.log.log[1] = self.name.get()
            self.log.log[2] = self.message.get()
        #end if/else
    #end store_data


    def populate_log_window(self):
        """Take the associated Trigger object, and populate each of the widgets in the window with the data inside"""
        logging.debug("Populating TriggerWindow...")

        if self.format_type == "<message>":
            if self.log.log[0] is not None:
                self.message_entry.set(self.log.log[0].lstrip('`').rstrip('`'))
        else:
            if self.log.log[0] is not None:
                self.group_entry.set(self.log.log[0])
            if self.log.log[1] is not None:
                self.name_entry.set(self.log.log[1])
            if self.log.log[2] is not None:
                self.message_entry.set(self.log.log[2].lstrip('`').rstrip('`'))
        #end if/else
    #end populate_log_window
#end class LogWindow
