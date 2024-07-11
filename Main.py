from tkinter import *
from tkinter.ttk import *
from app.ControlsFrame import *
from app.MenuHandler import  *
from app.InputDispatcher import *
from app.SpriteAligner import *
from app.Settings import Settings

class Main:

    def __init__(self):
        self.settings = None
        self.input = None
        self.viewport = None
        self.scene = None
        self.canvas = None
        self.scroller = None
        self.aligner = None  # The sprite handler used to align the sprites and their's bounding boxes
        self.controls = None  # The controls reference (the ControlFrame instance) which displays sprite informattion.
        self.sprites = []

        self.root = Tk()
        self.loadSettings()
        self.createMenu()
        self.createCanvas()
        self.createIso()
        self.createControls()
        self.settings.addSettingsListener(self)


    def createMenu(self):
        self.menu_handler = MenuHandler(self)
        menu = Menu(self.root)
        self.root["menu"] = menu
        self.createFileMenu(menu)
        self.createSettingsMenu(menu)


    def createFileMenu(self, menu):
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.menu_handler.new)
        file_menu.add_command(label="Open...", command=self.menu_handler.open)
        file_menu.add_command(label="Add image..", command=self.menu_handler.addImage)
        file_menu.add_command(label="Add animation..", command=self.menu_handler.addAnimation)
        file_menu.add_command(label="Save..", command=self.menu_handler.save)
        self.root.bind_all("<Control-s>", self.menu_handler.save)

    def createSettingsMenu(self, menu):
        settings_menu = Menu(menu)
        menu.add_cascade(label="Settings", menu=settings_menu)
        settings_menu.add_command(label="Settings", command=self.menu_handler.displaySettings)

    def createCanvas(self):
        self.canvas = Canvas(self.root, width=800, height=800)
        self.canvas.pack(side=LEFT)

    def createControls(self):
        self.controls = ControlsFrame(self)
        self.controls.pack(side=RIGHT, fill=BOTH, expand=True)

    def createIso(self):
        self.input = iso.Input()
        grid = iso.SceneGrid(40,2,2)
        self.scene = iso.Scene(grid)
        self.aligner = SpriteAligner(self)
        self.aligner.enable()
        self.viewport = iso.Viewport(self.canvas, self.scene)
        dispatcher = InputDispatcher(self)
        dispatcher.bind()

        self.scroller = iso.Scroller(self.viewport, self.input)
        self.scroller.enable()

    def loadSettings(self):
        self.settings = Settings()


    def settingsChanged(self, settings):
        self.viewport.setDrawBounds(settings.use_bounds)

    def loop(self):
        self.redraw()
        self.root.after(40, self.loop)

    def redraw(self):
        self.canvas.delete(ALL)
        clock = iso.TkClock()
        self.viewport.update(clock)
        self.viewport.draw()

    def start(self):
        self.root.mainloop()



if __name__ == "__main__":
    main = Main()
    main.loop()
    main.start()

