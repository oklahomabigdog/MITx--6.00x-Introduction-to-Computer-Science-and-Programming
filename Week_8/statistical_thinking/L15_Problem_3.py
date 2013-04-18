def stdDevOfLengths(L):
    if not len(L):
        return float('NaN')
    else:
        mean = sum((len(i) for i in L)) / float(len(L))
        variance = sum((len(i) - mean)**2 for i in L) / float(len(L))
        std_dev = variance **0.5
        return std_dev