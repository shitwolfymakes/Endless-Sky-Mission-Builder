""" AggregatedComponentMandOptFrame.py
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

from tkinter import ttk


class AggregatedComponentMandOptFrame(ttk.Frame):
    """
    This class extends ttk.Frame, allowing the user to add an arbitrary
    number of ComponentMandOptFrame widgets to the GUI.
    """

    def __init__(self, parent, title):
        ttk.Frame.__init__(self, parent)

        self.parent = parent
        self.cmof_frame_list = []

        self.outer = ttk.Frame(self)
        self.outer.pack(expand=True, fill="x")

        section_name_label = ttk.Label(self.outer, text=title, anchor="center")
        section_name_label.pack()

        self.inner = ttk.Frame(self.outer)
        self.inner.pack(expand=True, fill="x")

        add_button = ttk.Button(self.outer, text="Add %s" % title, command=self._add_cmof)
        add_button.pack(expand=True, fill="x")
    #end init


    def _add_cmof(self):
        pass
    #end _add_cmof


    def remove_cmof(self):
        pass
    #end remove_cmof
#end AggregatedComponentMandOptFrame
