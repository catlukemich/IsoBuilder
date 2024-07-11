import time
import threading
from functools import cmp_to_key
from .PickResults import PickResults
from .SpriteGroup import SpriteGroup
from .Vector2D import *
from .Vector3D import *
from .Range import *

# The tile width and height in pixels.
# Modify this values if you want tiles to be in different size.
TILE_WIDTH = 96
TILE_HEIGHT = 48

# Precalculated half tile dimensions, dont touch that
HALF_TILE_WIDTH = TILE_WIDTH / 2
HALF_TILE_HEIGHT = TILE_HEIGHT / 2

class ViewportUpdateable:
    def viewportUpdate(self, clock):
        pass


class ViewportLayer:
    def __init__(self, scene_layer):
        self.scene_layer = scene_layer
        self.sprites = []

    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        self.sprites.remove(sprite)

class Viewport:
    def __init__(self, canvas, scene):
        self.canvas = canvas
        self.scene = scene
        self.center = Vector3D(0, 0, 0)
        self.layers = []  # List of viewport layers
        # Cull the layers:
        for scene_layer in self.scene.layers:
            viewport_layer = ViewportLayer(scene_layer)
            self.layers.append(viewport_layer)

        self.culled_and_sorted = False
        self.dirty = True
        self.cull_iterations = 0
        self.draw_bounds = True


    def update(self, clock):
        for layer in self.layers:
            for sprite in layer.sprites:
                if isinstance(sprite, ViewportUpdateable):
                    sprite.viewportUpdate(clock)


    def draw(self):
        self.performCull()
        viewport_layers = self.layers
        for viewport_layer in viewport_layers:
            viewport_layer.sprites.sort(key = cmp_to_key(self.compareSprites))

        for layer in viewport_layers:
            for sprite in layer.sprites:
                sprite.draw(self, self.canvas)


    def performCull(self):
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        offset = -40  # The offset for culling sprites
        viewport_horizontal_range = Range(-offset, w + offset)
        viewport_vertical_range = Range(- offset, h + offset)
        viewport_layers = self.layers

        for viewport_layer in self.layers:
            for sprite in viewport_layer.sprites:
                sprite_scene = sprite.getScene()
                if sprite_scene == None:
                    viewport_layer.removeSprite(sprite)


        for viewport_layer in viewport_layers:
            for cell in viewport_layer.scene_layer.grid.cells:
                for sprite in cell.sprites:
                    contains_sprite = sprite in viewport_layer.sprites
                    if not contains_sprite and sprite.scene != None:
                        viewport_layer.sprites.append(sprite)

            # Do sorting:
            for i in range(0, len(viewport_layer.sprites)):
                for j in range(i + 5, i):
                    sprite1 = viewport_layer.sprites[i]
                    sprite2 = viewport_layer.sprites[j]
                    cmp = self.compareSprites(sprite1, sprite2)
                    if cmp == -1:
                        viewport_layer.sprites[i] = sprite2
                        viewport_layer.sprites[j] = sprite1


    # Sort the layers:
    def compareSprites(self, sprite1, sprite2):
        sprite1_bounds = sprite1.calcAbsoluteBounds()
        sprite2_bounds = sprite2.calcAbsoluteBounds()
        if sprite1_bounds.min_x >= sprite2_bounds.max_x: return 1;
        elif sprite2_bounds.min_x >= sprite1_bounds.max_x: return -1;

        if sprite1_bounds.min_y >= sprite2_bounds.max_y: return 1;
        elif sprite2_bounds.min_y >= sprite1_bounds.max_y: return -1;

        if sprite1_bounds.min_z >= sprite2_bounds.max_z: return -1;
        elif sprite2_bounds.min_z >= sprite1_bounds.max_z: return 1;

        sprite1_loc = sprite1.getLocation();
        sprite2_loc = sprite2.getLocation();
        sum1 = sprite1_loc.x + sprite1_loc.y + sprite1_loc.z;
        sum2 = sprite2_loc.x + sprite2_loc.y + sprite2_loc.z;

        if sum1 >= sum2:
            return 1;
        else:
            return -1;


    def getCenter(self):
        return Vector3D(self.center.x, self.center.y, 0)


    def setCenter(self, center):
        if center != self.center:
            self.center = center
            self.dirty = True


    def project(self, location):
        ''' Project from world location to world position '''
        x = (location.x - location.y) * HALF_TILE_WIDTH
        y = (location.x + location.y - location.z * 2) * HALF_TILE_HEIGHT
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        projected = Vector2D(x + w / 2, y + h / 2);
        center = self.projectCenter()
        return projected - center


    def projectCenter(self):
        x = (self.center.x - self.center.y) * HALF_TILE_WIDTH
        y = (self.center.x + self.center.y - self.center.z * 2) * HALF_TILE_HEIGHT
        return Vector2D(x, y)


    def pickSprites(self, mouse_x, mouse_y) -> PickResults:
        pick_results = PickResults()
        for layer in self.layers:
            for sprite in layer.sprites:
                result = sprite.handlePick(self, mouse_x, mouse_y)
                if result != None:
                    pick_results.addObject(result)
        pick_results.reverse()
        return pick_results


    def setDrawBounds(self, draw_bounds):
        self.draw_bounds = draw_bounds