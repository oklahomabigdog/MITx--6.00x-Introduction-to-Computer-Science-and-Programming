# =======================================
# = From Problem 1 RectangularRoom Class=
# =======================================
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

# ===================
# = Current Problem =
# ===================
class Robot(object):
    def __init__(self, room, speed):
        self.dir = int(360 * random.random())
        self.pos = Position(room.width * random.random(),room.height * random.random())
        self.room = room
        self.room.cleanTileAtPosition(self.pos)
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError("Zero is not a speed.")

    def getRobotPosition(self):
        return self.pos
    
    def getRobotDirection(self):
        return self.dir

    def setRobotPosition(self, position):
        self.pos = position

    def setRobotDirection(self, direction):
        self.dir = direction

    def updatePositionAndClean(self):
        raise NotImplementedError # don't change this!
