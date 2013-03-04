low = 0
high = 100
ans = ' '
print "Please think of a number between 0 and 100!"
print "Is your secret number " + str((low + high)/2) + "?"
ans = raw_input('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. Enter ''c'' to indicate I guessed correctly.')

while ans != 'c':
    if ans == 'h' or ans == 'l':
        slicing = (low + high)/2
        if ans == "h":
            high = slicing
        elif ans == "l":
            low = slicing
        slicing = (low + high)/2
        print "Is your secret number " + str(slicing) + "?"
        ans = raw_input('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. Enter ''c'' to indicate I guessed correctly.')
    else:
        print "Sorry, I did not understand your input."
        print "Is your secret number " + str((low + high)/2) + "?"
        ans = raw_input('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. Enter ''c'' to indicate I guessed correctly.')

print "Game over. Your secret number was: " + str(slicing)
