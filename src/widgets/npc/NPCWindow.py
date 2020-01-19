""" NPCWindow.py
# Copyright (c) 2020 by Andrew Sneed
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
from src import config


class NPCWindow(Toplevel):
    """This class creates a custom pop-up window to display and edit the data in an associated NPC object"""

    def __init__(self, master, npc):
        logging.debug("\tBuilding NPCWindow...")
        super().__init__(master)

        self.npc = npc
        config.active_item = npc

        self.title("Edit Trigger")
        self.configure(bg="#ededed")
        self.grab_set()  # freezes the app until the user enters or cancels

        outer = ttk.Frame(self)
        outer.pack(side=TOP)

        self.left_frame = ttk.Frame(outer)
        self.left_frame.pack(side=LEFT)

        self.right_frame = ttk.Frame(outer)
        self.right_frame.pack(side=RIGHT, anchor=N)

        self.close_button = ttk.Button(self, text="Ok", command=self._cleanup)
        self.close_button.pack(side=BOTTOM)

        ### BUILDING LEFT FRAME ###
        #TODO: implement this

        ### BUILDING RIGHT FRAME###
        # TODO: implement this

        self._populate_window()
    #end init
#end class NPCWindow
