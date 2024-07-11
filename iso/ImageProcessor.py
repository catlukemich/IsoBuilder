import iso
import os
import PIL
from iso import Vector2D
from tkinter import *
from tkinter import filedialog

class ImageProcessor:
    def __init__(self):
        self.cutoff_alpha = 220

    def processImage(self, raw_image):
        cropped = self.cropImage(raw_image)
        processed = self.cutoffAlpha(cropped)
        return processed

    def calcAnchor(self, image):
        bbox = image.getbbox()
        center = (image.width / 2, image.height / 2)
        anchor_x = center[0] - bbox[0]
        anchor_y = center[1] - bbox[1]
        anchor = Vector2D(anchor_x, anchor_y)
        return anchor


    def cropImage(self, image):
        for x in range(0, image.width):
            for y in range(0, image.height):
                pixel = image.getpixel((x, y))
                if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0 and pixel[3] > 0:
                    pixel = (1,1,1,255)
                    image.putpixel((x, y), pixel)
                if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                    pixel = (0, 0, 0, 0)
                    image.putpixel((x, y), pixel)

        center = (image.width / 2, image.height / 2)
        bbox = image.getbbox()
        cropped_img = image.crop(bbox)
        return cropped_img

    def cutoffAlpha(self, image):
        for x in range(0, image.width):
            for y in range(0, image.height):
                pixel = image.getpixel((x, y))

                if pixel[3] < self.cutoff_alpha:
                    pixel = (0, 0, 0, 0)
                    image.putpixel((x, y), pixel)
        return image