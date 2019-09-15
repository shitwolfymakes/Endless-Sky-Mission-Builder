from tkinter import Toplevel, ttk, LEFT


class TypeSelectorWindow(Toplevel):
    """This class creates a custom pop-up window this allows the user to select a given data format"""

    def __init__(self, master, options, callback, **kwargs):
        self.callback = callback
        super().__init__(master, **kwargs)

        self.optionList = ttk.Combobox(self, values=options, state="readonly", width=25)
        self.optionList.current(0)
        self.optionList.pack()

        buttons = ttk.Frame(self)
        ok = ttk.Button(buttons, text="OK", command=self._cleanup)
        ok.pack(side=LEFT, fill="x")
        cxl = ttk.Button(buttons, text="Cancel", command=self._cancelled)
        cxl.pack(fill="x")
        buttons.pack()

        # these commands make the parent window inactive
        self.transient(master)
        self.grab_set()
        master.wait_window(self)
    #end init


    def _cleanup(self):
        """Clean up whatever popups we've created"""
        self.callback(self.optionList.get())
        self.destroy()
    #end _cleanup


    def _cancelled(self):
        """Close the window"""
        self.callback("cancelled")
        self.destroy()
    #end _cancelled
#end class TypeSelectorWindow
