from .Spatial import Spatial
from .IsoSprite import IsoSprite

class SpriteGroup(Spatial):
    def __init__(self):
        Spatial.__init__(self)
        self.sprites = set()

    def getSprites(self):
        return self.sprites

    def addSprite(self, sprite):
        self.sprites.add(sprite)
        if self.scene != None:
            self.scene.addSprite(sprite)
        sprite.setParent(self)

    def removeSprite(self, sprite):
        self.sprites.remove(sprite)
        if self.scene != None:
            self.scene.removeSprite(sprite)
        sprite.setParent(None)


    def setLocation(self, new_loc):
        old_loc = self.getLocation()
        delta_loc = new_loc - old_loc
        Spatial.setLocation(self, new_loc)
        for sprite in self.sprites:
            sprite_loc = sprite.getLocation()
            new_sprite_loc = sprite_loc + delta_loc
            sprite.setLocation(new_sprite_loc)