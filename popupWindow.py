from tkinter import *

class popupWindow(object):
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
        value = self.e.get()
        self.app.addMission(value)
        self.top.grab_release()         # HAVE TO RELEASE
        self.top.destroy()
    #end cleanup

#end class popupWindow