def isIn(char, aStr):
    if len(aStr) == 0:
        return False
    split = len(aStr) / 2
    while char != aStr[split]:
        if split == 0:
            return False
        if char < aStr[split]:
            return isIn(char, aStr[:split])
        if char > aStr[split]:
            return isIn(char, aStr[split:])
    return True
    
    
print isIn("A", "DOANE")