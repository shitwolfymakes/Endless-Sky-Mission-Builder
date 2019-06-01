''' PopupWindow.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

'''

from tkinter import *

from guiutils import addMission

class PopupWindow(object):

    def __init__(self, app, master, text):
        self.app = app
        self.top = Toplevel(master)
        self.top.title("New Mission")
        self.top.grab_set()             # freezes the app until the user enters or cancels

        # build the widgets
        self.l = Label(self.top, text=text, bg='white')
        self.l.pack()
        self.e = Entry(self.top)
        self.e.pack()
        self.b = Button(self.top, text='Ok', command=self.cleanup)
        self.b.pack()
    #end init


    def cleanup(self):
        name = self.e.get()
        addMission(self.app, name)
        self.top.grab_release()         # HAVE TO RELEASE
        self.top.destroy()
    #end cleanup

#end class popupWindow