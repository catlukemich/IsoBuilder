import tempfile
import os
import iso
from tkinter import filedialog
from app.SettingsDialog import SettingsDialog

class MenuHandler:

    def __init__(self, main):
        self.main = main
        # The filepath set when the sprite was saved. Used when calls to "save" are made:
        self.saved_filepath = None

    def new(self):
        pass

    # Open .spr file (a zip archive)
    def open(self):
        path = filedialog.askopenfilename(title="Open sprite", filetypes=[("Sprite file", "*.spr")])
        if not path: return
        for sprite in vars.sprites:
            self.main.scene.removeSprite("SPRITES", sprite)
        self.main.sprites.clear()

        sprites = iso.loadSpriteSet(path)
        self.main.sprites.extend(sprites)
        for sprite in sprites:
            self.main.scene.addSprite("SPRITES", sprite)
        self.saved_filepath = path

    # Add image as a sprite to the canvas:
    def addImage(self):
        path = filedialog.askopenfilename(title="Open image", filetypes=[("Png file", "png")])
        if not path: return
        image = iso.loadImage(path)
        sprite = iso.ImageIsoSprite(image)
        self.main.scene.addSprite("SPRITES", sprite)
        self.main.sprites.append(sprite)
        self.main.aligner.setSprite(sprite)

    def addAnimation(self):
        paths = filedialog.askopenfilenames(title="Open animation", filetypes=[("Png files", "png")])
        if not paths: return
        animation = iso.loadAnimation(paths)
        sprite = iso.AnimatedSprite(animation)
        self.main.scene.addSprite("SPRITES", sprite)
        self.main.sprites.append(sprite)
        self.main.aligner.setSprite(sprite)


    def save(self, event = None):
        if not self.saved_filepath:
            self.saveAs()
        else:
            self.saveSpr(self.saved_filepath)

    def saveAs(self):
        filepath = filedialog.asksaveasfilename(title="Save sprite as", filetypes=[("Sprite", "*.spr")])
        if not filepath: return
        if os.path.exists(filepath):
            os.remove(filepath)
        self.saveSpr(filepath)
        self.saved_filepath = filepath


    def saveSpr(self, spr_filepath):
        iso.saveSpriteset(spr_filepath, vars.sprites)


    def displaySettings(self):
        dialog = SettingsDialog(self.main.root, self.main.settings)
