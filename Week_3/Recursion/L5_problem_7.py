def lenRecur(aStr):
    if aStr == "":
        return 0
    else:
        return 1 + lenRecur(aStr[1:])