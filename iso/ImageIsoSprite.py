from tkinter import *
from .Vector3D import *
from .Vector2D import *
from .IsoSprite import IsoSprite
from .BoundsDrawer import BoundsDrawer


class ImageIsoSprite(IsoSprite):
    def __init__(self, image=None):
        IsoSprite.__init__(self)
        self.image = image  # The image to render this sprite


    def setImage(self, image):
        self.image = image


    def getImage(self):
        return self.image


    def draw(self, viewport, canvas):
        if viewport.draw_bounds:
            BoundsDrawer.drawBoundsBackground(viewport, canvas)

        position = viewport.project(self.location)
        canvas.create_image((position.x - self.image.anchor.x, position.y - self.image.anchor.y),image=self.image.tk_image, anchor=NW)
        BoundsDrawer.drawImageBounds(viewport, canvas, self)

        self.drawImageBounds(viewport, canvas)

        if viewport.draw_bounds:
            BoundsDrawer.drawBoundsForeground(viewport, canvas)


    def handlePick(self, viewport, mouse_x, mouse_y):
        position = viewport.project(self.location)
        w = self.image.width()
        h = self.image.height()

        top_left = Vector2D(position.x - w / 2, position.y - h / 2)
        bottom_right = Vector2D(position.x + w / 2, position.y + h / 2)
        mouse = Vector2D(mouse_x, mouse_y)

        if mouse > top_left and mouse < bottom_right:
            mouse_relative = mouse - top_left
            color = self.image.pil_image.getpixel((int(mouse_relative.x), int(mouse_relative.y)))
            if color[0] == 0 and color[1] == 0 and color[2] == 0:
                return None
            else:
                return self
        else:
            return None