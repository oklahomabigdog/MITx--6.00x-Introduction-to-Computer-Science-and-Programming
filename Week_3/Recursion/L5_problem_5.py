def gcdRecur(a, b):
    c = min(a, b)
    d = max(a, b)
    if a%c == 0 and b%c == 0:
        return c
    else:
        return gcdRecur(b, a % b)