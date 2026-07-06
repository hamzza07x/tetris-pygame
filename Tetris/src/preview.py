from settings import *

class Preview:
    def __init__(self):
        self.surface = pygame.Surface((sideBarWidth, gameHeight * previewHeightFraction - padding))
        self.rect = self.surface.get_rect(topright = (windowWidth - padding, padding))
        self.displaySurface = pygame.display.get_surface()

    def run(self):
        # display
        self.displaySurface.blit(self.surface, self.rect)