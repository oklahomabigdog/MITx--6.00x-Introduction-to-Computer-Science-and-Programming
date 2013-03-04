def recurPowerNew(base, exp):
    if exp == 0:
        return 1
    elif base % 2 == 0:
        return base * recurPowerNew(base, (exp / 2))
    else:
        return base * recurPowerNew(base, (exp - 1))