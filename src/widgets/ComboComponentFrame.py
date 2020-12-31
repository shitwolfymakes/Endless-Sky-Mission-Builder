""" ComboComponentFrame.py
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
from tkinter import ttk, BooleanVar

import widgets

class ComboComponentFrame(ttk.Frame):
    """This class extends ttk.Frame to create a custom GUI widget"""

    def __init__(self, parent, component_name, list_combobox_data, tooltip_key):
        ttk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)

        logging.debug("\t\tBuilding \"%s\"" % component_name)
        label = widgets.TooltipLabel(self, tooltip_key, text=component_name)
        label.grid(row=0, column=0, sticky="w", padx=(5, 0))

        self.listComboboxData = list_combobox_data
        self.is_active = BooleanVar()
        self.option   = None

        self.button   = ttk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.is_active)
        self.combo    = ttk.Combobox(self, state="disabled", values=self.listComboboxData, style='D.TCombobox')
        self.combo.bind("<<ComboboxSelected>>", self.option_selected)

        self.button.configure(command=partial(self._cb_value_changed, self.is_active, [self.combo]))
        self.button.grid(row=0, column=1, sticky="e")
        self.combo.grid(row=1, column=0, sticky="ew", padx=(20,0))
    #end init

    @staticmethod
    def _cb_value_changed(entry_state, modified_widgets):
        """
        Set each of the modified_widgets to entry_state

        :param entry_state: The boolean value of the entry
        :param modified_widgets: A list of widgets
        """
        for widget in modified_widgets:
            logging.debug("The value of %s is: %s" % (widget, entry_state.get()))
            if type(widget) is str:
                break
            elif entry_state.get() is True:
                widget.config(state='readonly', style='TCombobox')
            elif entry_state.get() is False:
                widget.config(state='disabled', style='D.TCombobox')
            # end if/else
        # end for
    # end cb_value_changed

    def option_selected(self, event=None):
        """Store the combobox option selected by the user"""
        selected_option = self.combo.get()
        logging.debug("\nOption selected: \"%s\"" % selected_option)
    #end mission_selected


    def set(self, data):
        """
        This method does the following:
                1) set the given entry state to 1
                2) set the combobox to the given data
                3) enable the given entry using cb_value_changed

        :param data: The data to be stored
        """
        self.is_active.set(1)
        self.combo.current(self.listComboboxData.index(data.title()))
        self._cb_value_changed(self.is_active, [self.combo])
    #end set


    def reset(self):
        """Reset the frame to defaults"""
        self.is_active.set(0)
        self.combo.current(None)
        self.combo.config(state='disabled', style='D.TCombobox')
    #end reset
#end class ComboComponentFrame
