from settings import *
from os.path import join, dirname
from timer import Timer
from tetromino import Tetromino


class Game:
    def __init__(self, getNextShape, updateScore):
        # general
        self.surface = pygame.Surface((gameWidth, gameHeight))
        self.displaySurface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft=(padding, padding))
        self.sprites = pygame.sprite.Group()

        self.getNextShape = getNextShape
        self.updateScore = updateScore

        # lines
        self.linesSurface = self.surface.copy()
        self.linesSurface.fill((0, 255, 0))
        self.linesSurface.set_colorkey((0, 255, 0))
        self.linesSurface.set_alpha(120)

        # tetromino
        self.fieldData = [
            [0 for x in range(columns)]
            for y in range(rows)
        ]

        self.tetromino = Tetromino(
            self.getNextShape(),
            self.sprites,
            self.createNewTetromino,
            self.fieldData
        )

        # speed
        self.downSpeed = updateStartSpeed
        self.downSpeedFaster = self.downSpeed * 0.3
        self.downPressed = False

        # timers
        self.timers = {
            "vertical move": Timer(
                self.downSpeed,
                True,
                self.moveDown
            ),
            "horizontal move": Timer(moveWaitTime),
            "rotate": Timer(rotateWaitTime)
        }

        self.timers["vertical move"].activate()

        # score
        self.currentLevel = 1
        self.currentScore = 0
        self.currentLines = 0

        # state
        self.paused = False
        self.gameOver = False
        self.pauseStart = 0

        # font for the pause / game over overlay text
        fontPath = join(
            dirname(__file__),
            "..",
            "assets",
            "graphics",
            "Russo_One.ttf"
        )
        self.overlayFont = pygame.font.Font(fontPath, 32)

    # score
    def calculateScore(self, numLines):
        if numLines == 0:
            return

        # add completed lines to total
        self.currentLines += numLines

        # add score instead of replacing it
        self.currentScore += (
            scoreData[numLines] * self.currentLevel
        )

        # level up every 10 lines
        newLevel = self.currentLines // 10 + 1

        if newLevel > self.currentLevel:
            self.currentLevel = newLevel

            # increase falling speed
            self.downSpeed *= 0.75

            # calculate fast drop from the new normal speed
            self.downSpeedFaster = self.downSpeed * 0.3

            # update timer speed
            self.timers["vertical move"].duration = self.downSpeed

        # update score display
        self.updateScore(
            self.currentLines,
            self.currentScore,
            self.currentLevel
        )

    # create new tetromino (called by Tetromino.lock)
    def createNewTetromino(self, gameOver=False):
        # still credit any rows the piece that just locked completed,
        # even if it's the one that topped the stack out
        self.checkFinishedRows()

        if gameOver:
            self.gameOver = True
            self.timers["vertical move"].deactivate()
            return

        self.tetromino = Tetromino(
            self.getNextShape(),
            self.sprites,
            self.createNewTetromino,
            self.fieldData
        )

    # timer
    def timerUpdate(self):
        for timer in self.timers.values():
            timer.update()

    # move down
    def moveDown(self):
        if self.downPressed:
            self.currentScore += softDropPoints
            self.updateScore(
                self.currentLines,
                self.currentScore,
                self.currentLevel
            )

        self.tetromino.moveDown(1)

    # instantly drop the current tetromino
    def hardDrop(self):
        if self.paused or self.gameOver:
            return

        distance = self.tetromino.hardDrop()

        if distance > 0:
            self.currentScore += distance * hardDropPoints
            self.updateScore(
                self.currentLines,
                self.currentScore,
                self.currentLevel
            )

    # pause / resume
    def togglePause(self):
        if self.gameOver:
            return

        self.paused = not self.paused

        if self.paused:
            self.pauseStart = pygame.time.get_ticks()
        else:
            # shift every active timer forward by however long we were
            # paused, so nothing "catches up" instantly the moment we resume
            pausedFor = pygame.time.get_ticks() - self.pauseStart
            for timer in self.timers.values():
                if timer.active:
                    timer.startTime += pausedFor

    # draw grid
    def drawGrid(self):
        for cols in range(1, columns):
            pygame.draw.line(
                self.surface,
                lineColor,
                (cols * cellSize, 0),
                (
                    cols * cellSize,
                    self.surface.get_height()
                ),
                1
            )

        for row in range(1, rows):
            pygame.draw.line(
                self.surface,
                lineColor,
                (0, row * cellSize),
                (
                    self.surface.get_width(),
                    row * cellSize
                ),
                1
            )

        self.surface.blit(self.linesSurface, (0, 0))

    # ghost piece - translucent preview of where the tetromino will land
    def drawGhost(self):
        dropDistance = self.tetromino.getGhostDropDistance()

        if dropDistance <= 0:
            return

        ghostSurface = pygame.Surface((cellSize, cellSize))
        ghostSurface.set_alpha(90)
        ghostSurface.fill(self.tetromino.color)

        for block in self.tetromino.blocks:
            pos = (block.pos + pygame.Vector2(0, dropDistance)) * cellSize
            self.surface.blit(ghostSurface, pos)

    # dimmed overlay for paused / game over states
    def drawOverlay(self, text):
        overlay = pygame.Surface(self.surface.get_size())
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.surface.blit(overlay, (0, 0))

        textSurface = self.overlayFont.render(text, True, "white")
        textRect = textSurface.get_rect(
            center=(
                self.surface.get_width() / 2,
                self.surface.get_height() / 2
            )
        )
        self.surface.blit(textSurface, textRect)

    # input
    def input(self):
        keys = pygame.key.get_pressed()

        # horizontal movement
        if not self.timers["horizontal move"].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.moveHorizontal(-1)
                self.timers["horizontal move"].activate()

            elif keys[pygame.K_RIGHT]:
                self.tetromino.moveHorizontal(1)
                self.timers["horizontal move"].activate()

        # rotation
        if not self.timers["rotate"].active:
            if keys[pygame.K_UP]:
                self.tetromino.rotate()
                self.timers["rotate"].activate()

        # fast downward movement
        if not self.downPressed and keys[pygame.K_DOWN]:
            self.downPressed = True
            self.timers["vertical move"].duration = self.downSpeedFaster

        # restore normal downward movement
        if self.downPressed and not keys[pygame.K_DOWN]:
            self.downPressed = False
            self.timers["vertical move"].duration = self.downSpeed

    # check completed rows
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
                self.fieldData.insert(
                    0,
                    [0 for x in range(columns)]
                )

            # move existing blocks down
            for block in self.sprites:
                rowsToMove = sum(
                    int(block.pos.y) < row
                    for row in deleteRows
                )

                block.pos.y += rowsToMove

            # calculate score
            self.calculateScore(len(deleteRows))

    # game loop
    def run(self):
        self.surface.fill(gray)

        if not self.paused and not self.gameOver:
            self.input()
            self.timerUpdate()
            self.sprites.update()
            self.drawGhost()

        # drawing the grid
        self.sprites.draw(self.surface)
        self.drawGrid()

        if self.paused:
            self.drawOverlay("PAUSED")
        elif self.gameOver:
            self.drawOverlay("GAME OVER")

        # display
        self.displaySurface.blit(
            self.surface,
            (padding, padding)
        )

        pygame.draw.rect(
            self.displaySurface,
            lineColor,
            self.rect,
            2,
            2
        )
