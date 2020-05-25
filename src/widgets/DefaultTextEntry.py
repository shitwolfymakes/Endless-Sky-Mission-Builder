import tkinter as tk
from tkinter import ttk


class DefaultTextEntry(ttk.Entry):
    """This widget extends ttk.Entry, displays greyed-out text whenever it doesn't have user input"""
    def __init__(self, parent, default_text, **kwargs):
        ttk.Entry.__init__(self, parent, **kwargs)

        self.default_text = default_text
        self.insert(0, default_text)

        self.bind('<FocusIn>', self._on_entry_click)
        self.bind('<FocusOut>', self._on_focus_out)
        self.config(foreground='#A9A9A9')
    # end init


    def _on_entry_click(self, event):
        """function that gets called whenever entry is clicked"""
        if self.get() == self.default_text:
            self.delete(0, "end")
            self.insert(0, '')
            self.config(foreground='black')
        #end if
    #end _on_entry_click


    def _on_focus_out(self, event):
        if self.get() == '':
            self.insert(0, self.default_text)
            self.config(foreground='#A9A9A9')
        #end if
    #end _on_focus_out

    def set(self, data):
        self.delete(0, "end")
        self.insert(0, data)
        self.config(foreground='black')
    #end set
# end class DefaultTextEntry


def main():
    root = tk.Tk()
    label = tk.Label(root, text="User: ")
    label.pack(side="left")

    entry = DefaultTextEntry(root, 'Enter your user name...')
    entry.pack(side="right")
    root.mainloop()


if __name__ == '__main__':
    main()
