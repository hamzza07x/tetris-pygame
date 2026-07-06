from settings import *
from random import choice
from timer import Timer

class Game:
    def __init__(self):
        #general
        self.surface = pygame.Surface((gameWidth,gameHeight))
        self.displaySurface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft = (padding, padding))
        self.sprites = pygame.sprite.Group()
        # lines
        self.linesSurface = self.surface.copy()
        self.linesSurface.fill((0,255,0))
        self.linesSurface.set_colorkey((0,255,0))
        self.linesSurface.set_alpha(120)

        #tetromino
        self.tetromino = Tetromino(choice(list(tetrominoShapes.keys())), self.sprites)
        self.timers = {
            "vertical move": Timer(updateStartSpeed, True, self.moveDown),
        }
        self.timers["vertical move"].activate()

    def timerUpdate(self):
        for timer in self.timers.values():
            timer.update()
    
    def moveDown(self):
        self.tetromino.moveDown()
    
    def drawGrid(self):
        for cols in range(1,columns):
            pygame.draw.line(self.surface, lineColor, (cols * cellSize, 0), (cols * cellSize, self.surface.get_height()), 1)
        for row in range(1,rows):
            pygame.draw.line(self.surface, lineColor, (0, row * cellSize), (self.surface.get_width(), row * cellSize), 1)
        self.surface.blit(self.linesSurface, (0,0))

    def run(self):
        self.timerUpdate()
        self.sprites.update()
        # drwaing the grid
        self.surface.fill(gray)
        self.sprites.draw(self.surface)
        self.drawGrid()
        # display
        self.displaySurface.blit(self.surface,(padding,padding))
        pygame.draw.rect(self.displaySurface, lineColor, self.rect, 2,2)

class Tetromino:
    def __init__(self, shape, spriteGroup):
        #setup
        self.blockPosition = tetrominoShapes[shape]['shape']
        self.color = tetrominoShapes[shape]['color']

        #blocks
        self.blocks = [Block(spriteGroup, self.blockPosition[i], self.color) for i in range(4)]
    
    def moveDown(self):
        for block in self.blocks:
            block.pos.y = block.pos.y + 1

class Block(pygame.sprite.Sprite):
    def __init__(self, group,pos,color):
        #general
        super().__init__(group)
        self.image = pygame.Surface((cellSize, cellSize))
        self.image.fill(color)
        #position
        self.pos = pygame.Vector2(pos) + blockOffset
        self.rect = self.image.get_rect(topleft = self.pos * cellSize)
    
    def update(self):
        self.rect.topleft = self.pos * cellSize