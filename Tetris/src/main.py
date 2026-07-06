from settings import *
from sys import exit
# components
from game import Game
from score import Score
from preview import Preview

class Main:
    def __init__(self):
        #general
        pygame.init()
        self.displaySurface = pygame.display.set_mode((windowWidth, windowHeight))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris")
        self.game = Game()
        self.score = Score()
        self.preview = Preview()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            #display
            self.displaySurface.fill(gray)
            self.game.run()
            self.score.run()
            self.preview.run()
            # updating the game
            pygame.display.update()
            self.clock.tick()

if __name__ == "__main__":
    main = Main()
    main.run()