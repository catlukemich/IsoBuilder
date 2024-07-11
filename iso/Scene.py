from functools import cmp_to_key
from .Vector3D import Vector3D
from .SpriteGroup import SpriteGroup
from .Updateables import *

class SceneLayer:
    def __init__(self, name, index, grid):
        self.grid = grid
        self.name = name
        self.index = index

    def addSprite(self, sprite):
        self.grid.addSprite(sprite)

    def removeSprite(self, sprite):
        self.grid.removeSprite(sprite)

class Scene(Updater):
    def __init__(self, grid):
        Updater.__init__(self)
        self.grid = grid
        self.layers = []


    def addLayer(self, layer_name, index):
        grid = self.grid.copy()
        new_layer = SceneLayer(layer_name, index, grid)
        self.layers.append(new_layer)
        self.layers.sort(key=cmp_to_key(self.sortLayers))

    def removeLayer(self, layer_name):
        for layer in self.layers:
            if layer.name == layer_name:
                self.layers.remove(layer)

    def sortLayers(self, layer1, layer2):
        return layer1.index - layer2.index

    def addSprite(self, layer_name, sprite):
        if isinstance(sprite, SpriteGroup):
            sprites = sprite.getSprites()
            for child_sprite in sprites:
                self.addSprite(layer_name, child_sprite)

        if isinstance(sprite, Updateable):
            self.addUpdateable(sprite)

        target_layer = None
        for layer in self.layers:
            if layer.name == layer_name:
                target_layer = layer
        target_layer.addSprite(sprite)
        sprite.setScene(self, target_layer)

    def removeSprite(self, layer_name, sprite):
        if isinstance(sprite, SpriteGroup):
            sprites = sprite.getSprites()
            for child_sprite in sprites:
                self.removeSprite(layer_name, child_sprite)

        target_layer = None
        for layer in self.layers:
            if layer.name == layer_name:
                target_layer = layer
        target_layer.removeSprite(sprite)
        sprite.setScene(None, None)

