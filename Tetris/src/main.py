from settings import *
from sys import exit
from random import shuffle
# components
from game import Game
from score import Score
from preview import Preview


class Main:
    def __init__(self):
        # general
        pygame.init()
        self.displaySurface = pygame.display.set_mode((windowWidth, windowHeight))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris")

        # 7-bag shape queue: guarantees every tetromino appears exactly
        # once every 7 pieces instead of plain random.choice(), which can
        # hand out long droughts (no I piece for ages) or streaks (the
        # same piece back-to-back).
        self.bag = []
        self.nextShapes = [self.getBagShape() for _ in range(3)]

        self.score = Score()
        self.game = Game(self.getNextShape, self.score.updateScore)
        self.preview = Preview()

    def getBagShape(self):
        if not self.bag:
            self.bag = list(tetrominoShapes.keys())
            shuffle(self.bag)
        return self.bag.pop()

    def getNextShape(self):
        nextShape = self.nextShapes.pop(0)
        self.nextShapes.append(self.getBagShape())
        return nextShape

    def restart(self):
        self.bag = []
        self.nextShapes = [self.getBagShape() for _ in range(3)]
        self.score = Score()
        self.game = Game(self.getNextShape, self.score.updateScore)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if self.game.gameOver:
                        if event.key in (pygame.K_RETURN, pygame.K_r):
                            self.restart()
                    elif event.key == pygame.K_SPACE:
                        self.game.hardDrop()
                    elif event.key in (pygame.K_p, pygame.K_ESCAPE):
                        self.game.togglePause()

            # display
            self.displaySurface.fill(gray)
            self.game.run()
            self.score.run()
            self.preview.run(self.nextShapes)
            # updating the game
            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    main = Main()
    main.run()
