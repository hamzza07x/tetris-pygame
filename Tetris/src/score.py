from settings import *

class Score:
    def __init__(self):
        self.surface = pygame.Surface((sideBarWidth, gameHeight * scoreHeightFraction - padding))
        self.rect = self.surface.get_rect(bottomright = (windowWidth - padding, windowHeight - padding))
        self.displaySurface = pygame.display.get_surface()

    def run(self):
        # display
        self.displaySurface.blit(self.surface, self.rect)