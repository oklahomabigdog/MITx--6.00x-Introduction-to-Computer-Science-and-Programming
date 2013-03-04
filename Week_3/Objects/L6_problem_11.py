animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    if aDict == {}:
        return None
    else:
        biggest = "a"
        for i in aDict:
            print aDict[biggest] > aDict["a"]


            # if aDict[i] < aDict[biggest]:
            #     print aDict[biggest]
            #     biggest = i
            # else:
            #     continue


    # elif type(aDict.values()[0][0]) == str:
    #     return max(aDict.keys(), key=str)
    # else:
    #     # print type(aDict.values()[0][0])
    # 
    # 
    #     return max(aDict.keys(), key=int)



# print biggest(animals)    
# print biggest({})

print biggest({'a': [10, 9, 4, 11, 18, 4, 19, 14], 'c': [1, 15, 1, 20, 16, 15, 4], 'b': [12, 20, 3], 'e': [3, 5], 'd': [2, 10, 12, 15, 3, 20, 4, 3, 19, 9]})