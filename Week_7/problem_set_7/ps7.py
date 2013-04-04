import math
import random
import ps7_visualize
import pylab
from ps7_verify_movement27 import testRobotMovement

# Remove raise NotImplementedError on the methods you add code to or you will
# have issues.

class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)

# =============
# = Problem 1 =
# =============
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

# === Problem 2
class StandardRobot(Robot):
    def updatePositionAndClean(self):
        if self.room.isPositionInRoom(self.pos.getNewPosition(self.dir, self.speed)):
            self.pos = self.pos.getNewPosition(self.dir, self.speed)
            self.room.cleanTileAtPosition(self.pos)
        else:
            self.dir = int(360 * random.random())

# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    totaltime = 0
    num = num_trials
    while num>0:
        room = RectangularRoom(width, height)
        i = num_robots
        robots= []
        while i>0:
            robots.append(robot_type(room, speed))
            i -= 1
        while min_coverage * room.getNumTiles() > room.getNumCleanedTiles():
            for robot in robots:
                robot.updatePositionAndClean()
            totaltime += 1
        num -= 1
    return float(totaltime/num_trials)

# === Problem 4
class RandomWalkRobot(Robot):
    def updatePositionAndClean(self):
        self.dir = int(360 * random.random())
        while not self.room.isPositionInRoom(self.pos.getNewPosition(self.dir, self.speed)):
            self.dir = int(360 * random.random())
        self.pos = self.pos.getNewPosition(self.dir, self.speed)
        self.room.cleanTileAtPosition(self.pos)

def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
# showPlot1("Time It Takes 1 - 10 Robots To Clean 80% Of A Room",
#     "Number of Robots", "Time-steps")
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
# showPlot2("Time It Takes A Robot To Clean 80% Of Variously Shaped Rooms ",
#     "Aspect Ratio", "Time-steps")
#
