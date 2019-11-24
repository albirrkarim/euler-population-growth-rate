from tabulate import tabulate
import numpy as np
# AL BIRR KARIM SUSANTO
# albirkarim1@gmail.com
# https://github.com/albirrkarim/

# http://prajanto.blog.dinus.ac.id/courses/modeling-and-simulation/

# Description
# Growth Function

    # dP / dt = P * r

# Death Function

    # dD / dt = (r * P / M) *P

# M = region capacity

# Delta P = Growth  - Death

# Delta t = 0.5

# Input & Initialize
firstPopulation = 100.0
growthRate      = 0.1
M               = 500.0
deltaT          = 0.5

population      = firstPopulation

results=[]

deltaP=0.0
# Process
for t in np.arange(0, 5.5, 0.5):
    population=population+(deltaP*deltaT)

    growth=growthRate*population

    death=growth*(population/M)

    deltaP=growth-death

    results.append((t,population,growth,death,deltaP))

# Output
print(tabulate(results,headers=["t","P(t)","r*P","r*P/M*P","deltaP"],tablefmt="fancy_grid"))
