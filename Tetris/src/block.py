from settings import *


class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        super().__init__(group)

        # image
        self.image = pygame.Surface(
            (cellSize, cellSize)
        )
        self.image.fill(color)

        # position
        self.pos = pygame.Vector2(pos) + blockOffset

        self.rect = self.image.get_rect(
            topleft=self.pos * cellSize
        )

    # rotation
    def rotate(self, pivotPosition):
        return (
            pivotPosition
            + (self.pos - pivotPosition).rotate(90)
        )

    # vertical collision
    def verticalCollide(self, y, fieldData):

        if y >= rows:
            return True

        if y >= 0 and fieldData[
            int(y)
        ][
            int(self.pos.x)
        ]:
            return True

        return False

    # horizontal collision
    def horizontalCollide(self, x, fieldData):

        if not 0 <= x < columns:
            return True

        # self.pos.y can be negative while the piece is still above the
        # visible field (e.g. right after spawning - blockOffset.y is -1,
        # and some pieces have a block a further row above that). Without
        # this guard, int(self.pos.y) is negative and Python indexes
        # fieldData from the END of the list instead of raising an error,
        # so a piece near the TOP of the board silently "collides" with
        # whatever is filled at the BOTTOM of the board. Confirmed this
        # was happening - see bug_proof.py.
        if self.pos.y >= 0 and fieldData[
            int(self.pos.y)
        ][
            int(x)
        ]:
            return True

        return False

    # update sprite rectangle
    def update(self):
        self.rect.topleft = self.pos * cellSize