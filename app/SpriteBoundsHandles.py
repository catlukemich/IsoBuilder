from iso.Direction import Direction
from iso.IsoSprite import IsoSprite
from iso.Vector2D import Vector2D
from iso.Vector3D import Vector3D


class SpriteBoundsHandles(IsoSprite):
    def __init__(self, sprite):
        IsoSprite.__init__(self)
        self.sprite = sprite
        bounds_handle_color = "violet"
        self.x_plus_bounds_handle = BoundsHandle(self, Direction.X_PLUS, bounds_handle_color)
        self.x_minus_bounds_handle = BoundsHandle(self, Direction.X_MINUS, bounds_handle_color)
        self.y_plus_bounds_handle = BoundsHandle(self, Direction.Y_PLUS, bounds_handle_color)
        self.y_minus_bounds_handle = BoundsHandle(self, Direction.Y_MINUS, bounds_handle_color)
        self.z_plus_bounds_handle = BoundsHandle(self, Direction.Z_PLUS, bounds_handle_color)
        self.z_minus_bounds_handle = BoundsHandle(self, Direction.Z_MINUS, bounds_handle_color)


    def setSprite(self, sprite):
        self.sprite = sprite
        sprite_loc = sprite.getLocation()
        self.setLocation(Vector3D(sprite_loc))

    def draw(self, viewport, canvas):
        location = self.getLocation()
        position = viewport.project(location)
        # Draw the bounds handles:
        self.x_plus_bounds_handle.draw(viewport, canvas)
        self.x_minus_bounds_handle.draw(viewport, canvas)
        self.y_plus_bounds_handle.draw(viewport, canvas)
        self.y_minus_bounds_handle.draw(viewport, canvas)
        self.z_plus_bounds_handle.draw(viewport, canvas)
        self.z_minus_bounds_handle.draw(viewport, canvas)

        # Draw the center widget:
        canvas.create_oval(position.x-4, position.y-4, position.x+4, position.y+4, fill="orange")

    def handlePick(self, viewport, mouse_x, mouse_y):
        mouse_pos = Vector2D(mouse_x, mouse_y)
        x_plus_handle_pos   = self.x_plus_bounds_handle.calcPickPosition(viewport)
        x_minus_hanlde_pos  = self.x_minus_bounds_handle.calcPickPosition(viewport)
        y_plus_handle_pos   = self.y_plus_bounds_handle.calcPickPosition(viewport)
        y_minus_handle_pos  = self.y_minus_bounds_handle.calcPickPosition(viewport)
        z_plus_handle_pos   = self.z_plus_bounds_handle.calcPickPosition(viewport)
        z_minus_handle_pos  = self.z_minus_bounds_handle.calcPickPosition(viewport)

        max_dist = 10

        if mouse_pos.distance(x_plus_handle_pos) < max_dist:
            return self.x_plus_bounds_handle
        if mouse_pos.distance(x_minus_hanlde_pos) < max_dist:
            return self.x_minus_bounds_handle
        if mouse_pos.distance(y_plus_handle_pos) < max_dist:
            return self.y_plus_bounds_handle
        if mouse_pos.distance(y_minus_handle_pos) < max_dist:
            return self.y_minus_bounds_handle
        if mouse_pos.distance(z_plus_handle_pos) < max_dist:
            return self.z_plus_bounds_handle
        if mouse_pos.distance(z_minus_handle_pos) < max_dist:
            return self.z_minus_bounds_handle

        return None


class BoundsHandle:
    def __init__(self, handles, direction, color):
        self.handles = handles
        self.direction = direction
        self.color = color

    def draw(self, viewport, canvas):
        handles_loc = self.handles.getLocation()
        bounds = self.handles.sprite.getBounds()
        if self.direction == Direction.X_PLUS:
            start_location = handles_loc + Vector3D(bounds.max_x, 0, 0)
        if self.direction == Direction.X_MINUS:
            start_location = handles_loc + Vector3D(bounds.min_x, 0, 0)
        if self.direction == Direction.Y_PLUS:
            start_location = handles_loc + Vector3D(0, bounds.max_y, 0)
        if self.direction == Direction.Y_MINUS:
            start_location = handles_loc + Vector3D(0, bounds.min_y, 0)
        if self.direction == Direction.Z_PLUS:
            start_location = handles_loc + Vector3D(0, 0, bounds.max_z)
        if self.direction == Direction.Z_MINUS:
            start_location = handles_loc + Vector3D(0, 0, bounds.min_z)
        end_location = start_location + self.direction
        # Calculate the start and end position of handle:
        start_pos = viewport.project(start_location)
        end_pos = viewport.project(end_location)
        # Draw the line from the bounding box face to outside:
        canvas.create_line(start_pos.x, start_pos.y, end_pos.x, end_pos.y, fill=self.color)
        # Draw the handle widget:
        canvas.create_oval(end_pos.x - 4, end_pos.y - 4, end_pos.x + 4, end_pos.y + 4, fill=self.color)


    def calcPickPosition(self, viewport):
        handles_loc = self.handles.getLocation()
        bounds = self.handles.sprite.getBounds()
        if self.direction == Direction.X_PLUS:
            start_location = handles_loc + Vector3D(bounds.max_x, 0, 0)
        if self.direction == Direction.X_MINUS:
            start_location = handles_loc + Vector3D(bounds.min_x, 0, 0)
        if self.direction == Direction.Y_PLUS:
            start_location = handles_loc + Vector3D(0, bounds.max_y, 0)
        if self.direction == Direction.Y_MINUS:
            start_location = handles_loc + Vector3D(0, bounds.min_y, 0)
        if self.direction == Direction.Z_PLUS:
            start_location = handles_loc + Vector3D(0, 0, bounds.max_z)
        if self.direction == Direction.Z_MINUS:
            start_location = handles_loc + Vector3D(0, 0, bounds.min_z)
        end_location = start_location + (self.direction * 0.9)
        position = viewport.project(end_location)
        return position

