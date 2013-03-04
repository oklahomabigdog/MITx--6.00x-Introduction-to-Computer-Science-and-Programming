import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    counter = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            counter += 1
    return counter == len(secretWord)

def getGuessedWord(secretWord, lettersGuessed):
    stringSoFar = ""
    for i in range(0, len(secretWord)):
        if secretWord[i] in lettersGuessed:
            stringSoFar += secretWord[i]
        else:
            stringSoFar += "_ "
    return stringSoFar

def getAvailableLetters(lettersGuessed):
    lettersGuessedString = "".join(lettersGuessed)
    remaining = "".join(c for c in string.ascii_lowercase if c not in
        lettersGuessedString)
    return remaining

def hangman(secretWord):
    guessCounter = 8
    lettersGuessed = []
    print "Welcome to the game Hangman!"
    print "I am thinknig of a word that is " + str(len(secretWord)
        ) +" letters long."
    while True:
        print "-------------"
        print "You have " + str(guessCounter) + " guesses left."
        print "Available letters: " + getAvailableLetters(lettersGuessed)
        guess = raw_input("Please guess a letter: ").lower()
        if guess not in lettersGuessed and guess in secretWord:
            lettersGuessed.append(guess)
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
        elif guess not in lettersGuessed and guess not in secretWord:
            lettersGuessed.append(guess)
            print "Oops! That letter is not in my word: " + getGuessedWord(
                secretWord, lettersGuessed)
            guessCounter -= 1
        else:
            print "Oops! You've already guessed that letter: " + getGuessedWord(
                secretWord, lettersGuessed)

        if guessCounter == 0 or isWordGuessed(secretWord, lettersGuessed
            ) == True:
            print "-------------"
            break
        
    if (isWordGuessed(secretWord, lettersGuessed)):
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses.  The word was " + secretWord 

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)