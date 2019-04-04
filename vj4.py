#TODO
#implement
import numpy as np
import random
from Values import *
import math

costLimit = 8000
#if set to true it will use the predefined cost limit (which might be higher than first solution cost)
#otherwise it will generate solution that has a better cost then the first random solution
useCostLimit = False
#generate a random solution
sol = np.random.randint(2, size=20)
print(sol)
#calculate fitness
#Fitness = [cost][Satisfaction]
Fitness = calculateCost(sol, True)

k = 0
m = 0.5
tk = m*20**2

Mk = 2000

if not useCostLimit:
    costLimit = Fitness[0]
else:
    print("Cost Limit fixed and set to: ", costLimit)
while tk>0:
    for m in range(Mk):
        
        randPos=np.random.randint(20)
        newSol = list(sol)
        if newSol[randPos] == 0: 
            newSol[randPos] = 1
        else:
            newSol[randPos] = 0
        
        newSolutionFitness = calculateCost(newSol)
        delta = Fitness[1] - newSolutionFitness[1]
        #cost prohibitive?

        if newSolutionFitness[0]>costLimit:
            continue
        if delta < 0:
            #print(newSolutionFitness[1],">",Fitness[1])
            #print(newSol)
            sol = list(newSol)
            Fitness = newSolutionFitness
        else:
            probability = math.exp(delta/tk)
            #print(probability)
            
            if np.random.uniform(0,1,1) < (1-probability):
                sol = list(newSol)
                Fitness = newSolutionFitness
            
        tk-=0.9

print("\n\nBest solution found:")
print(sol)
calculateCost(sol, True)
