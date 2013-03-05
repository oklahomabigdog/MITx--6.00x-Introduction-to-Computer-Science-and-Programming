def foo(x, a):
    """
    x: a positive integer argument
    a: a positive integer argument

    returns an integer
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
        return count


print "\n============"
print "Test Suite B"
print "============"
print foo(10, 3)
print foo(1, 4)
print foo(10, 6)
