import random

def draw():
    balls = ["r", "r", "r", "g", "g", "g"]
    selected = []
    for i in range(3):
        ball = random.choice(balls)
        balls.remove(ball)
        selected.append(ball)
    if (selected[0] == selected[1]) & (selected[1] == selected[2]):
        return True
    return False

def noReplacementSimulation(numTrials):
    true = 0
    for n in range(numTrials):
        if draw():
            true += 1
    return float(true)/float(numTrials)

print noReplacementSimulation(5000)