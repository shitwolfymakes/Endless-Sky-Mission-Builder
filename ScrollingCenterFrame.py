""" ScrollingCenterFrame.py
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


class ScrollingCenterFrame(ttk.Frame):
    """This code provides for the center frame to resize as necessary to fit all the components in a mission"""

    def __init__(self, app, parent):
        ttk.Frame.__init__(self, parent)

        cf_title = ttk.Label(self, text="Mission Options")
        cf_title.pack()

        self.app = app
        self.parent = parent

        # create canvas and scrollbar
        self.vsb = ttk.Scrollbar(self, orient=VERTICAL)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.canvas = Canvas(self, highlightthickness=0, bg="#ededed", height=10, width=10)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.vsb.configure(command=self.canvas.yview)

        # add bindings for mousewheel
        self.canvas.bind("<Enter>", self._bind_mouse)
        self.canvas.bind("<Leave>", self._unbind_mouse)

        self.inner  = ttk.Frame(self.canvas)
        self.inner_id = self.canvas.create_window((4, 4), window=self.inner, anchor=NW)

        self.inner.bind("<Configure>", self._configure_inner)
        self.canvas.bind("<Configure>", self._configureCanvas)

    #end init


    def _bind_mouse(self, event=None):
        """Tell the canvas that the cursor is over it, so we can do scrolling"""
        self.canvas.bind_all("<4>", self._on_mousewheel)
        self.canvas.bind_all("<5>", self._on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
    #end _bind_mouse


    def _unbind_mouse(self, event=None):
        """Tell the canvas that the cursor is no longer over it"""
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")
    #end _unbind_mouse


    def _on_mousewheel(self, event):
        """Linux uses event.num; Windows / Mac uses event.delta"""
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")
        #end if/else
    #end _on_mousewheel


    def _configure_inner(self, event=None):
        """Resize the inner frame and scrollbars to make the screen scroll properly, even when you change the window"""
        # update the scrollbars to match the size of the inner frame
        bbox = self.canvas.bbox("all")
        self.canvas.config(scrollregion=bbox)

        if self.inner.winfo_reqwidth() >= self.canvas.winfo_width():
            # update the canvas's width to fit the inner frame only works before mainloop
            self.canvas.config(width=self.inner.winfo_reqwidth())
        #end if

        screen_h = self.winfo_screenheight()
        height = self.parent.winfo_rooty() + self.parent.winfo_height() - self.canvas.winfo_height() + self.inner.winfo_reqheight()

        if height < screen_h:
            self.canvas.configure(height=self.inner.winfo_reqheight())
    #end _configure_inner


    def _configureCanvas(self, event=None):
        """Resize the canvas if the inner frame changes"""
        if self.inner.winfo_reqwidth() < self.canvas.winfo_width():
            self.canvas.itemconfigure(self.inner_id, width=self.canvas.winfo_width())
        elif self.inner.winfo_reqwidth() > self.canvas.winfo_width():
            self.canvas.config(width=self.inner.winfo_reqwidth())
        #end if/else
    #end _configureCanvas

#end class ScrollingCenterFrame
