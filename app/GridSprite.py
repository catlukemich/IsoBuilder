from iso.IsoSprite import *
from iso.Vector3D import *

class GridSprite(IsoSprite):

    def __init__(self, x_size, y_size):
        IsoSprite.__init__(self)
        self.x_size = x_size
        self.y_size = y_size

    def draw(self, viewport, canvas):
        location = self.getLocation()
        start_x = location.x - self.x_size / 2
        start_y = location.y - self.y_size / 2
        end_x = location.x + self.x_size / 2
        end_y = location.y + self.y_size / 2

        for j in range(0, self.y_size):
            for i in range(0, self.x_size):
                x = i - self.x_size / 2
                y = j - self.y_size / 2
                v_tl = Vector3D(x, y, 0)
                v_tr = Vector3D(x + 1, y, 0)
                v_bl = Vector3D(x, y + 1, 0)
                v_br = Vector3D(x + 1, y + 1, 0)

                v_tl_pos = viewport.project(v_tl)
                v_tr_pos = viewport.project(v_tr)
                v_bl_pos = viewport.project(v_bl)
                v_br_pos = viewport.project(v_br)

                canvas.create_line(v_tl_pos.x, v_tl_pos.y, v_tr_pos.x, v_tr_pos.y, fill="black")
                canvas.create_line(v_bl_pos.x, v_bl_pos.y, v_br_pos.x, v_br_pos.y, fill="black")
                canvas.create_line(v_tl_pos.x, v_tl_pos.y, v_bl_pos.x, v_bl_pos.y, fill="black")
                canvas.create_line(v_tr_pos.x, v_tr_pos.y, v_br_pos.x, v_br_pos.y, fill="black")

    def handlePick(self, viewport, mouse_x, mouse_y):
        return None