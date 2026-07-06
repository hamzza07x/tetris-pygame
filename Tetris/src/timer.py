from pygame.time import get_ticks
class Timer:
    def __init__(self, duration, repeated = False, func = None):
        self.repeated = repeated
        self.duration = duration
        self.func = func

        self.startTime = 0
        self.active = False
    
    def activate(self):
        self.active = True
        self.startTime = get_ticks()
    
    def deactiate(self):
        self.active = False
        self.startTime = 0
    
    def update(self):
        currentTime = get_ticks()
        if currentTime - self.startTime >= self.duration and self.active:
            if self.func and self.startTime != 0:
                self.func()
            # reset timer
            self.deactiate()
            # repeat timer
            if self.repeated:
                self.activate()