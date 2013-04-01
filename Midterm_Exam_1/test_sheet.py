def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story. 
    """

    array = story.split(" ")
    
    for w in array:
        if w in listOfAdjs:
            story = story.replace(w, "[ADJ]")
        if w in listOfNouns:
            story = story.replace(w, "[NOUN]")
        if w in listOfVerbs:
            story = story.replace(w, "[VERB]")
    return story

            
# story = 'The ravenous zombies started attacking yesterday'
# listOfAdjs = ['ravenous']
# listOfNouns = ['zombies', 'humans', 'yesterday']
# listOfVerbs = ['attacking', 'attacks']
# print generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)


story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
listOfAdjs = ['creepy', 'plaid']
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = ['found', 'looked']
print generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)







