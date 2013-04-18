# ========
# = Code =
# ========
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    avg_pop=[]
    for i in range(0, 300):
        avg_pop.append(0.0)
    for i in range(numTrials):
        viruses =[]
        for j in range(numViruses):
            virus=SimpleVirus(maxBirthProb, clearProb)
            viruses.append(virus)
        Patient_obj = Patient(viruses, maxPop)
        for time in range(300):
            avg_pop[time]+=Patient_obj.update()
    for i in range(0, 300):
        avg_pop[i]/=numTrials
    pylab.plot(range(0, 300), avg_pop)
    pylab.title("SimpleVirus Simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend()
    pylab.figure()
    pylab.show()

# ============
# = Question =
# ============
About 150 time-steps