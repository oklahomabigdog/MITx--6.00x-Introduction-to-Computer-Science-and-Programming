# ==================================
# = Required Class of Robot to Run =
# ==================================
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

# ===================
# = Current Problem =
# ===================
class RandomWalkRobot(Robot):
    def updatePositionAndClean(self):
        self.dir = int(360 * random.random())
        while not self.room.isPositionInRoom(self.pos.getNewPosition(self.dir, self.speed)):
            self.dir = int(360 * random.random())
        self.pos = self.pos.getNewPosition(self.dir, self.speed)
        self.room.cleanTileAtPosition(self.pos)
