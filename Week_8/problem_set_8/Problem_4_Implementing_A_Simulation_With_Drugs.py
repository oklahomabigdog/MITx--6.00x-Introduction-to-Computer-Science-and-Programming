class ResistantVirus(SimpleVirus):
 
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.r=resistances
        self.mutProb=mutProb
 
 
    def isResistantTo(self, drug):
        if drug in self.r:
            return self.r[drug]
        else:
            return False
 
    def reproduce(self, popDensity, activeDrugs):
        for i in activeDrugs:
            if not self.isResistantTo(i):
                raise NoChildException()
        prob=random.random()
        if prob < self.maxBirthProb*(1-popDensity):
            childResistances={}
            for j in self.r.keys():
                resistanceProb=random.random()
                if resistanceProb < self.mutProb:
                    childResistances[j]=not self.r[j]
                else:
                    childResistances[j]=self.r[j]
            return ResistantVirus(self.maxBirthProb, self.clearProb, childResistances, self.mutProb)
        else:
            raise NoChildException()