def gcdIter(a, b):
    c = min(a, b)
    d = max(a, b)
    if a%c == 0 and b%c == 0:
        return c
    else:
        while a%c != 0 or b%c != 0:
            c -= 1
            if int(c) == 1:
                break
        return int(c)