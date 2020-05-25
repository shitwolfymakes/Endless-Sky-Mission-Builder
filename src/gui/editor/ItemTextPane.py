""" ItemTextPane.py
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

import src.config as config
from src.gui.editor import GUIPane


class ItemTextPane(ttk.Frame, GUIPane):
    #TODO: add vertical and horizontal scrollbars
    #TODO: make it not wrap on word
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        logging.debug("\tInitializing ItemTextPane...")
        self.item_text_frame = self

        title = ttk.Label(self.item_text_frame, text="Item Text")
        title.pack()

        self.text_box = self._build_text_widget()
        self.text_box.pack(expand=1, fill='both')

        self._add_welcome_message()
        self.text_box.config(state=DISABLED)
    #end def


    def _add_welcome_message(self):
        welcome_message = "\n\t\t\tWelcome to Endless Sky Mission Builder!\n"
        welcome_message += "\n\t - Click \"New Item\" to create a new mission\n"
        welcome_message += "\n\t - Click \"Save Mission File\" to save all everything to a text file\n"
        welcome_message += "\n\t - Click \"Open Mission File\" to open a mission file for editing\n"
        welcome_message += "\n\t - Click \"Compile\" to save save the current mission\n"
        welcome_message += "\n\t - Click \"Help\" to be directed to the ESMB User Documentation\n"
        welcome_message += "\n\t - Click \"ES Wiki\" to be directed to the Endless Sky Mission Creation wiki\n"
        self.text_box.insert(END, welcome_message)
    #end _add_welcome_message


    def update_pane(self):
        logging.debug("Updating text_pane...")

        self.text_box.forget()
        self.text_box = self._build_text_widget()
        self.text_box.pack(expand=1, fill='both')
        self.text_box.insert(END, config.active_item.to_string())
        self.text_box.config(state=DISABLED)
    #end update_pane

    def _build_text_widget(self):
        text = Text(self.item_text_frame, height=50, width=100, wrap=WORD)#, wrap=NONE)
        return text
    #end _build_text_widget
#end ItemTextPane
