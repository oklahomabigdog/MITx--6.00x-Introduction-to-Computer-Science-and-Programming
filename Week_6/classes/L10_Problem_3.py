def isPrime(n):
    if type(n) != int: raise TypeError
    if n < 0: raise ValueError
    if n == 0: raise ValueError
    if n == 2: return True
    if not n & 1: return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0: return False
    return True

print isPrime(3)