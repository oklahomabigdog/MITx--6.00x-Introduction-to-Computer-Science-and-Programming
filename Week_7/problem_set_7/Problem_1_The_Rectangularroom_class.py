class RectangularRoom(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cleaned = []

    def cleanTileAtPosition(self, pos):
        x = math.floor(pos.getX())
        y = math.floor(pos.getY())
        if (x,y) not in self.cleaned:
            self.cleaned.append((x,y))

    def isTileCleaned(self, m, n):
        return (m,n) in self.cleaned

    def getNumTiles(self):
        return self.width * self.height

    def getNumCleanedTiles(self):
        return len(self.cleaned)

    def getRandomPosition(self):
        x = random.choice(range(self.width))
        y = random.choice(range(self.height))
        pos = Position(x,y)
        return pos

    def isPositionInRoom(self, pos):
        return (0 <= pos.getX() < self.width and 0 <= pos.getY() < self.height)
