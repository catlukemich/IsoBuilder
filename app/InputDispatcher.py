
class InputDispatcher:

    def __init__(self, main):
        self.main = main

    def bind(self):
        self.main.canvas.bind("<ButtonPress>", self.dispatchMousePress)
        self.main.canvas.bind("<ButtonRelease>", self.main.input.mouseButtonUp)
        self.main.canvas.bind("<Motion>", self.main.input.mouseMotion)
        self.main.canvas.bind("<Key>", self.main.input.keyDown)


    def dispatchMousePress(self, event):
        self.main.canvas.focus_set()
        self.main.input.mouseButtonDown(event)