L = [1, 2, 3, 4, 5, 6, 7]


def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False



print search(L, 9)
print search(L, 9)