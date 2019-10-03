""" TooltipLabel.py
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

from tkinter import *
from tkinter import ttk

import src.config as config
from src.widgets.Tooltip import add_tooltip


class TooltipLabel(ttk.Label):
    """This widget extends ttk.Label, and displays a tooltip when the cursor hovers over it"""
    def __init__(self, parent, tooltip_dict_key, **kwargs):
        ttk.Label.__init__(self, parent, **kwargs)

        self.parent = parent
        self.tooltip_text = None

        self.fetch_tooltip_text(tooltip_dict_key)
        add_tooltip(self, self.tooltip_text)
    #end init


    def fetch_tooltip_text(self, tooltip_dict_key):
        self.tooltip_text = config.tooltips_dict.get(tooltip_dict_key)
    #end fetch_tooltip_text
#end class TooltipLabel


def main():
    config.tooltips_dict = {"tooltip_dict_key": "testing tooltip_dicts!"}
    root = Tk()
    label = TooltipLabel(root, "tooltip_dict_key", text="testing")
    label.pack()

    root.mainloop()



if __name__ == "__main__":
    main()
