""" ItemTextFrame.py
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


class ItemTextFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        logging.debug("\tInitializing OutputTextFrame...")
        self.item_text_frame = self

        title = ttk.Label(self.item_text_frame, text="Item Text")
        title.pack()

        self.text_box = Text(self.item_text_frame, wrap=WORD, height=50, width=100)
        self.text_box.pack(expand=1, fill='both')
        #TODO: Rewrite welcome message
        self._add_welcome_message()
        self.text_box.config(state=DISABLED)
    #end def


    def _add_welcome_message(self):
        welcome_message = "\n\t\t\tWelcome to Endless Sky Mission Builder!\n"
        welcome_message += "\n\t - Click \"New Mission\" to get started\n"
        welcome_message += "\n\t - Click \"Save Mission File\" to save all the missions to a text file\n"
        welcome_message += "\n\t - Click \"Open Mission File\" to open a mission file for editing\n"
        welcome_message += "\n\t - Click \"Compile Mission\" to save save the current mission\n"
        welcome_message += "\n\t - Click \"Help\" to be directed to the Mission Creation wiki\n"
        self.text_box.insert(END, welcome_message)
    #end _add_welcome_message


    def update_frame(self):
        logging.debug("Updating text_frame...")

        self.text_box.forget()
        self.text_box = Text(self.item_text_frame, height=50, width=100, wrap=WORD)
        self.text_box.pack()
        self.text_box.insert(END, config.active_item.print_item_lines_to_text())
        self.text_box.config(state=DISABLED)
    #end update_frame
#end OutputTextFrame
