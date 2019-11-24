# AL BIRR KARIM SUSANTO
# albirkarim1@gmail.com
# https://github.com/albirrkarim/
# http://prajanto.blog.dinus.ac.id/courses/modeling-and-simulation/

# --------------------- Exactly Value Method ------------------

import math 
import time
start_time = time.time()

# Input & Initialize

# Euler number
e=math.e

firstPopulation=100
growthRate=0.1
endTime=10

# Process

populationT= firstPopulation * pow(e,growthRate*endTime)


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
print(populationT)