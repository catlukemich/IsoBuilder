import iso
from tkinter.ttk import *
from tkinter import Listbox, END

class ControlsFrame(LabelFrame):
    def __init__(self, main):
        LabelFrame.__init__(self, main.root, text="Controls")
        self.main = main
        self.sprite = None
        self.frame  = None
        self.createGridControls()
        self.createSpriteList()
        self.createSpriteControls()
        self.bindEvents()
        self.main.settings.addSettingsListener(self)

    def createGridControls(self):
        grid_frame = LabelFrame(self, text="Grid:")
        grid_frame.pack()
        size_label = Label(grid_frame, text="Size:")
        size_label.grid(column=0, row=0)
        self.grid_size_text = Entry(grid_frame)
        self.grid_size_text.grid(column=1, row=0)
        self.grid_size_text.bind("<Return>", self.applyGrid)
        self.apply_grid_button = Button(grid_frame, text="Apply")
        self.apply_grid_button.grid(column=0, row=1, columnspan=2)
        self.apply_grid_button["command"] = self.applyGrid

    def applyGrid(self, event=None):
        gird_size = int(self.grid_size_text.get())
        self.main.aligner.setGridSize(gird_size)



    # Create the sprite list with list of all the imported image sprites:
    def createSpriteList(self):
        sprite_list_frame = LabelFrame(self, text="Sprites:")
        sprite_list_frame.pack()

        self.sprite_list = Listbox(sprite_list_frame)
        self.sprite_list.pack()



    # Create the sprite controls for manual positioning and changing the bounding box of selected sprite:
    def createSpriteControls(self):
        self.frame = LabelFrame(self, text="Sprite:")
        self.frame.pack()

        self.createLocationControls()
        self.createBoundsControls()

    def createLocationControls(self):
        # Create the location frame and it's contents:
        self.location_frame = LabelFrame(self.frame, text="Location:")
        self.location_frame.pack()

        location_x_label = Label(self.location_frame, text="Location x:")
        location_x_label.grid(column=0, row=0)
        self.location_x_text = Entry(self.location_frame)
        self.location_x_text.grid(column=1, row=0)

        location_y_label = Label(self.location_frame, text="Location y:")
        location_y_label.grid(column=0, row=1)
        self.location_y_text = Entry(self.location_frame)
        self.location_y_text.grid(column=1, row=1)

        location_z_label = Label(self.location_frame, text="Location z:")
        location_z_label.grid(column=0, row=2)
        self.location_z_text = Entry(self.location_frame)
        self.location_z_text.grid(column=1, row=2)

    def createBoundsControls(self):
        # Create the bounds frame and it's contents:
        self.bounds_frame = LabelFrame(self.frame, text="Bounds:")
        self.bounds_frame.pack()

        bound_min_x_label = Label(self.bounds_frame, text="Min x:")
        bound_min_x_label.grid(column=0, row=0)
        self.bound_min_x_text = Entry(self.bounds_frame)
        self.bound_min_x_text.grid(column=1, row=0)

        bound_max_x_label = Label(self.bounds_frame, text="Max x:")
        bound_max_x_label.grid(column=0, row=1)
        self.bound_max_x_text = Entry(self.bounds_frame)
        self.bound_max_x_text.grid(column=1, row=1)

        bound_min_y_label = Label(self.bounds_frame, text="Min y:")
        bound_min_y_label.grid(column=0, row=2)
        self.bound_min_y_text = Entry(self.bounds_frame)
        self.bound_min_y_text.grid(column=1, row=2)

        bound_max_y_label = Label(self.bounds_frame, text="Max y:")
        bound_max_y_label.grid(column=0, row=3)
        self.bound_max_y_text = Entry(self.bounds_frame)
        self.bound_max_y_text.grid(column=1, row=3)

        bound_min_z_label = Label(self.bounds_frame, text="Min z:")
        bound_min_z_label.grid(column=0, row=4)
        self.bound_min_z_text = Entry(self.bounds_frame)
        self.bound_min_z_text.grid(column=1, row=4)

        bound_max_z_label = Label(self.bounds_frame, text="Max z:")
        bound_max_z_label.grid(column=0, row=5)
        self.bound_max_z_text = Entry(self.bounds_frame)
        self.bound_max_z_text.grid(column=1, row=5)

    def bindEvents(self):
        self.location_x_text.bind("<Return>", self.updateSprite)
        self.location_y_text.bind("<Return>", self.updateSprite)
        self.location_z_text.bind("<Return>", self.updateSprite)

        self.bound_min_x_text.bind("<Return>", self.updateSprite)
        self.bound_max_x_text.bind("<Return>", self.updateSprite)

        self.bound_min_y_text.bind("<Return>", self.updateSprite)
        self.bound_max_y_text.bind("<Return>", self.updateSprite)

        self.bound_min_z_text.bind("<Return>", self.updateSprite)
        self.bound_max_z_text.bind("<Return>", self.updateSprite)


    # Update sprite bounds and location, when the ui is changed:
    def updateSprite(self, event):
        self.updateSpriteLocation(event)
        self.updateSpriteBounds(event)

    # Update sprite location after changing it's location values:
    def updateSpriteLocation(self, event):
        try:
            x_loc_value = self.location_x_text.get()
            x_loc_value = float(x_loc_value)
            y_loc_value = self.location_y_text.get()
            y_loc_value = float(y_loc_value)
            z_loc_value = self.location_z_text.get()
            z_loc_value = float(z_loc_value)



            if self.sprite != None:
                location = iso.Vector3D(x_loc_value,y_loc_value,z_loc_value)
                self.sprite.setLocation(location)

        except ValueError as exception:
            print(exception)


    # Update sprite bounds after changing it's bounds values
    def updateSpriteBounds(self, event):
        try:
            bounds_x_min_value = self.bound_min_x_text.get()
            bounds_x_min_value = float(bounds_x_min_value)
            bounds_x_max_value = self.bound_max_x_text.get()
            bounds_x_max_value = float(bounds_x_max_value)

            bounds_y_min_value = self.bound_min_y_text.get()
            bounds_y_min_value = float(bounds_y_min_value)
            bounds_y_max_value = self.bound_max_y_text.get()
            bounds_y_max_value = float(bounds_y_max_value)

            bounds_z_min_value = self.bound_min_z_text.get()
            bounds_z_min_value = float(bounds_z_min_value)
            bounds_z_max_value = self.bound_max_z_text.get()
            bounds_z_max_value = float(bounds_z_max_value)

            if self.sprite is not None:
                bounds = iso.Bounds3D()
                bounds.min_x = bounds_x_min_value
                bounds.max_x = bounds_x_max_value
                bounds.min_y = bounds_y_min_value
                bounds.max_y = bounds_y_max_value
                bounds.min_z = bounds_z_min_value
                bounds.max_z = bounds_z_max_value
                self.sprite.setBounds(bounds)

        except ValueError as exception:
            print(exception)


    def setSprite(self, sprite):
        self.sprite = sprite
        self.updateControls()


    # Update controls in response of moving the sprite handles.
    def updateControls(self):
        if not self.sprite: return
        location = self.sprite.getLocation()

        self.location_x_text.delete(0, END)
        self.location_x_text.insert(0, "%.4f" % location.x)

        self.location_y_text.delete(0, END)
        self.location_y_text.insert(0, "%.4f" % location.y)

        self.location_z_text.delete(0, END)
        self.location_z_text.insert(0, "%.4f" % location.z)

        bounds = self.sprite.getBounds()

        self.bound_min_x_text.delete(0, END)
        self.bound_min_x_text.insert(0, "%.4f" % bounds.min_x)

        self.bound_max_x_text.delete(0, END)
        self.bound_max_x_text.insert(0, "%.4f" % bounds.max_x)

        self.bound_min_y_text.delete(0, END)
        self.bound_min_y_text.insert(0, "%.4f" % bounds.min_y)

        self.bound_max_y_text.delete(0, END)
        self.bound_max_y_text.insert(0, "%.4f" % bounds.max_y)

        self.bound_min_z_text.delete(0, END)
        self.bound_min_z_text.insert(0, "%.4f" % bounds.min_z)

        self.bound_max_z_text.delete(0, END)
        self.bound_max_z_text.insert(0, "%.4f" % bounds.max_z)


    def settingsChanged(self, settings):
        if settings.use_bounds == False:
            self.bounds_frame.pack_forget()
        elif settings.use_bounds == True:
            self.bounds_frame.pack()