# ===============
# = Code To Run =
# ===============
import pylab

WORDLIST_FILENAME = "words.txt"
VOWELS = 'aeiou'

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    vowelsList = []
    for word in wordList:
        numVowels = 0
        for letter in word.lower():
            if letter in VOWELS:
                numVowels = numVowels + 1
        vowelsList.append(numVowels/float(len(word)))
    pylab.figure()
    pylab.title("Vowel Proportion Histogram")
    # pylab.xlabel('Final Score')
    pylab.ylabel('Number of Vowels')


    pylab.hist(vowelsList, numBins)
    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)


# ======================
# = Answer To Question =
# ======================
# 1. Using the code you wrote to investigate, do more words in the word list have a vowel proportion greater than or less than 0.5?
#     Answer: More words have a vowel proportion less than 0.5