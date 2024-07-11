import iso

class CenterDrawer(iso.IsoSprite):

    def draw(self, viewport, canvas):
        location = iso.Vector3D(0,0,0)
        center_pos = viewport.project(location)
        canvas.create_oval(center_pos.x - 4, center_pos.y - 4, center_pos.x + 4, center_pos.y + 4,
                           fill="white", outline="black")