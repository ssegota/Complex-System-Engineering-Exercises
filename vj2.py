from Values import *
import numpy as np
import itertools
import matplotlib.pyplot as plt
from operator import itemgetter

def getCombosForNumberOfTasks(sizeOfTaskArray, numberOfCompletedTasks, printFull=True):
    if printFull:
        
        print(type(int(numberOfCompletedTasks)))
    which = np.array(list(itertools.combinations(
        range(sizeOfTaskArray), numberOfCompletedTasks)))
    grid = np.zeros((len(which), sizeOfTaskArray), dtype="int8")

    # Magic
    grid[np.arange(len(which))[None].T, which] = 1

    return grid

plotStuff = False

np.set_printoptions(threshold=np.inf)


allVals = []
for i in range(1,21):
    print("TOTAL:", i/20*100, "%")
    tasks_per_i = getCombosForNumberOfTasks(len(Cost), i, False)
    for n in tasks_per_i:
        allVals.append(calculateCost(n))

costs = []
satisfaction = []

for i in allVals:
    for j in range(5):        
        costs.append(i[j][0])
        satisfaction.append(i[j][1])

#singleObjective
costLimit = 500.0

filteredValues=[]
print("SATISFACTION\tCOST")
for i in range(len(costs)):
    if costs[i]<costLimit:
        filteredValues.append([costs[i], satisfaction[i]])



filteredValues.sort(key=itemgetter(1))
filteredValues.reverse()
for i in range(len(filteredValues)):
    print(str(filteredValues[i][1])+"\t\t"+str(filteredValues[i][0]))
#Multi Objective
if plotStuff:      
    plt.scatter(costs, satisfaction)
    plt.show()
