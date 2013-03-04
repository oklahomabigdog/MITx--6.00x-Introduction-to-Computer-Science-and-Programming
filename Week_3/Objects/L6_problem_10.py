animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def howMany(aDict):
    number = 0
    for i in aDict:
        number += len(aDict[i])
    return number

print howMany(animals)