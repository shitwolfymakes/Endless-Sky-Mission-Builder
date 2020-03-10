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

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.parent = parent
        self.cmof_frame_list = []
    #end init
#end AggregatedComponentMandOptFrame
