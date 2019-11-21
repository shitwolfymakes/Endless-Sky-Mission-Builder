""" GUI.py
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
from tkinter import ttk
from ttkthemes import ThemedTk

import src.gui.editor as editor
import src.config as config


class GUI:
    """This handles the GUI for ESMB"""

    def __init__(self):
        logging.debug("\tBuilding GUI...")

        # Build the application window
        self.gui = ThemedTk(theme="plastik")
        self.gui.title("ESMissionBuilder")
        self.gui.configure(bg="orange")

        # enable window resizing
        self.gui.columnconfigure(2, weight=1)
        self.gui.rowconfigure(0, weight=1)

        # set disabled styles
        self.disabledEntryStyle = ttk.Style()
        self.disabledEntryStyle.configure('D.TEntry', background='#D3D3D3')
        self.disabledComboboxStyle = ttk.Style()
        self.disabledComboboxStyle.configure('D.TCombobox', background='#D3D3D3')

        # Declare the frames
        self.option_pane = editor.OptionPane(self.gui)
        self.option_pane.grid(row=0, column=0, sticky="ns")

        self.center_pane = editor.MissionEditorPane(self.gui)
        self.center_pane.grid(row=0, column=1, sticky="ns")

        self.item_text_pane = editor.ItemTextPane(self.gui)
        self.item_text_pane.grid(row=0, column=2, sticky="nsew")

        config.gui = self
        self.gui.mainloop()
    #end init


    def update_option_pane(self):
        self.option_pane.update_pane()
    #end update_option_pane


    def update_center_pane(self):
        self.center_pane.update_pane()
    #end update_center_pane


    def update_item_text_pane(self):
        self.item_text_pane.update_pane()
    #end update_item_text_pane
#end class GUI
