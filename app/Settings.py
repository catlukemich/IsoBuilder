class Settings:

    def __init__(self):
        self.use_bounds = True
        self.tile_width = 64
        self.tile_height = 32
        self.listeners = []

    def addSettingsListener(self, listener):
        self.listeners.append(listener)
        self.fireChangeEvent()

    def removeSettingsListener(self, listener):
        self.listeners.remove(listener)
        self.fireChangeEvent()

    def setUseBounds(self, use):
        self.use_bounds = use
        self.fireChangeEvent()

    def fireChangeEvent(self):
        for listener in self.listeners:
            listener.settingsChanged(self)