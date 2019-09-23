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


class LogWindow(object):
    """This class creates a custom pop-up window to display and edit the data in an associated Log object"""

    def __init__(self, app, master, log, format_type):
        #TODO: replace formatType with an integer
        logging.debug("\tBuilding LogWindow...")

        self.app        = app
        self.log        = log
        self.formatType = format_type
        self.logGroup   = StringVar()
        self.name       = StringVar()
        self.message    = StringVar()

        self.top = Toplevel(master)
        self.top.title("Edit Log")
        self.top.configure(bg="#ededed")
        self.top.grab_set()  # freezes the app until the user enters or cancels

        frame = ttk.Frame(self.top)
        frame.pack(side=TOP)

        if format_type == "<message>":
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

        self.populate_log_window()
    #end init


    def cleanup(self):
        """Clean up whatever popups we've created"""
        self._store_data()
        self.top.grab_release()  # HAVE TO RELEASE
        self.top.destroy()
    #end _cleanup


    def _store_data(self):
        """Store the data from the GUI into the associated Log object"""
        logging.debug("Storing LogWindow data...")
        self.log.clear_log()
        logging.debug("format_type: %s" % self.formatType)
        if self.formatType == "<message>":
            self.log.log[0] = self.message.get()
        else:
            self.log.log[0] = self.logGroup.get()
            self.log.log[1] = self.name.get()
            self.log.log[2] = self.message.get()
        #end if/else
    #end store_data


    def populate_log_window(self):
        """Take the associated Trigger object, and populate each of the widgets in the window with the data inside"""
        logging.debug("Populating TriggerWindow...")

        if self.formatType == "<message>":
            if self.log.log[0] is not None:
                self.message.set(self.log.log[0].lstrip('`').rstrip('`'))
        else:
            if self.log.log[0] is not None:
                self.logGroup.set(self.log.log[0])
            if self.log.log[1] is not None:
                self.name.set(self.log.log[1])
            if self.log.log[2] is not None:
                self.message.set(self.log.log[2].lstrip('`').rstrip('`'))
        #end if/else
    #end populate_log_window
#end class LogWindow
