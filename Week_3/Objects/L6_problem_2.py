def oddTuples(aTup):
    odd = ()
    for r in range(len(aTup)):
        if r % 2 == 0:
            odd += (aTup[r],)
    return odd




aTup = ('I', 'am', 'a', 'test', 'tuple')
print oddTuples(aTup)