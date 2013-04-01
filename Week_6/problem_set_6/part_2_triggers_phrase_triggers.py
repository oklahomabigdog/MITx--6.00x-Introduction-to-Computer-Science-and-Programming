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

class PhraseTrigger(Trigger):
    def __init__(self,phrase):
        self.phrase = phrase

    def evaluate(self,story):
        return self.phrase in story.getTitle() or self.phrase in story.getSubject() or self.phrase in story.getSummary()

class NotTrigger(Trigger):
    def __init__(self,trigger):
        self.trigger = trigger

    def evaluate(self,story):
        return not self.trigger.evaluate(story)

class AndTrigger(Trigger):
    def __init__(self,trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self,story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

class OrTrigger(Trigger):
    def __init__(self,trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self,story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)

