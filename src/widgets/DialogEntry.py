""" DialogEntry.py
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

from functools import partial
from tkinter import *
from tkinter import ttk

import src.widgets as widgets


class DialogEntry(ttk.Entry):
    """This class extends ttk.Frame to create a custom GUI widget"""

    def __init__(self, master):
        ttk.Entry.__init__(self, master)
        self.data = StringVar()
    #end init
#end class
