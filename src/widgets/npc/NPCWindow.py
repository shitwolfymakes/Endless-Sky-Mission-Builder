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
from functools import partial
from tkinter import *
from tkinter import ttk

import src.widgets as widgets
from model.components import NPC
from src import config


class NPCWindow(Toplevel):
    """This class creates a custom pop-up window to display and edit the data in an associated NPC object"""

    def __init__(self, master, npc):
        logging.debug("\tBuilding NPCWindow...")
        super().__init__(master)

        self.npc = npc
        config.active_item = npc

        self.title("Edit NPC")
        self.configure(bg="#ededed")
        self.grab_set()  # freezes the app until the user enters or cancels

        outer = ttk.Frame(self)
        outer.pack(side=TOP)

        self.left_frame = ttk.Frame(outer)
        self.left_frame.pack(side=LEFT)

        self.right_frame = ttk.Frame(outer)
        self.right_frame.pack(side=RIGHT, anchor=N)

        self.center_frame = ttk.Frame(outer)
        self.center_frame.pack(side=RIGHT, anchor=N)

        self.close_button = ttk.Button(self, text="Ok", command=self._cleanup)
        self.close_button.pack(side=BOTTOM)

        ### BUILDING LEFT FRAME ###
        tags_list = ["save", "kill", "board", "assist", "disable", "scan cargo", "scan outfits", "evade", "accompany"]
        self.tags_frame = widgets.MultiOptionFrame(self.left_frame, "NPC tags", tags_list)
        self.tags_frame.grid(row=0, column=0, sticky="w", padx=(5, 0))

        personalities_list = ["staying", "entering", "waiting", "launching", "fleeing", "derelict", "uninterested"]
        self.personalities_frame = widgets.MultiOptionFrame(self.left_frame, "Personality Types", personalities_list)
        self.personalities_frame.grid(row=1, column=0, sticky="w", padx=(5, 0))

        self.confusion_component = widgets.ComponentMandOptFrame(self.left_frame, "Confusion", 1, 0, ["<#amount>"], "npc_confusion")
        self.confusion_component.grid(row=2, column=0, sticky="ew", padx=(5, 0))

        self.planet = widgets.ComponentMandOptFrame(self.left_frame, "Planet", 1, 0, ["<name>"], "npc_planet")
        self.planet.grid(row=3, column=0, sticky="ew", padx=(5, 0))

        ### BUILDING CENTER FRAME###
        # TODO: add system filter

        self.dialog = widgets.AggregatedDialogFrame(self.center_frame)
        self.dialog.grid(row=0, column=0, sticky="ew", padx=(5, 0))

        # TODO: add Conversation widget

        ### BUILDING RIGHT FRAME###
        #TODO: add tooltips to each of these
        self.ship = widgets.AggregatedSimpleEditorFrame(self.right_frame, "Ships", 2, 0, ["model", "name"], None)
        self.ship.grid(row=0, column=0, sticky="ew", padx=(5, 0))

        self.fleet = widgets.AggregatedSimpleEditorFrame(self.right_frame, "Fleets", 1, 1, ["name", "<count#>"], None)
        self.fleet.grid(row=1, column=0, sticky="ew", padx=(5, 0))

        self._populate_window()
    #end init


    def _cleanup(self):
        """Clean up whatever popups we've created"""
        self._store_data()
        config.active_trigger = None
        self.grab_release()  # HAVE TO RELEASE
        self.destroy()
    #end _cleanup


    def _store_data(self):
        pass
    #end _store_data


    def _populate_window(self):
        pass
    #end _populate_window
#end class NPCWindow


def main():
    root = Tk()
    button = ttk.Button(root, text="test NPCWindow", command=partial(pressed, root))
    button.pack()
    root.mainloop()


def pressed(root):
    npc = NPC("test npc")
    window = NPCWindow(root, npc)


if __name__ == "__main__":
    main()
