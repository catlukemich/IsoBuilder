# Abstract class


class UpdateInterval:
    EVERY_FRAME = 0
    EVERY_SECOND = 1
    EVERY_TEN_SECONDS = 2
    EVERY_MINUTE = 3


class Updateable:
    def update(self, delta_time):
        pass

    def getUpdateInterval(self):
        return UpdateInterval.EVERY_FRAME


class Updater():
    def __init__(self):
        self.time_frame = 0
        self.time_second = 0
        self.time_ten_seconds = 0

        self.updateables_every_frame = []
        self.updateables_every_second = []
        self.updateables_every_ten_seconds = []
        self.updateables_every_minute = []

    def addUpdateable(self, updateable):
        interval = updateable.getUpdateInterval()
        if interval == UpdateInterval.EVERY_FRAME:
            self.updateables_every_frame.append(updateable)
        if interval == UpdateInterval.EVERY_SECOND:
            self.updateables_every_second.append(updateable)
        if interval == UpdateInterval.EVERY_TEN_SECONDS:
            self.updateables_every_ten_seconds.append(updateable)
        if interval == UpdateInterval.EVERY_MINUTE:
            self.updateables_every_minute.append(updateable)

    def removeUpdateable(self, updateable):
        interval = updateable.getUpdateInterval()
        if interval == UpdateInterval.EVERY_FRAME:
            self.updateables_every_frame.remove(updateable)
        if interval == UpdateInterval.EVERY_SECOND:
            self.updateables_every_second.remove(updateable)
        if interval == UpdateInterval.EVERY_TEN_SECONDS:
            self.updateables_every_ten_seconds.remove(updateable)
        if interval == UpdateInterval.EVERY_MINUTE:
            self.updateables_every_minute.remove(updateable)

    def update(self, clock):
        delta = clock.get_time()
        for frame_updateable in self.updateables_every_frame:
            frame_updateable.update(delta)
        self.time_frame += delta
        if self.time_frame > 1000:
            self.time_second += self.time_frame
            self.time_frame = self.time_frame - 1000
            for second_updateable in self.updateables_every_second:
                second_updateable.update(1000)
            if self.time_second >= 10000:
                self.time_second = 0
                self.time_ten_seconds += 10000
                for ten_seconds_updateable in self.updateables_every_ten_seconds:
                    ten_seconds_updateable.update(10000)
                if self.time_ten_seconds >= 60000:
                    self.time_ten_seconds = 0
                    for minute_updateable in self.updateables_every_minute:
                        minute_updateable.update(60000)
