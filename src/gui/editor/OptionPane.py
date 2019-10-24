""" OptionPane.py
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
from tkinter import ttk

import src.config as config
import src.utils as utils
from src.gui.editor import GUIPane


class OptionPane(ttk.Frame, GUIPane):
    """This frame contains user functions for navigating ESMB"""
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        logging.debug("\tInitializing OptionPane...")
        self.mfi = config.mission_file_items
        self.option_frame = self

        title = ttk.Label(self.option_frame, text="Mission File Items")
        title.pack()

        item_names = self.mfi.get_names()
        self.combo_box = ttk.Combobox(self.option_frame, state="readonly", values=item_names)
        self.combo_box.bind("<<ComboboxSelected>>", self.item_selected)
        self.combo_box.pack()
        if config.debugging:
            self.combo_box.current(0)

        self.add_buttons()
    #end init


    def item_selected(self, event=None):
        """Set active_item to the combobox option selected by the user"""
        selected_name = self.combo_box.get()
        logging.debug("Opening item \"%s\"" % selected_name)
        config.active_item = self.mfi.get_item(selected_name)

        config.gui.update_center_frame()
        config.gui.update_mission_frame()
    #end mission_selected


    def add_buttons(self):
        self.add_new_button()
        self.add_save_file_button()
        self.add_open_file_button()
        self.add_compile_button()
        self.add_help_button()
        self.add_change_name_button()
        self.delete_current_button()
    #end add_buttons


    def add_new_button(self):
        new_item_button = ttk.Button(self.option_frame,
                                     text="New Item",
                                     command=partial(utils.new_mission))
        new_item_button.pack(fill='x')
    #end add_new_button


    def add_save_file_button(self):
        save_file_button = ttk.Button(self.option_frame,
                                      text="Save Mission File",
                                      command=partial(utils.save_file, self))
        save_file_button.pack(fill='x')
    #end add_save_file_button


    def add_open_file_button(self):
        open_file_button = ttk.Button(self.option_frame,
                                      text="Open Mission File",
                                      command=partial(utils.open_file))
        open_file_button.pack(fill='x')
    #end add_open_file_button


    def add_compile_button(self):
        compile_item_button = ttk.Button(self.option_frame,
                                         text="Compile",
                                         command=partial(utils.compile_mission))
        compile_item_button.pack(fill='x')
    #end add_compile_button


    def add_help_button(self):
        help_button = ttk.Button(self.option_frame,
                                 text="Help",
                                 command=partial(utils.help_user))
        help_button.pack(fill='x')
    #end add_help_button


    def add_change_name_button(self):
        #TODO: Implement this
        pass
    #end add_change_item_name_button


    def delete_current_button(self):
        # TODO: Implement this
        pass
    #end delete_current_item_button


    def update_pane(self):
        logging.debug("Updating option_pane...")
        logging.debug("\tCombobox options: %s" % str(self.mfi.get_names()))

        self.combo_box['values'] = self.mfi.get_names()
        current_item = self.mfi.items_list.index(config.active_item)
        self.combo_box.current(current_item)

        config.gui.update_center_pane()
        config.gui.update_item_text_pane()
    #end update_pane
#end class OptionPane
