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
        self.fieldData = [[0 for x in range(columns)] for y in range(rows)]
        self.tetromino = Tetromino(choice(list(tetrominoShapes.keys())), self.sprites,self.createNewTetromino,self.fieldData)
        self.timers = {
            "vertical move": Timer(updateStartSpeed, True, self.moveDown),
            "horizontal move": Timer(moveWaitTime)
        }
        self.timers["vertical move"].activate()

    def createNewTetromino(self):
        self.checkFinishedRows()
        self.tetromino = Tetromino(choice(list(tetrominoShapes.keys())), self.sprites,self.createNewTetromino,self.fieldData)

    def timerUpdate(self):
        for timer in self.timers.values():
            timer.update()
    
    def moveDown(self):
        self.tetromino.moveDown(1)
    
    def drawGrid(self):
        for cols in range(1,columns):
            pygame.draw.line(self.surface, lineColor, (cols * cellSize, 0), (cols * cellSize, self.surface.get_height()), 1)
        for row in range(1,rows):
            pygame.draw.line(self.surface, lineColor, (0, row * cellSize), (self.surface.get_width(), row * cellSize), 1)
        self.surface.blit(self.linesSurface, (0,0))

    def input(self):
        if not self.timers["horizontal move"].active:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.tetromino.moveHorizontal(-1)
                self.timers["horizontal move"].activate()
            elif keys[pygame.K_RIGHT]:
                self.tetromino.moveHorizontal(1)
                self.timers["horizontal move"].activate()

    def checkFinishedRows(self):
        deleteRows = []

        for i, row in enumerate(self.fieldData):
            if all(row):
                deleteRows.append(i)

        if deleteRows:
            # remove blocks belonging to completed rows
            for block in self.sprites:
                if int(block.pos.y) in deleteRows:
                    block.kill()

            # remove completed rows from field data
            for row in sorted(deleteRows, reverse=True):
                del self.fieldData[row]

            # add empty rows at the top
            for _ in deleteRows:
                self.fieldData.insert(0, [0 for x in range(columns)])

            # move existing blocks down
            for block in self.sprites:
                rows_to_move = sum(int(block.pos.y) < row for row in deleteRows)
                block.pos.y += rows_to_move

    def run(self):
        self.input()
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
    def __init__(self, shape, spriteGroup,createNewTetromino,fieldData):
        #setup
        self.blockPosition = tetrominoShapes[shape]['shape']
        self.color = tetrominoShapes[shape]['color']
        self.createNewTetromino = createNewTetromino
        self.fieldData = fieldData

        #blocks
        self.blocks = [Block(spriteGroup, self.blockPosition[i], self.color) for i in range(4)]
    # collisions
    def nextMoveHorizontalCollide(self,block,amount):
        collisionList = [block.horizontalCollide(int(block.pos.x + amount),self.fieldData) for block in  self.blocks]
        if any(collisionList):
            return True
        else:
            return False
    
    def nextMoveVerticalCollide(self,block,amount):
        collisionList = [block.verticalCollide(int(block.pos.y + amount),self.fieldData) for block in  self.blocks]
        if any(collisionList):
            return True
        else:
            return False
        
    #movement
    def moveHorizontal(self,amount):
        if not self.nextMoveHorizontalCollide(self.blocks, amount):
            for block in self.blocks:
                block.pos.x = block.pos.x + amount

    def moveDown(self,amount):
        if not self.nextMoveVerticalCollide(self.blocks,amount):
            for block in self.blocks:
                block.pos.y = block.pos.y + 1
        else:
            for block in self.blocks:
                self.fieldData[int(block.pos.y)][int(block.pos.x)] = 1
            self.createNewTetromino()
            

class Block(pygame.sprite.Sprite):
    def __init__(self, group,pos,color):
        #general
        super().__init__(group)
        self.image = pygame.Surface((cellSize, cellSize))
        self.image.fill(color)
        #position
        self.pos = pygame.Vector2(pos) + blockOffset
        self.rect = self.image.get_rect(topleft = self.pos * cellSize)

    def verticalCollide(self, y,filedData):
        if y >= rows:
            return True
        if y >= 0 and filedData[int(y)][int(self.pos.x)]:
            return True
        
    def horizontalCollide(self, x,fieldData):
        if not 0 <= x < columns:
            return True
        if fieldData[int(self.pos.y)][int(x)]:
            return True
        
    def update(self):
        self.rect.topleft = self.pos * cellSize
