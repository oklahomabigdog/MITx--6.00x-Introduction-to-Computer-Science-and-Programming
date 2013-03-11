def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

# ==============
# = Question 1 =
# ==============
# linearSearch([20, 10, 1, 7, 4, 22, 25, 12, 31], 20)   # Best Case Senerio

# ==============
# = Question 2 =
# ==============
# linearSearch([13, 9, 22, 3, 10, 17, 11, 2, 12], 26) # Worst Case Senerio

# ==============
# = Question 3 =
# ==============
# linearSearch([9, 3, 12, 24, 7, 8, 23, 11, 19], 8) # Average Case Senerio

# ==============
# = Question 4 =
# ==============
