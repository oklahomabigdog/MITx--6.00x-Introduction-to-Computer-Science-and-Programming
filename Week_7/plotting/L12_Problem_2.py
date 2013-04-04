def lotsOfParameters1(a,b,c,d,e):
    print a
    print b
    print c
    print d
    print e

# ===============
# = Question 1A =
# ===============
# 1. lotsOfParameters1()                        # => Error
# 2. lotsOfParameters1(1, 2)                    # => Error
# 3. lotsOfParameters1(1,e=5,d=4,c=3,b=2)       # => No Error
# 4. lotsOfParameters1(e=5,a=1,d=4,b=2,c=3)     # => No Error
# 5. lotsOfParameters1(a=5,b=1,c=4,d=2,3)       # => Error

# ===============
# = Question 1B =
# ===============
# 1. lotsOfParameters1()                        # => Error
# 2. lotsOfParameters1(1, 2)                    # => Error
# 3. lotsOfParameters1(1,e=5,d=4,c=3,b=2)       # => Produces Same Output
# 4. lotsOfParameters1(e=5,d=4,c=3,b=2,1)       # => Error
# 5. lotsOfParameters1(e=5,a=1,d=4,b=2,c=3)     # => Produces Same Output

def lotsOfParameters2(a=1,b=2,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e

# ===============
# = Question 2A =
# ===============
# 1. lotsOfParameters2()                        # => No Error
# 2. lotsOfParameters2(1, 2)                    # => No Error
# 3. lotsOfParameters2(1, c=2)                  # => No Error
# 4. lotsOfParameters2(1, c=2, 3)               # => Error
# 5. lotsOfParameters2(1, e=20, b=3)            # => No Error
# 6. lotsOfParameters2(1, e=20, b=3, a=10)      # => Error

# ===============
# = Question 2B =
# ===============
# 1. lotsOfParameters2()                        # => Produces Same Output
# 2. lotsOfParameters2(1,2,3,4)                 # => Produces Same Output
# 3. lotsOfParameters2(5,4,3,2,1)               # => Produces Different Output

def lotsOfParameters3(a,b,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e

# ===============
# = Question 3A =
# ===============
# 1. lotsOfParameters3()                        # => Error
# 2. lotsOfParameters3(1, 2)                    # => No Error
# 3. lotsOfParameters3(1, c=2)                  # => Error
# 4. lotsOfParameters3(1, c=2, 3)               # => Error
# 5. lotsOfParameters3(1, c=2, b=3)             # => No Error

# ===============
# = Question 3B =
# ===============
# 1. lotsOfParameters3()                        # => Error
# 2. lotsOfParameters3(1,2)                     # => Produces Same Output
# 3. lotsOfParameters3(1,e=5,d=4,c=3,b=2)       # => Produces Same Output
# 4. lotsOfParameters3(e=5,d=4,c=3,b=2,1)       # => Error
# 5. lotsOfParameters3(e=5,a=1,d=4,b=2,c=3)     # => Produces Same Output