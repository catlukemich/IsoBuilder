from iso import Vector3D
from iso.IsoSprite import *

# Projection plane is a plane that is designed
# to display projected bounds of a Sprite to
# plane in the isometric 3D world.
class ProjectionPlane(IsoSprite):
    PLANE_XZ = 1
    PLANE_YZ = 2

    def __init__(self, plane, size, settings):
        IsoSprite.__init__(self)
        self.plane = plane
        self.size = size
        self.settings = settings
        self.sprite = None

    def setSprite(self, sprite):
        self.sprite = sprite

    # Depending on what plane the projection
    # plane is about to be situated draw the plane itself,
    # the projected bounds of an object and a center of an object.
    def draw(self, viewport, canvas):
        location = self.getLocation()
        half_size = int(self.size / 2)

        if self.plane == ProjectionPlane.PLANE_XZ:
            y_loc = location.y
            v_tl = Vector3D(-half_size, y_loc, half_size)
            v_tr = Vector3D(half_size , y_loc, half_size)
            v_bl = Vector3D(-half_size, y_loc, -half_size)
            v_br = Vector3D(half_size , y_loc, -half_size)

            v_tl_pos = viewport.project(v_tl)
            v_tr_pos = viewport.project(v_tr)
            v_bl_pos = viewport.project(v_bl)
            v_br_pos = viewport.project(v_br)

            canvas.create_polygon(
                v_tl_pos.x, v_tl_pos.y,
                v_tr_pos.x, v_tr_pos.y,
                v_br_pos.x, v_br_pos.y,
                v_bl_pos.x, v_bl_pos.y,
                fill="#f5f0d5",
                outline="black"
            )

            if self.sprite != None:
                absolute_bounds = self.sprite.calcAbsoluteBounds()
                # Calculate the vertices of the bounds:
                bounds_v_tl = Vector3D(absolute_bounds.min_x, y_loc, absolute_bounds.max_z)
                bounds_v_tr = Vector3D(absolute_bounds.max_x, y_loc, absolute_bounds.max_z)
                bounds_v_bl = Vector3D(absolute_bounds.min_x, y_loc, absolute_bounds.min_z)
                bounds_v_br = Vector3D(absolute_bounds.max_x, y_loc, absolute_bounds.min_z)
                # Calculate positions of the vertices of the bounds:
                bounds_v_tl_pos = viewport.project(bounds_v_tl)
                bounds_v_tr_pos = viewport.project(bounds_v_tr)
                bounds_v_bl_pos = viewport.project(bounds_v_bl)
                bounds_v_br_pos = viewport.project(bounds_v_br)
                # Draw the polygon of the sprite bounds:
                if self.settings.use_bounds:
                    canvas.create_polygon(
                        bounds_v_tl_pos.x, bounds_v_tl_pos.y,
                        bounds_v_tr_pos.x, bounds_v_tr_pos.y,
                        bounds_v_br_pos.x, bounds_v_br_pos.y,
                        bounds_v_bl_pos.x, bounds_v_bl_pos.y,
                        fill="red",
                        outline="black"
                    )

                # Draw the sprite center:
                sprite_loc = Vector3D(self.sprite.getLocation())
                sprite_loc.y = y_loc
                sprite_pos = viewport.project(sprite_loc)
                canvas.create_oval(sprite_pos.x - 4, sprite_pos.y - 4,
                                   sprite_pos.x + 4, sprite_pos.y + 4,
                                   fill = "blue")

        elif self.plane == ProjectionPlane.PLANE_YZ:
            x_loc = location.x
            v_tl = Vector3D(x_loc,  half_size, half_size)
            v_tr = Vector3D(x_loc, -half_size, half_size)
            v_bl = Vector3D(x_loc, half_size, -half_size)
            v_br = Vector3D(x_loc, -half_size, -half_size)

            v_tl_pos = viewport.project(v_tl)
            v_tr_pos = viewport.project(v_tr)
            v_bl_pos = viewport.project(v_bl)
            v_br_pos = viewport.project(v_br)

            canvas.create_polygon(
                v_tl_pos.x, v_tl_pos.y,
                v_tr_pos.x, v_tr_pos.y,
                v_br_pos.x, v_br_pos.y,
                v_bl_pos.x, v_bl_pos.y,
                fill="#f5e7d5",
                outline="black"
            )


            # Draw the projected bounds outline:
            if self.sprite != None:
                sprite_loc = self.sprite.getLocation()
                absolute_bounds = self.sprite.calcAbsoluteBounds()
                # Calculate the vertices of the bounds:
                bounds_v_tl = Vector3D(x_loc, absolute_bounds.max_y, absolute_bounds.max_z)
                bounds_v_tr = Vector3D(x_loc, absolute_bounds.min_y, absolute_bounds.max_z)
                bounds_v_bl = Vector3D(x_loc, absolute_bounds.max_y, absolute_bounds.min_z)
                bounds_v_br = Vector3D(x_loc, absolute_bounds.min_y, absolute_bounds.min_z)
                # Calculate positions of the vertices of the bounds:
                bounds_v_tl_pos = viewport.project(bounds_v_tl)
                bounds_v_tr_pos = viewport.project(bounds_v_tr)
                bounds_v_bl_pos = viewport.project(bounds_v_bl)
                bounds_v_br_pos = viewport.project(bounds_v_br)
                # Draw the polygon of the sprite bounds:
                if self.settings.use_bounds:
                    canvas.create_polygon(
                        bounds_v_tl_pos.x, bounds_v_tl_pos.y,
                        bounds_v_tr_pos.x, bounds_v_tr_pos.y,
                        bounds_v_br_pos.x, bounds_v_br_pos.y,
                        bounds_v_bl_pos.x, bounds_v_bl_pos.y,
                        fill="red",
                        outline="black"
                    )
                # Draw the sprite center:
                sprite_loc = Vector3D(self.sprite.getLocation())
                sprite_loc.x = x_loc
                sprite_pos = viewport.project(sprite_loc)
                canvas.create_oval(sprite_pos.x - 4, sprite_pos.y - 4,
                                   sprite_pos.x + 4, sprite_pos.y + 4,
                                   fill="blue")



