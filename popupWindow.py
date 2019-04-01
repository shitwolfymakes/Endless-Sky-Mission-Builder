from tkinter import *

class popupWindow(object):
    def __init__(self, master, text):
        top = self.top = Toplevel(master)
        self.value = ""
        self.l = Label(top, text=text, bg='white')
        self.l.pack()
        self.e = Entry(top)
        self.e.pack()
        self.b = Button(top, text='Ok', command=self.cleanup)
        self.b.pack()
    #end init


    def cleanup(self):
        self.value = self.e.get()
        self.top.destroy()

    #end cleanup

#end class popupWindow()