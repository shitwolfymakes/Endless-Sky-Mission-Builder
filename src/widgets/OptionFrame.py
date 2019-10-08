""" OptionFrame.py
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


class OptionFrame(ttk.Frame):
    """This frame contains user functions for navigating ESMB"""
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        logging.debug("\tInitializing OptionFrame...")
        self.mfo = config.mission_file_objects
        self.option_frame = self

        title = ttk.Label(self.option_frame, text="Mission File Objects")
        title.pack()

        obj_names = self.mfo.get_names()
        self.combo_box = ttk.Combobox(self.option_frame, state="readonly", values=obj_names)
        self.combo_box.bind("<<ComboboxSelected>>", self.obj_selected)
        self.combo_box.pack()
        if config.debugging:
            self.combo_box.current(0)

        self.add_buttons()
    #end init


    def obj_selected(self, event=None):
        """Set active_object to the combobox option selected by the user"""
        selected_name = self.combo_box.get()
        logging.debug("Opening object \"%s\"" % selected_name)
        config.active_object = self.mfo.get_object(selected_name)

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
        self.delete_current_object_button()
    #end add_buttons


    def add_new_button(self):
        new_button = ttk.Button(self.option_frame,
                                text="New",
                                command=partial(utils.new_mission, self))
        new_button.pack(fill='x')
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
                                      command=partial(utils.open_file, self))
        open_file_button.pack(fill='x')
    #end add_open_file_button


    def add_compile_button(self):
        compile_obj_button = ttk.Button(self.option_frame,
                                        text="Compile",
                                        command=partial(utils.compile_mission, self))
        compile_obj_button.pack(fill='x')
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
    #end add_change_name_button


    def delete_current_object_button(self):
        # TODO: Implement this
        pass
    #end delete_current_object_button


    def update_frame(self):
        logging.debug("Updating option_frame...")
        logging.debug("\tCombobox options: %s" % str(self.mfo.get_names))

        self.combo_box['values'] = self.mfo.get_names()
        current_object = self.mfo.objects_list.index(config.active_object.name)
        self.combo_box.current(current_object)

        config.gui.update_center_frame()
        config.gui.update_mission_frame()
    #end update_frame
#end class OptionFrame
