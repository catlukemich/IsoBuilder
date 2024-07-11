from tkinter import *
from iso.Direction import Direction
from iso.IsoSprite import IsoSprite
from iso.Vector2D import Vector2D
from iso.Vector3D import Vector3D


class SpriteLocationHandles(IsoSprite):
    def __init__(self, sprite):
        IsoSprite.__init__(self)
        self.sprite = sprite
        self.x_axis_handle = LocationHandle(self, Direction.X_PLUS, "red")
        self.y_axis_handle = LocationHandle(self, Direction.Y_PLUS, "green")
        self.z_axis_handle = LocationHandle(self, Direction.Z_PLUS, "blue")


    def setSprite(self, sprite):
        self.sprite = sprite
        sprite_loc = sprite.getLocation()
        self.setLocation(Vector3D(sprite_loc))

    def draw(self, viewport, canvas):
        location = self.getLocation()
        position = viewport.project(location)
        # Draw the sprite handles:
        self.x_axis_handle.draw(viewport, canvas)
        self.y_axis_handle.draw(viewport, canvas)
        self.z_axis_handle.draw(viewport ,canvas)
        # Draw the center widget:
        canvas.create_oval(position.x-4, position.y-4, position.x+4, position.y+4, fill="orange")

    def handlePick(self, viewport, mouse_x, mouse_y):
        mouse_pos = Vector2D(mouse_x, mouse_y)
        x_handle_pos = self.x_axis_handle.calcPickPosition(viewport)
        y_handle_pos = self.y_axis_handle.calcPickPosition(viewport)
        z_handle_pos = self.z_axis_handle.calcPickPosition(viewport)

        max_dist = 10

        if mouse_pos.distance(x_handle_pos) < max_dist:
            return self.x_axis_handle
        if mouse_pos.distance(y_handle_pos) < max_dist:
            return self.y_axis_handle
        if mouse_pos.distance(z_handle_pos) < max_dist:
            return self.z_axis_handle

        return None



class LocationHandle:
    def __init__(self, handles, direction, color):
        self.handles = handles
        self.direction = direction
        self.color = color

    def draw(self, viewport, canvas):
        sprite_loc = self.handles.getLocation()
        sprite_pos = viewport.project(sprite_loc)
        handle_pos = self.calcPosition(viewport)
        canvas.create_line(sprite_pos.x, sprite_pos.y, handle_pos.x, handle_pos.y, fill=self.color, arrow = LAST)

    def calcPosition(self, viewport):
        handles_loc = self.handles.getLocation()
        position = viewport.project(handles_loc + self.direction)
        return position

    def calcPickPosition(self, viewport):
        handles_loc = self.handles.getLocation()
        position = viewport.project(handles_loc + (self.direction * 0.9))
        return position

