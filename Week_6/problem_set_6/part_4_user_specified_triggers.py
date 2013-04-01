def makeTrigger(triggerMap, triggerType, params, name):
    if triggerType == "TITLE":
        triggerMap[name] = TitleTrigger(params[0])
    elif triggerType == "SUBJECT":
        triggerMap[name] = SubjectTrigger(params[0])
    elif triggerType == "SUMMARY":
        triggerMap[name] = SummaryTrigger(params[0])
    elif triggerType == "NOT":
        triggerMap[name] = NotTrigger(triggerMap[params[0]])
    elif triggerType == "AND":
        triggerMap[name] = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
    elif triggerType == "OR":
        triggerMap[name] = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
    elif triggerType == "PHRASE":
        triggerMap[name] = PhraseTrigger(' '.join(params))
    return triggerMap[name]
 
def readTriggerConfig(filename):
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)
    triggers = []
    triggerMap = {}

    for line in lines:
        linesplit = line.split(" ")
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])
 
    return triggers
   
import thread

SLEEPTIME = 60 #seconds -- how often we poll

def main_thread(master):
    try:
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        triggerlist = readTriggerConfig("triggers.txt")
 
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
 
        t = "Dan's Google & Yahoo Top News Rss-er"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())
 
        while True:
 
            print "Polling . . .",
            stories = process("http://news.google.com/?output=rss")
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))
            stories = filterStories(stories, triggerlist)
            map(get_cont, stories)
            scrollbar.config(command=cont.yview)
 
            print "Sleeping..."
            time.sleep(SLEEPTIME)
 
    except Exception as e:
        print e