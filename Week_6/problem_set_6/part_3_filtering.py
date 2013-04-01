def filterStories(stories, triggerlist):
    res = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                res.append(story)
                break
    return res

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word

    def is_word_in(self, text):
        word = self.word.lower()
        text = text.lower()
 
        for punc in string.punctuation:
            text = text.replace(punc, " ")
        splittext = text.split(" ")
 
        return word in splittext
 
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.is_word_in(story.getTitle())

class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.is_word_in(story.getSubject())

class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.is_word_in(story.getSummary())

class PhraseTrigger(Trigger):
    def __init__(self, pharse):
        self.p=pharse
    def evaluate (self, story):
        return self.p in story.getTitle() or self.p in story.getSummary() or self.p in story.getSubject()