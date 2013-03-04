def iterPower(base, exp):
    result = base
    while exp > 1:
        result = base * result
        exp -= 1
    if exp == 0:
        result = 1.0000
    return result

print iterPower(6.3, 5)