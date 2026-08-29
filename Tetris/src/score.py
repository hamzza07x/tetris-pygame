from settings import *
from os.path import join, dirname


class Score:
    def __init__(self):
        # general
        scoreHeight = int(gameHeight * scoreHeightFraction - padding)
        self.surface = pygame.Surface(
            (
                sideBarWidth,
                scoreHeight
            )
        )

        self.rect = self.surface.get_rect(
            bottomright=(
                windowWidth - padding,
                windowHeight - padding
            )
        )

        self.displaySurface = pygame.display.get_surface()

        # font
        fontPath = join(
            dirname(__file__),
            "..",
            "assets",
            "graphics",
            "Russo_One.ttf"
        )

        self.font = pygame.font.Font(fontPath, 30)

        # increment
        self.incrementHeight = self.surface.get_height() / 3

        # data
        self.score = 0
        self.level = 1
        self.lines = 0

    def updateScore(self, lines, score, level):
        self.lines = lines
        self.score = score
        self.level = level

    def displayText(self, pos, text):
        textSurface = self.font.render(
            f"{text[0]}: {text[1]}",
            True,
            "white"
        )

        textRect = textSurface.get_rect(
            center=pos
        )

        self.surface.blit(
            textSurface,
            textRect
        )

    def run(self):
        self.surface.fill(gray)

        for i, text in enumerate(
            [
                ("Score", self.score),
                ("Level", self.level),
                ("Lines", self.lines)
            ]
        ):
            x = self.surface.get_width() / 2
            y = (
                self.incrementHeight / 2
                + i * self.incrementHeight
            )

            self.displayText(
                (x, y),
                text
            )

        self.displaySurface.blit(
            self.surface,
            self.rect
        )

        pygame.draw.rect(
            self.displaySurface,
            lineColor,
            self.rect,
            2,
            2
        )
