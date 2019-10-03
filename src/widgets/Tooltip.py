""" Tooltip.py
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
import math
import tkinter as tk
from tkinter import ttk


class Tooltip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tooltip = None
        self.text = None
        self.x = 0
        self.y = 0
    #end init

    def show_tooltip(self, text):
        self.text = text
        if self.tooltip or not self.text:
            return

        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 45
        y = y + cy + self.widget.winfo_rooty() + 30

        self.tooltip = tooltip_window = tk.Toplevel(self.widget)
        tooltip_window.wm_overrideredirect(1)   # removes the default window hide/maximize/close buttons
        tooltip_window.wm_geometry("+%d+%d" % (x, y))

        self._add_tooltip_text(tooltip_window)
    #end show_tooltip

    def hide_tooltip(self):
        tooltip_window = self.tooltip
        self.tooltip = None
        if tooltip_window:
            tooltip_window.destroy()
    #end hide_tooltip


    def _add_tooltip_text(self, tooltip_window):
        tooltip = tk.Text(tooltip_window, relief=tk.SOLID, width=40, wrap=tk.WORD)
        height = math.ceil(len(self.text) / 40)
        tooltip.insert(tk.END, self.text)
        tooltip.config(state=tk.DISABLED, height=height)
        tooltip.pack(ipadx=1)
    #end _add_tooltip_text
#end class Tooltip


def add_tooltip(widget, text):
    tooltip = Tooltip(widget)

    def enter(event):
        tooltip.show_tooltip(text)
    #end enter

    def leave(event):
        tooltip.hide_tooltip()
    #end leave

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
#end add_tooltip
