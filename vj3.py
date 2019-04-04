import numpy as np
from Values import *

LOOPS = 20000
costLimit = 10000
#if set to true it will use the predefined cost limit (which might be higher than first solution cost)
#otherwise it will generate solution that has a better cost then the first random solution
useCostLimit = False

print("Upper Cost Limit for Solution is set to", costLimit)
#generate a random solution
sol = np.random.randint(2, size=20)
print(sol)
#calculate fitness
#Fitness = [cost][Satisfaction]
Fitness = calculateCost(sol, True)

if not useCostLimit:
    costLimit = Fitness[0]
else:
    print("Cost Limit fixed and set to: ", costLimit)
#loop
for i in range(LOOPS):
    #generate neighboor solution
    randPos = np.random.randint(20)
    newSol = list(sol)
    if newSol[randPos] == 0: 
        newSol[randPos] = 1
    else:
        newSol[randPos] = 0
    #with a small chance
    if(np.random.randint(100) == 0):
        #mutate
        randPos = np.random.randint(20)
        if newSol[randPos] == 0:
            newSol[randPos] = 1
        else:
            newSol[randPos] = 0
    #caluclate fitness
    newSolutionFitness = calculateCost(newSol)
    
    #check if cost prohibitive
    if newSolutionFitness[0]>costLimit:
        continue
    
    #if neighboor better than old solution
    if newSolutionFitness[1]>Fitness[1]:
        #solution becomes the neighbor
        #print(newSolutionFitness[1],">",Fitness[1])
        sol = list(newSol)
        Fitness = calculateCost(sol)
        #print("New Fitness set: ", Fitness, "for solution", sol)
    #print(sol)

print("\n\nBest Solution, after",LOOPS, "loops")
print(sol)
calculateCost(sol, True)
