from settings import *
from pygame.image import load
from os import path


class Preview:
    def __init__(self):
        previewHeight = int(gameHeight * previewHeightFraction - padding)
        self.surface = pygame.Surface(
            (sideBarWidth, previewHeight)
        )
        self.rect = self.surface.get_rect(
            topright=(windowWidth - padding, padding)
        )
        self.displaySurface = pygame.display.get_surface()

        graphicsPath = path.join(
            path.dirname(__file__),
            "..",
            "assets",
            "graphics"
        )

        self.shapeSurface = {
            shape: load(
                path.join(graphicsPath, f"{shape}.png")
            ).convert_alpha()
            for shape in tetrominoShapes.keys()
        }
        self.fragmentHeight = self.surface.get_height() / 3
    
    def displayPieces(self, shapes):
        for i, shape in enumerate(shapes):
            shapeSurface = self.shapeSurface[shape]
            x = self.surface.get_width() / 2
            y = self.fragmentHeight / 2 + i * self.fragmentHeight
            rect = shapeSurface.get_rect(center=(x, y))
            self.surface.blit(shapeSurface, rect)

    def run(self, nextShapes):
        self.surface.fill(gray)
        self.displayPieces(nextShapes)
        self.displaySurface.blit(self.surface, self.rect)
        pygame.draw.rect(self.displaySurface, lineColor, self.rect, 2, 2)
