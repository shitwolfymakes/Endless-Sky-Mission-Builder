''' ScrollingCenterFrame.py
Most of the code for this is from: https://gist.github.com/novel-yet-trivial/3eddfce704db3082e38c84664fc1fdf8

Link to their github: https://github.com/novel-yet-trivial

Thanks m8!
'''

from tkinter import *
from tkinter import ttk

class ScrollingCenterFrame:
    """
    A vertically scrolled Frame that can be treated like any other Frame
    ie it needs a master and layout and it can be a master.
    keyword arguments are passed to the underlying Frame
    except the keyword arguments 'width' and 'height', which
    are passed to the underlying Canvas
    note that a widget layed out in this frame will have Canvas as self.master,
    if you subclass this there is no built in way for the children to access it.
    You need to provide the controller separately.
    """

    def __init__(self, master, **kwargs):
        width = kwargs.pop('width', 450)     #default width = None
        height = kwargs.pop('height', None)
        self.outer = ttk.Frame(master, **kwargs)

        cfTitle = ttk.Label(self.outer, text="Mission Options")
        cfTitle.pack()

        self.vsb = tk.Scrollbar(self.outer, orient=tk.VERTICAL)
        self.vsb.pack(fill=tk.Y, side=tk.RIGHT, pady=(2,2))
        self.canvas = tk.Canvas(self.outer, highlightthickness=0, width=width, height=height, bg="#ededed")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=(0, 10))
        self.canvas['yscrollcommand'] = self.vsb.set
        # mouse scroll does not seem to work with just "bind"; You have
        # to use "bind_all". Therefore to use multiple windows you have
        # to bind_all in the current widget
        self.canvas.bind("<Enter>", self._bind_mouse)
        self.canvas.bind("<Leave>", self._unbind_mouse)
        self.vsb['command'] = self.canvas.yview

        self.inner = tk.Frame(self.canvas, bg="#ededed")
        #self.inner.configure(bg="orange")
        # pack the inner Frame into the Canvas with the top-left corner 4 pixels offset, set the Frame width
        self.canvas.create_window(4, 4, window=self.inner, anchor='nw')
        self.inner.bind("<Configure>", self._on_frame_configure)

        self.outer_attr = set(dir(tk.Widget))

    def __getattr__(self, item):
        if item in self.outer_attr:
            # geometry attributes etc (eg pack, destroy, tkraise) are passed on to self.outer
            return getattr(self.outer, item)
        else:
            # all other attributes (_w, children, etc) are passed to self.inner
            return getattr(self.inner, item)

    def _on_frame_configure(self, event=None):
        x1, y1, x2, y2 = self.canvas.bbox("all")
        width = self.inner.winfo_reqwidth()
        height = self.canvas.winfo_height()
        self.canvas.config(scrollregion=(0, 0, width, max(y2, height)))

    def _bind_mouse(self, event=None):
        self.canvas.bind_all("<4>", self._on_mousewheel)
        self.canvas.bind_all("<5>", self._on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mouse(self, event=None):
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        """Linux uses event.num; Windows / Mac uses event.delta"""
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")
#end class ScrollingCenterFrame


class ScrollingCenterFrame2(ttk.Frame):
    #TODO: Implement this to replace the current SCF
    def __init__(self, app, parent):
        ttk.Frame.__init__(self, parent)

        cfTitle = ttk.Label(self, text="Mission Options")
        cfTitle.pack()

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
        self.inner_id = self.canvas.create_window((4,4), window=self.inner, anchor=NW)

        self.inner.bind("<Configure>", self._configureInner)
        self.canvas.bind("<Configure>", self._configureCanvas)

    #end init


    def _bind_mouse(self, event=None):
        self.canvas.bind_all("<4>", self._on_mousewheel)
        self.canvas.bind_all("<5>", self._on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)


    def _unbind_mouse(self, event=None):
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")


    def _on_mousewheel(self, event):
        """Linux uses event.num; Windows / Mac uses event.delta"""
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")


    def _configureInner(self, event=None):
        # update the scrollbars to match the size of the inner frame
        size = (self.inner.winfo_width(), self.inner.winfo_height())
        self.canvas.config(scrollregion="0 0 %s %s" % size)
        if self.inner.winfo_reqwidth() >= self.canvas.winfo_width():
            # update the canvas's width to fit the inner frame
            # only works before mainloop
            self.canvas.config(width=self.inner.winfo_reqwidth())
        screen_h = self.winfo_screenheight()
        height   = self.parent.winfo_rooty() + self.parent.winfo_height() - self.canvas.winfo_height() + self.inner.winfo_reqheight()
        if height < screen_h:
            self.canvas.configure(height=self.inner.winfo_reqheight())
    #end _configureInner


    def _configureCanvas(self, event=None):
        if self.inner.winfo_reqwidth() < self.canvas.winfo_width():
            self.canvas.itemconfigure(self.inner_id, width=self.canvas.winfo_width())
        elif self.inner.winfo_reqwidth() > self.canvas.winfo_width():
            self.canvas.config(width=self.inner.winfo_reqwidth())

        if (self.inner.winfo_reqheight() < self.canvas.winfo_height()) or (self.inner.winfo_height() < self.canvas.winfo_height()):
            self.canvas.itemconfigure(self.inner_id, height=self.canvas.winfo_height())
    #end _configureCanvas

#end class ScrollingCenterFrame2