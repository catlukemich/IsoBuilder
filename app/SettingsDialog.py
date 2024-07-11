from tkinter.simpledialog import Dialog
from tkinter.ttk import *
from tkinter import BooleanVar
from tkinter import IntVar
from tkinter import StringVar

class SettingsDialog(Dialog):

    def __init__(self, parent, settings):
        self.settings = settings
        self.use_bounds_var = BooleanVar(value=settings.use_bounds)
        self.tile_width_var  = IntVar(value=settings.tile_width)
        self.tile_height_var = IntVar(value=settings.tile_height)
        Dialog.__init__(self, parent, "Settings")

    def body(self, master):
        use_bounds_check = Checkbutton(master, text="Use bounds", command=self.settingsChanged,
                       variable=self.use_bounds_var, onvalue=True, offvalue=False)
        use_bounds_check.pack()

        tile_width_input = Entry(master, textvariable=self.tile_width_var)
        tile_width_input.pack()

        tile_height_input = Entry(master, textvariable=self.tile_height_var)
        tile_height_input.pack()

        return use_bounds_check

    def settingsChanged(self, event=None):
        self.settings.setUseBounds(self.use_bounds_var.get())