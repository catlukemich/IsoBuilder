import iso
from .SpriteBoundsHandles import *
from .SpriteLocationHandles import *

from .GridSprite import GridSprite
from .ProjectionPlane import ProjectionPlane
from .CenterDrawer import CenterDrawer

class SpriteAligner(iso.MouseListener, iso.KeyboardListener):

    def __init__(self, main):
        self.main = main
        self.main.scene.addLayer("GRIDS", 0)
        self.main.scene.addLayer("SPRITES", 1)
        self.main.scene.addLayer("INTERFACE", 2)
        self.sprite = None
        self.sprite_handles = SpriteLocationHandles(None)
        self.bounds_handles = SpriteBoundsHandles(None)
        self.current_sprite_handle = None
        self.current_bounds_handle = None
        self.grid = None
        self.projection_plane_xz = None
        self.projection_plane_yz = None
        self.settings = self.main.settings
        self.settings.addSettingsListener(self)

    def enable(self):
        self.main.input.addMouseListener(self)
        self.main.input.addKeyboardListener(self)
        self.grid = GridSprite(10, 10)
        self.main.scene.addSprite("GRIDS", self.grid)

        self.projection_plane_xz = ProjectionPlane(ProjectionPlane.PLANE_XZ, 10, self.settings)
        self.main.scene.addSprite("GRIDS", self.projection_plane_xz)
        self.projection_plane_xz.setLocationXYZ(0, -5, 0)

        self.projection_plane_yz = ProjectionPlane(ProjectionPlane.PLANE_YZ, 10, self.settings)
        self.main.scene.addSprite("GRIDS", self.projection_plane_yz)
        self.projection_plane_yz.setLocationXYZ(-5, 0, 0)

        self.center_drawer = CenterDrawer()
        self.main.scene.addSprite("INTERFACE", self.center_drawer)



    def disable(self):
        self.main.input.removeMouseListener(self)
        self.main.input.removKeyboardListener(self)


    def setGridSize(self, grid_size):
        self.main.scene.removeSprite("GRIDS", self.grid)
        self.grid = GridSprite(grid_size, grid_size)
        self.main.scene.addSprite("GRIDS", self.grid)

    def setSprite(self, sprite):
        if sprite is not None:
            layer_name = sprite.scene_layer.name
            self.sprite_handles.setSprite(sprite)
            self.main.scene.addSprite("INTERFACE", self.sprite_handles)
            self.bounds_handles.setSprite(sprite)
            if self.settings.use_bounds:
                self.main.scene.addSprite("INTERFACE", self.bounds_handles)
            self.projection_plane_yz.setSprite(sprite)
            self.projection_plane_xz.setSprite(sprite)
            self.sprite = sprite
        else:
            self.main.scene.removeSprite("INTERFACE", self.sprite_handles)
            self.main.scene.removeSprite("INTERFACE", self.bounds_handles)
            self.projection_plane_xz.setSprite(sprite)
            self.projection_plane_yz.setSprite(sprite)
            self.sprite = None

    def mouseButtonDown(self, event):
        if event.num == 1:
            results = self.main.viewport.pickSprites(event.x, event.y)
            sprite_handle = results.getObjectOfClass(LocationHandle)
            self.current_sprite_handle = sprite_handle
            bounds_handle = results.getObjectOfClass(BoundsHandle)
            self.current_bounds_handle = bounds_handle

            # If none of the handles were pressed, then check if sprite was clicked and set it as an active sprite:
            if sprite_handle is None and bounds_handle is None:
                sprite = results.getObjectOfClass(iso.ImageIsoSprite)
                if sprite != None:
                    self.setSprite(sprite)
                    self.main.controls.setSprite(sprite)


    def mouseMotion(self, event, delta_x, delta_y):
        if self.current_sprite_handle != None or self.current_bounds_handle != None:
            dx = delta_x
            dy = delta_y

            if self.sprite != None:
                loc = self.sprite.getLocation()
                if self.current_sprite_handle != None:
                    if self.current_sprite_handle.direction == Direction.X_PLUS:
                        loc.x += float(dx) / iso.TILE_WIDTH
                        loc.x += float(dy) / iso.TILE_HEIGHT

                    elif self.current_sprite_handle.direction == Direction.Y_PLUS:
                        loc.y -= float(dx) / iso.TILE_WIDTH
                        loc.y += float(dy) / iso.TILE_HEIGHT

                    elif self.current_sprite_handle.direction == Direction.Z_PLUS:
                        loc.z -= float(dy) / iso.TILE_HEIGHT

                    self.sprite_handles.setLocation(Vector3D(loc))
                    self.bounds_handles.setLocation(Vector3D(loc))

                if self.current_bounds_handle != None:
                    bounds = self.sprite.getBounds()
                    if self.current_bounds_handle.direction == Direction.X_PLUS or self.current_bounds_handle.direction == Direction.X_MINUS:
                        delta_loc_x = (float(dx) / iso.TILE_WIDTH) + (float(dy) / iso.TILE_HEIGHT)
                    if self.current_bounds_handle.direction == Direction.Y_PLUS or self.current_bounds_handle.direction == Direction.Y_MINUS:
                        delta_loc_y = -(float(dx) / iso.TILE_WIDTH) + (float(dy) / iso.TILE_HEIGHT)
                    if self.current_bounds_handle.direction == Direction.Z_PLUS or self.current_bounds_handle.direction == Direction.Z_MINUS:
                        delta_loc_z = -(float(dy) / iso.TILE_HEIGHT)

                    if self.current_bounds_handle.direction == Direction.X_PLUS:
                        bounds.max_x += delta_loc_x
                    if self.current_bounds_handle.direction == Direction.X_MINUS:
                        bounds.min_x += delta_loc_x
                    if self.current_bounds_handle.direction == Direction.Y_PLUS:
                        bounds.max_y += delta_loc_y
                    if self.current_bounds_handle.direction == Direction.Y_MINUS:
                        bounds.min_y += delta_loc_y
                    if self.current_bounds_handle.direction == Direction.Z_PLUS:
                        bounds.max_z += delta_loc_z
                    if self.current_bounds_handle.direction == Direction.Z_MINUS:
                        bounds.min_z += delta_loc_z

            self.main.controls.updateControls()

    def mouseButtonUp(self, event):
        self.current_sprite_handle = None
        self.current_bounds_handle = None

    def keyDown(self, event):
        if event.keycode == 46:
            if self.sprite != None:
                self.main.sprites.remove(self.sprite)
                self.main.scene.removeSprite("SPRITES", self.sprite)
                self.setSprite(None)

    def settingsChanged(self, settings):
        if settings.use_bounds == False and self.sprite is not None:
            self.main.scene.removeSprite("INTERFACE", self.bounds_handles)
        elif settings.use_bounds == True and self.sprite is not None:
            self.main.scene.addSprite("INTERFACE", self.bounds_handles)
