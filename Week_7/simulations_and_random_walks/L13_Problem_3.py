import random
def deterministicNumber():
    '''
    Deterministically generates an even number between 9 and 21
    '''
    return 10

def stochasticNumber():
    '''
    Stochastically generates a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10, 22, 2)
