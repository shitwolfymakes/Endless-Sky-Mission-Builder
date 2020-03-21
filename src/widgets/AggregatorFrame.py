""" AggregatorFrame.py
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
from functools import partial
from tkinter import *
from tkinter import ttk


class AggregatorFrame(ttk.Frame):
    """This class extends ttk.Frame to create a widget that can add and remove other frames in a list-type fashion"""
    #TODO: may eventually need this to be built onto a ScrollingFrame, do user testing to determine
    def __init__(self, parent, title):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.frame_list = []
        self.entry_state = BooleanVar()

        self.outer = ttk.Frame(self)
        self.outer.grid()
        self.outer.grid_columnconfigure(0, weight=1)

        section_name_label = ttk.Label(self.outer, text=title, width=28)
        section_name_label.grid(row=0, column=0, sticky="ew", padx=(2, 0))

        cb = ttk.Checkbutton(self.outer, onvalue=1, offvalue=0, variable=self.entry_state)
        cb.configure(command=partial(self.cb_value_changed, self.entry_state, self))
        cb.grid(row=0, column=1, sticky="e", padx=(20, 0))

        self.inner = ttk.Frame(self.outer)
        self.inner.grid(row=1, column=0, columnspan=2, sticky="nsew")

        add_button = ttk.Button(self.outer, text="Add %s" % title, command=self.add_frame)
        add_button.grid(row=2, column=0, columnspan=2, sticky="ew")
    #end init


    def add_frame(self):
        """ Provided method declaration for the subclass to implement """
        pass
    #end add_frame


    def delete_frame(self, frame):
        self.frame_list.remove(frame)
        frame.frame.pack_forget()
        frame.frame.destroy()
    #end delete_frame


    def configure_frame(self):
        """ Provided method declaration for the subclass to implement """
        pass
    #end configure_frame


    @staticmethod
    def cb_value_changed(entry_state, modified_widget):
        """
        Log the change of the entry_state of a given widget

        :param entry_state: The boolean value of the entry
        :param modified_widget: The widget modified
        """
        logging.debug("The value of %s is: %s" % (modified_widget, entry_state.get()))
    # end cb_value_changed
#end AggregatorFrame


def main():
    root = Tk()
    frame = AggregatorFrame(root, "Testing")
    frame.pack()
    root.mainloop()
#end main


if __name__ == "__main__":
    main()
