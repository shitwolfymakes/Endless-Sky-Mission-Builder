""" AggregatedDialogFrame.py
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

import src.widgets as widgets


class AggregatedDialogFrame(widgets.AggregatorFrame):
    """
    This class extends ttk.Frame, allowing the user to add an arbitrary number of TriggerFrame widgets to the GUI.
    """

    def __init__(self, parent):
        logging.debug("\t\tBuilding AggregatedDialogFrame")
        widgets.AggregatorFrame.__init__(self, parent, "Dialog")
    #end init


    def add_frame(self):
        df = widgets.DialogFrame(self)
        self.frame_list.append(df)
        print(self.frame_list)
    #end _add_dialog


    def delete_frame(self, frame):
        self.frame_list.remove(frame)
        frame.frame.pack_forget()
        frame.frame.destroy()
        print(self.frame_list)
        for d in self.frame_list:
            print(d.data.get())
    #end _delete_dialog
#end class
