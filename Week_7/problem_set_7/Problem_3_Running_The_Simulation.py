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
