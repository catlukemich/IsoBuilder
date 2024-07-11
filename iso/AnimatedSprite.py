import random
from .IsoSprite import IsoSprite
from .Viewport import ViewportUpdateable
from .ImageIsoSprite import ImageIsoSprite

class AnimatedSprite(ImageIsoSprite, ViewportUpdateable):
    def __init__(self, animation_images):
        ImageIsoSprite.__init__(self, animation_images[0])
        self.animation_images = animation_images
        self.current_frame = 0
        self.length = len(animation_images)
        self.time_so_far = 0
        self.frame_time_ms = 30

    def setFrameRate(self, framerate):
        self.frame_time_ms = 1 / framerate * 1000

    def setRandomFrame(self):
        self.current_frame = random.randint(0, self.length - 1)

    def viewportUpdate(self, clock):
        delta = clock.get_time()
        self.time_so_far += delta
        if self.time_so_far > self.frame_time_ms:
            self.current_frame += 1
            if self.current_frame == self.length:
                self.current_frame = 0
            self.setImage(self.animation_images[self.current_frame])
            self.time_so_far = self.time_so_far - self.frame_time_ms

    def setAnimation(self, animation_images):
        self.animation_images = animation_images

    def getAnimation(self):
        return self.animation_images