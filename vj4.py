#TODO
#implement
import numpy as np
import random

def calculateFitness(sol):
    #ToDO toss in the fitness function
    np.multiply
    pass
    
#generiraj stanje

k = 0
m = 0.5
tk = m*20**2

#slucajno rjesenje
sol = np.random.randint(2,size=20)
print(sol)

Mk = 20

while tk>0:
    for m in range(Mk):
        #TODO placeholder, ubaciti generiranje susjednog od doma
        randPos=np.random.randint(20)
        newSol = sol
        if sol[randPos] == 0: 
            newSol[randPos] = 1
        else:
            newSol[randPos] = 0
        #TODO calculateFitness iz vj3.py 
        delta = calculateFitness(sol) - calculateFitness(newSol)
        if delta < 0:
            sol = newSol
        else:
            probability = np.exp(-delta/tk)
            if random.random() < probability:
                sol = newSol
        tk-=0.9
        