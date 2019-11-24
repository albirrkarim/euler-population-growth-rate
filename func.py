import numpy as np

def rungeKutta2():
    firstPopulation = 100
    growthRate      = 0.1
    deltaT          = 0.5

    def GrowthFunc(b):
        return growthRate*b

    population      = firstPopulation
    results=[]
    deltaP=0.0

    # Process

    for t in np.arange(0, 10, deltaT):
        population  += (deltaP*deltaT)

        # a = F(tn,pn)
        # b = yn+1
        # c = F(tn,yn+1)

        a       =  GrowthFunc(population)
        b       =  population+(a*deltaT)
        c       =  GrowthFunc(b)
        deltaP  =  (a+c)/2

        results.append((t,population,a,b,c,deltaP))

    return results

def euler(firstPopulation,growthRate,MaximumPopulation):

    # Input & Initialize
    firstPopulation = 100.0
    growthRate      = 0.1
    M               = 500.0
    deltaT          = 0.5

    def GrowthFunc(b):
        return growthRate*b

    population      = firstPopulation

    results=[]

    deltaP=0.0

    # Process
    for t in np.arange(0, 10, deltaT):
        population=population+(deltaP*deltaT)

        growth=GrowthFunc(population)

        death=growth*(population/M)

        deltaP=growth-death

        results.append((t,population,growth,death,deltaP))

    return results

def exact():

    # Input & Initialize

    # Euler number
    import math
    e=math.e

    firstPopulation=100
    growthRate=0.1
    endTime=10

    # Process

    populationT= firstPopulation * pow(e,growthRate*endTime)

    return populationT


