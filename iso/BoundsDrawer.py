from .Vector3D import Vector3D

# Bounds drawer is used to draw bounds around the image and the 3d bounds of an isometric sprite.
class BoundsDrawer:

    @staticmethod
    def drawImageBounds(viewport, canvas, sprite):
        position = viewport.project(self.location)
        start_x = position.x - sprite.image.anchor.x
        start_y = position.y - sprite.image.anchor.y
        end_x = start_x + sprite.image.tk_image.width()
        end_y = start_y + sprite.image.tk_image.height()
        canvas.create_line(start_x, start_y, end_x, start_y)
        canvas.create_line(start_x, end_y, end_x, end_y)
        canvas.create_line(start_x, start_y, start_x, end_y)
        canvas.create_line(end_x, start_y, end_x, end_y)

    @staticmethod
    def drawBoundsBackground(viewport, canvas, sprite):
        bounds = sprite.calcAbsoluteBounds()

        vertex_upper_bl = Vector3D(bounds.min_x, bounds.max_y, bounds.max_z)
        upper_bl_position = viewport.project(vertex_upper_bl)
        vertex_upper_tl = Vector3D(bounds.min_x, bounds.min_y, bounds.max_z)
        upper_tl_position = viewport.project(vertex_upper_tl)
        vertex_upper_tr = Vector3D(bounds.max_x, bounds.min_y, bounds.max_z)
        upper_tr_position = viewport.project(vertex_upper_tr)

        vertex_lower_bl = Vector3D(bounds.min_x, bounds.max_y, bounds.min_z)
        lower_bl_position = viewport.project(vertex_lower_bl)
        vertex_lower_tl = Vector3D(bounds.min_x, bounds.min_y, bounds.min_z)
        lower_tl_position = viewport.project(vertex_lower_tl)
        vertex_lower_tr = Vector3D(bounds.max_x, bounds.min_y, bounds.min_z)
        lower_tr_position = viewport.project(vertex_lower_tr)

        vertex_lower_br = Vector3D(bounds.max_x, bounds.max_y, bounds.min_z)
        lower_br_position = viewport.project(vertex_lower_br)

        BoundsDrawer.drawLine(canvas, upper_bl_position, upper_tl_position)
        BoundsDrawer.drawLine(canvas, upper_tl_position, upper_tr_position)
        BoundsDrawer.drawLine(canvas, upper_bl_position, lower_bl_position)
        BoundsDrawer.drawLine(canvas, upper_tl_position, lower_tl_position)
        BoundsDrawer.drawLine(canvas, upper_tr_position, lower_tr_position)
        BoundsDrawer.drawLine(canvas, lower_bl_position, lower_tl_position)
        BoundsDrawer.drawLine(canvas, lower_tl_position, lower_tr_position)
        BoundsDrawer.drawLine(canvas, lower_bl_position, lower_br_position)
        BoundsDrawer.drawLine(canvas, lower_br_position, lower_tr_position)


    def drawBoundsForeground(viewport, canvas, sprite):
        bounds = self.calcAbsoluteBounds()

        vertex_upper_br = Vector3D(bounds.max_x, bounds.max_y, bounds.max_z)
        upper_br_position = viewport.project(vertex_upper_br)
        vertex_upper_bl = Vector3D(bounds.min_x, bounds.max_y, bounds.max_z)
        upper_bl_position = viewport.project(vertex_upper_bl)
        vertex_upper_tr = Vector3D(bounds.max_x, bounds.min_y, bounds.max_z)
        upper_tr_position = viewport.project(vertex_upper_tr)

        vertex_lower_bl = Vector3D(bounds.min_x, bounds.max_y, bounds.min_z)
        lower_bl_position = viewport.project(vertex_lower_bl)
        vertex_lower_br = Vector3D(bounds.max_x, bounds.max_y, bounds.min_z)
        lower_br_position = viewport.project(vertex_lower_br)
        vertex_lower_tr = Vector3D(bounds.max_x, bounds.min_y, bounds.min_z)
        lower_tr_position = viewport.project(vertex_lower_tr)

        BoundsDrawer.drawLine(canvas, upper_bl_position, upper_br_position);
        BoundsDrawer.drawLine(canvas, upper_br_position, upper_tr_position);
        BoundsDrawer.drawLine(canvas, upper_br_position, lower_br_position);


    @staticmethod
    def drawLine(canvas, coord_1, coord_2):
        canvas.create_line(coord_1.x, coord_1.y, coord_2.x, coord_2.y, fill="red")