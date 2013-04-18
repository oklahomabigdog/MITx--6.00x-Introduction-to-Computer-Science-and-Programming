class ResistantVirus(SimpleVirus):

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):

        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        return self.resistances

    def getMutProb(self):
        return self.mutProb

    def isResistantTo(self, drug):
        if drug in self.getResistances():
            return self.resistances[drug]
        else:
            return False
       
    def reproduce(self, popDensity, activeDrugs):
        for a in activeDrugs:
            if not self.isResistantTo(a):
                raise NoChildException
        if random.random()<self.getMaxBirthProb()*(1 - popDensity): 
            new_resist = self.getResistances()
            for b in self.getResistances():
                if random.random()< self.getMutProb():
                    if new_resist[b] == True:
                        new_resist[b] = False
                    else:
                        new_resist[b] = True
            return ResistantVirus(self.getMaxBirthProb(),self.getClearProb(),new_resist,self.getMutProb())   
        else:
            raise NoChildException       
            
class TreatedPatient(Patient):

    def __init__(self, viruses, maxPop):
        Patient.__init__(self, viruses, maxPop)
        self.prescription = list()


    def addPrescription(self, newDrug):
        if newDrug not in self.prescription:
            self.prescription.append(newDrug)


    def getPrescriptions(self):
        return self.prescription


    def getResistPop(self, drugResist):
        count =0
        for a in self.getViruses():
            flag =1
            for b in drugResist:
                if not a.isResistantTo(b):
                    flag =0
                    break
            if flag ==1:
                count+=1
        return count
    
    def update(self):

        rem_virus = self.getViruses()
        for v in rem_virus:
            if v.doesClear():
                self.viruses.remove(v)
        popDensity = float(self.getTotalPop())/self.getMaxPop()
        new_virus =[]
        for v in self.getViruses():
            try:
                new_virus.append(v.reproduce(popDensity,self.getPrescriptions()))
            except NoChildException:
                pass
        self.viruses = self.viruses +new_virus
        return self.getTotalPop()