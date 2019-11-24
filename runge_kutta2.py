# AL BIRR KARIM SUSANTO
# albirkarim1@gmail.com
# https://github.com/albirrkarim/
# http://prajanto.blog.dinus.ac.id/courses/modeling-and-simulation/

# ------------------------ Runge Kutta 2 ------------------------


from tabulate import tabulate
import numpy as np
import time
start_time = time.time()

# Input & Initialize

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


# Measure Time & Heap Memory
print("__________Measurement__________\n")
# Time
print("______Time______\n\n")
end_time = time.time()
delta_time = end_time-start_time
print("Execution Time : ",delta_time," ms\n")

# Memory
print("_____Memory_____\n")
from guppy import hpy
h = hpy()
print (h.heap())

# Output
print(tabulate(results,headers=["tn","Pn","F(tn,pn)","yn+1","F(tn,yn+1)","deltaP"],tablefmt="fancy_grid"))
