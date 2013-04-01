class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8
w1 = Weird(X, Y)
w2 = Wild(X, Y)
w3 = Wild(17, 18)
w4 = Wild(X, 18)
X = w4.getX() + w3.getX() + w2.getX()
Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
# print w1.getX() # NoneType=> Error
# print w1.getY() # NoneType=> Error
# print w2.getX() # Int => 7
# print w2.getY() # Int => 8
# print w3.getX() # Int => 17
# print w3.getY() # Int => 18
# print w4.getX() # Int => 7
# print w4.getY() # Int => 18
# print X         # Int => 31
# print w4.getX() # Int => 7
# print Y         # Int => 44
# print w2.getY() # Int => 8

