from .Spatial import Spatial
from .Bounds3D import *

class IsoSprite(Spatial):

    def __init__(self):
        Spatial.__init__(self)
        self.bounds = Bounds3D()

    def draw(self, viewport, canvas):
        pass

    def handlePick(self, viewport, mouse_x, mouse_y):
        pass

    def setBounds(self, bounds):
        self.bounds = bounds

    def getBounds(self):
        return self.bounds

    def calcAbsoluteBounds(self):
        bounds_absolute = Bounds3D()
        bounds_absolute.min_x = self.location.x + self.bounds.min_x
        bounds_absolute.max_x = self.location.x + self.bounds.max_x
        bounds_absolute.min_y = self.location.y + self.bounds.min_y
        bounds_absolute.max_y = self.location.y + self.bounds.max_y
        bounds_absolute.min_z = self.location.z + self.bounds.min_z
        bounds_absolute.max_z = self.location.z + self.bounds.max_z
        return bounds_absolute