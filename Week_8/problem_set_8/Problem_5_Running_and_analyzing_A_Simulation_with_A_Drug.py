def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials):
    def runTrialDrug(elapsedTimeSteps, numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, tempResistPopList):
        viruses = [];
        for i in range(numViruses):
            virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb);
            viruses.append(virus);

        patient = TreatedPatient(viruses, maxPop);

        virusLevelsThisTrial = [];
        ResistPopListThisTrial = [];
        ResistPopListThisTrial.append(patient.getResistPop(patient.getPrescriptions()));
        virusLevelsThisTrial.append(patient.getTotalPop());

        for i in range(elapsedTimeSteps):
            if i == 150:
                patient.addPrescription('guttagonol');

            virusLevelsThisTrial.append(patient.update());
            ResistPopListThisTrial.append(patient.getResistPop(['guttagonol']));

        for i in range(len(ResistPopListThisTrial)):
            tempResistPopList.append(ResistPopListThisTrial[i]);

        return virusLevelsThisTrial;
    accumulatedVirusLevels = [];
    virusLevelResults = [];
    resistPopList = [];

    for trial in range(numTrials):
        tempResistPopList = [];
        virusLevelResults = runTrialDrug(300, numViruses, maxPop, maxBirthProb, clearProb, resistances.copy(), mutProb, tempResistPopList);

        if trial == 0:
            accumulatedVirusLevels = virusLevelResults;
            resistPopList = tempResistPopList[:];

        else:
            for i in range(len(virusLevelResults)):
                accumulatedVirusLevels[i] += virusLevelResults[i];

            for i in range(len(tempResistPopList)):
                resistPopList[i] += tempResistPopList[i];

    accumulatedVirusLevels.remove(accumulatedVirusLevels[0]);
    resistPopList.remove(resistPopList[0]);

    for i in range(len(accumulatedVirusLevels)):
        accumulatedVirusLevels[i] /= float(numTrials);

    for i in range(len(resistPopList)):
        resistPopList[i] /= float(numTrials);

    pylab.plot(range(0, len(accumulatedVirusLevels)), accumulatedVirusLevels, label = "Total")
    pylab.plot(range(0, len(resistPopList)), resistPopList,
               label = "ResistantVirus")
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("time step")
    pylab.ylabel("# viruses")
    pylab.legend(loc = "best")
    pylab.show()