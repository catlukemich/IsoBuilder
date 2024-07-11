from .Vector3D import *


class Spatial:
    def __init__(self):
        self.location = Vector3D()  # Location of the spatial in isometric 3d world coordinates
        self.scene = None
        self.scene_layer = None
        self.parent  = None

    def setScene(self, scene, layer):
        self.scene = scene
        self.scene_layer = layer

    def getScene(self):
        return self.scene

    def setParent(self, parent):
        self.parent = parent

    def setLocationXYZ(self, x, y, z):
        loc = Vector3D(x, y, z)
        self.setLocation(loc)



    def setLocation(self, new_loc):
        if self.scene == None:
            self.location = new_loc
        old_loc = self.getLocation()
        if old_loc != new_loc and self.scene != None:
            should_move = self.scene_layer.grid.shouldMoveSprite(old_loc, new_loc)
            if should_move:
                self.scene_layer.grid.removeSprite(self)
                self.location = new_loc
                self.scene_layer.grid.addSprite(self)
            else:
                self.location = new_loc

    def getLocation(self):
        return self.location
