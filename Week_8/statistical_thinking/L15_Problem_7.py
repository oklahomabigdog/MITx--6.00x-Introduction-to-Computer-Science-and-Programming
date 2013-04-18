# ===============
# = Code To Run =
# ===============
import pylab
import random

STICKS = [1,2,3,4,5,6,7,8,9,10]

def drawStick():
    return random.choice(STICKS)

def plotDrawStick(numOfDraws, numBins=9):
    draws, draw_list = 0, []
    while draws < numOfDraws:
        draws += 1
        draw_list.append(drawStick())
    new_draw = []
    pylab.figure()
    pylab.title("Pick a Number 1-10")
    pylab.xlabel('Stick Number')
    pylab.ylabel('Out of ' + str(numOfDraws) + " Picks")
    pylab.ylim((1,numOfDraws))
    pylab.hist(draw_list, numBins, rwidth=.5, color='b')
    pylab.show()

if __name__ == '__main__':
    plotDrawStick(1000)