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

class TriggerWindow(object):

    def __init__(self, app, master, trigger):
        print("Building TriggerWindow...")

        self.app = app
        self.top = Toplevel(master)
        self.trigger = trigger

        print("Done.")
    #end init

#end class TriggerWindow