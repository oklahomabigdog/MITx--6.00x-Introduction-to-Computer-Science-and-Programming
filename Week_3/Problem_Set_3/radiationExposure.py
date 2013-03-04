def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    if start >= stop - step:
        return f(stop-step) * step
    return (f(start) * step) + radiationExposure(start + step, stop, step)
    
    
    
# print radiationExposure(0, 5, 1)
# print radiationExposure(5, 11, 1)
# print radiationExposure(0, 11, 1)
# print radiationExposure(40, 100, 1.5)
