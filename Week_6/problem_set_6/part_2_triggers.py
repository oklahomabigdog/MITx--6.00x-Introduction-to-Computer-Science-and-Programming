class Trigger(object):
    def evaluate(self, story):
        raise NotImplementedError

class WordTrigger(Trigger):
    def __init__(self,word):
        self.word = word.lower()

    def changeChars(self,text):
        final = ""
        for c in text:
            if c in string.punctuation:
                final += " "
            else:
                final += c
        return final

    def isWordIn(self,text):
        comp = self.changeChars(text)
        list = comp.lower().split(" ")
        return self.word in list

class TitleTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getTitle())

class SubjectTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getSummary())