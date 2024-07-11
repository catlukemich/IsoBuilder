

class Image:
    def __init__(self, pil_image, tk_image, anchor, filename):
        self.pil_image = pil_image
        self.tk_image = tk_image
        self.anchor = anchor
        self.filename = filename

    def width(self):
        return self.tk_image.width()

    def height(self):
        return self.tk_image.height()