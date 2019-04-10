import numpy as np
from Values import *
import math

#maximum allowed cost(budget) 
#used if useCostLimit = True
costLimit = 8000
#if set to true it will use the predefined cost limit (which might be higher than first solution cost)
#otherwise it will generate solution that has a better cost then the first random solution - algorithm tends to not find a better solution in this case
useCostLimit = True
breakValue = 0
#coolingStrategy = "linear" or "geometric" or anything for basic
coolingStrategy = "linear"
if coolingStrategy == "geometric":
    breakValue = 0.03#smallest possible without dumping a mathOverflow when using exp

#generate a random solution
sol = np.random.randint(2, size=20)
print(sol)
#calculate fitness
#Fitness = [cost][Satisfaction]
Fitness = calculateCost(sol, True)

k = 1
m = 0.5
tk = m*20**2
t0 = tk
Mk = 2000

if not useCostLimit:
    costLimit = Fitness[0]
else:
    print("maximum cost(budget) fixed and set to: ", costLimit)
while tk>breakValue:
    k+=1
    print("tk=",tk,"in iteration:",k)
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
            
    if coolingStrategy == "linear":
        #pass
        #beta = (t0 - tk)/(k-1)
        beta = 0.8
        tk = t0 - beta*k
    elif coolingStrategy == "geometric":
        pass
        #alpha = (tk/t0)**(1/(k-1))
        alpha = 0.5
        tk = alpha**k * t0
    else:
        tk-=0.9
    
    if tk <= 0:
        break;
        

print("\n\nBest solution found:")
print(sol)
calculateCost(sol, True)