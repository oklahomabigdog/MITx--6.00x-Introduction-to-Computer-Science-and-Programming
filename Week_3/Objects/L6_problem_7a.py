def makePositive(a):
    count = 0
    for i in testList:
        if i < 0:
            testList[count] = abs(i)
        count += 1
    return a

applyToEach(testList, makePositive)