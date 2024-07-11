import os
import tempfile
import zipfile
import PIL.Image
import PIL.ImageTk
from .Image import Image
from .Vector2D import Vector2D
from .Vector3D import Vector3D
from .Bounds3D import Bounds3D
from .ImageIsoSprite import ImageIsoSprite
from .AnimatedSprite import AnimatedSprite
from .ImageProcessor import ImageProcessor

def loadSpriteSet(spr_path):
    zip = zipfile.ZipFile(spr_path)
    sprites_data = zip.open("sprites.txt")
    text = sprites_data.read().decode("utf-8")
    lines = text.split("\n")
    spriteset = []
    for line in lines:
        if not line: continue
        # Parse the data:
        data = line.split(" ")
        is_image = data[0] == "image"
        is_anim = data[0] == "anim"
        if is_anim:
            frames_count = int(data[1])
            start_index = 2
            end_index = start_index + frames_count
            frames = []
            for frame_index in range(start_index, end_index):
                frame_name = data[frame_index]
                image = loadZipppedImage(zip, frame_name)
                frames.append(image)
            sprite = AnimatedSprite(frames)


        elif is_image:
            img_path = data[1]
            image = loadZipppedImage(zip, img_path)
            sprite = ImageIsoSprite(image)
            end_index = 2

        location_x = float(data[end_index + 0])
        location_y = float(data[end_index + 1])
        location_z = float(data[end_index + 2])
        bounds_min_x = float(data[end_index + 3])
        bounds_max_x = float(data[end_index + 4])
        bounds_min_y = float(data[end_index + 5])
        bounds_max_y = float(data[end_index + 6])
        bounds_min_z = float(data[end_index + 7])
        bounds_max_z = float(data[end_index + 8])

        # Create location vector:
        location = Vector3D(location_x, location_y, location_z)
        # Create the bounds:
        bounds = Bounds3D()
        bounds.min_x = bounds_min_x
        bounds.max_x = bounds_max_x
        bounds.min_y = bounds_min_y
        bounds.max_y = bounds_max_y
        bounds.min_z = bounds_min_z
        bounds.max_z = bounds_max_z
        # Create and return a sprite:
        sprite.setLocation(location)
        sprite.setBounds(bounds)
        spriteset.append(sprite)
    sprites_data.close()
    zip.close()
    return spriteset


# Zip images already loaded:
zipimages = {}

# Load an image that is within a zip file.
# zip - a ZipFile instance
# image_name - the name of the file in zip file.
def loadZipppedImage(zip, image_name):
    global zipimages
    if image_name in zipimages:
        return zipimages[image_name]
    else:
        # Load the zip file
        zipped_image = zip.open(image_name)
        # Load the images that are the part of the iso.Image instance
        pil_image = PIL.Image.open(zipped_image)
        tk_image = PIL.ImageTk.PhotoImage(pil_image)
        zipped_image.close()
        # Load the anchor file:
        anchor_filename = image_name.replace(".png", "") + "_anchor.txt"
        anchor_file = zip.open(anchor_filename)
        anchor_contents = anchor_file.read().decode("utf-8")
        anchor_x = int(anchor_contents.split(" ")[0])
        anchor_y = int(anchor_contents.split(" ")[1])
        anchor = Vector2D(anchor_x, anchor_y)
        print(anchor)
        # Create Image instance, mark it as zipped, cache and return:
        image = Image(pil_image, tk_image, anchor, image_name)
        zipimages[image_name] = image
        return image



# Load animation frames
def loadAnimation(paths):
    animation_images = []
    for path in paths:
        image = loadImage(path)
        animation_images.append(image)
    return animation_images


# Image loader functions
images = {}
def loadImage(image_path):
    global images
    if(image_path in images):
        return images[image_path]
    else:
        raw_image = PIL.Image.open(image_path)
        processor = ImageProcessor()
        anchor = processor.calcAnchor(raw_image)
        pil_image = processor.processImage(raw_image)
        tk_image = PIL.ImageTk.PhotoImage(pil_image)
        image_filename = os.path.split(image_path)[1]
        image = Image(pil_image, tk_image, anchor, image_filename)
        images[image_path] = image
        return image



def saveSpriteset(filepath, sprites):
    sprite_file = zipfile.ZipFile(filepath, "w")
    data_string = ""
    for sprite in sprites:
        if isinstance(sprite, ImageIsoSprite) and not isinstance(sprite, AnimatedSprite):
            # The format of the sprite file is as follows:
            # [image_filename] [location.x] [location.y] [location.z]
            #       [bound_min_x] [bounds_max_x] [bound_min_y] [bounds_max_y]
            #       [bounds_min_z] [bounds_max_z]

            # Write the image to the zipfile:
            image = sprite.getImage()
            tmp_filename = tempfile.gettempdir() + os.sep + image.filename
            if not image.filename in sprite_file.namelist():
                image.pil_image.save(tmp_filename)
                sprite_file.write(tmp_filename, arcname=image.filename)
                os.remove(tmp_filename)

            data_string += "image "
            data_string += "%s " % image.filename


        elif isinstance(sprite, AnimatedSprite):
            data_string += "anim "
            images = sprite.getAnimation()
            data_string += str(len(images)) + " "
            for image in images:
                tmp_filename = tempfile.gettempdir() + os.sep + image.filename
                if not image.filename in sprite_file.namelist():
                    image.pil_image.save(tmp_filename)
                    sprite_file.write(tmp_filename, arcname=image.filename)
                    os.remove(tmp_filename)

                data_string += "%s " % image.filename
                anchor_filename = image.filename.replace(".png", "") + "_anchor.txt"
                sprite_file.writestr(anchor_filename, "%d %d"% (image.anchor.x, image.anchor.y) )

        location = sprite.getLocation()
        bounds = sprite.getBounds()
        data_string += f"{location.x} {location.y} {location.z} " \
                       f"{bounds.min_x} {bounds.max_x} {bounds.min_y} {bounds.max_y} {bounds.min_z} {bounds.max_z} " \
                       f"\n"

    sprite_file.writestr("sprites.txt", data_string)