from settings import *
from block import Block


class Tetromino:
    def __init__(
        self,
        shape,
        spriteGroup,
        createNewTetromino,
        fieldData
    ):
        # setup
        self.blockPosition = tetrominoShapes[shape]["shape"]
        self.color = tetrominoShapes[shape]["color"]
        self.createNewTetromino = createNewTetromino
        self.fieldData = fieldData
        self.shape = shape

        # blocks
        self.blocks = [
            Block(
                spriteGroup,
                self.blockPosition[i],
                self.color
            )
            for i in range(4)
        ]

    # collision detection
    def nextMoveHorizontalCollide(self, amount):
        collisionList = [
            block.horizontalCollide(
                int(block.pos.x + amount),
                self.fieldData
            )
            for block in self.blocks
        ]

        return any(collisionList)

    def nextMoveVerticalCollide(self, amount):
        collisionList = [
            block.verticalCollide(
                int(block.pos.y + amount),
                self.fieldData
            )
            for block in self.blocks
        ]

        return any(collisionList)

    # horizontal movement
    def moveHorizontal(self, amount):
        if not self.nextMoveHorizontalCollide(amount):
            for block in self.blocks:
                block.pos.x += amount

    # vertical movement
    def moveDown(self, amount):
        if not self.nextMoveVerticalCollide(amount):
            for block in self.blocks:
                block.pos.y += amount
        else:
            self.lock()

    # write blocks into the field and spawn the next tetromino
    def lock(self):
        # every shape spawns with blockOffset.y = -1, so ALL of a piece's
        # blocks start above row 0 (confirmed: T/J/L/S/Z/O spawn at y in
        # {-1,-2}, I spawns at y=-1 for all four). If a block is STILL
        # above row 0 at the moment it locks, the stack was too tall for
        # this piece to fully enter the field - that's a top-out, not a
        # normal lock.
        toppedOut = any(int(block.pos.y) < 0 for block in self.blocks)

        for block in self.blocks:
            # only write cells that are actually on the board. Without
            # this guard, a block locking above row 0 has a negative
            # int(pos.y), and Python indexes fieldData from the END of
            # the list, silently corrupting the BOTTOM row instead of
            # ending the game (same wraparound issue as horizontalCollide).
            if 0 <= int(block.pos.y) < rows:
                self.fieldData[
                    int(block.pos.y)
                ][
                    int(block.pos.x)
                ] = 1

        self.createNewTetromino(toppedOut)

    # how many rows this tetromino can currently fall before it lands
    def getGhostDropDistance(self):
        distance = 0
        while not self.nextMoveVerticalCollide(distance + 1):
            distance += 1
        return distance

    # instantly drop and lock the tetromino, returns rows dropped
    def hardDrop(self):
        distance = self.getGhostDropDistance()

        for block in self.blocks:
            block.pos.y += distance

        self.lock()
        return distance

    # rotation
    def rotate(self):
        if self.shape != "O":

            pivotPosition = self.blocks[0].pos

            newBlockPosition = [
                block.rotate(pivotPosition)
                for block in self.blocks
            ]

            # collision checking
            for pos in newBlockPosition:

                if pos.x < 0 or pos.x >= columns:
                    return

                if pos.y >= rows:
                    return

                if (
                    pos.y >= 0
                    and self.fieldData[
                        int(pos.y)
                    ][
                        int(pos.x)
                    ]
                ):
                    return

            # apply rotation
            for i, block in enumerate(self.blocks):
                block.pos = newBlockPosition[i]