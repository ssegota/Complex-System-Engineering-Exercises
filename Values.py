# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:22:38 2019

@author: Sandi Šegota
"""

import numpy as np

Cost = np.array([ 394.6573,  701.3776,  519.6367,  430.7028,  254.6620,  548.8158,  434.4954,  393.7929,  743.5340,  531.2210 , 383.2510,  783.5422,  526.4680,  228.6492,  541.3931,  459.5770,  598.0073,  512.9623,  496.3435,  989.9871])

Value = np.array([[4, 4, 5, 4, 5],
                  [2, 4, 3, 5, 4],
                  [1, 2, 3, 2, 2],
                  [2, 2, 3, 3, 4],
                  [5, 4, 4, 3, 5],
                  [5, 5, 5, 4, 4],
                  [2, 1, 2, 2, 2],
                  [4, 4, 4, 4, 4],
                  [4, 4, 4, 2, 5],
                  [4, 5, 4, 3, 2],
                  [2, 2, 2, 5, 4],
                  [3, 3, 4, 2, 5],
                  [4, 2, 1, 3, 3],
                  [2, 4, 5, 2, 4],
                  [4, 4, 4, 4, 4],
                  [4, 2, 1, 3, 1],
                  [4, 3, 2, 5, 1],
                  [1, 2, 3, 4, 2],
                  [3, 3, 3, 3, 4],
                  [2, 1, 2, 2, 1]])


def calculateCost(completedTasks, printValues=False):
    ValueReshaped = np.reshape(Value, [5,20])
    CostReshaped = np.reshape(Cost, [1,20])
    ret = []
    costForSeed = np.sum(np.multiply(completedTasks, CostReshaped))
    for i in range(len(ValueReshaped)):
        #calculate Satisfaction for a given seed
        satisfactionForSeed = np.sum(np.multiply(completedTasks, ValueReshaped[i]))
        ret.append([costForSeed, satisfactionForSeed])
    
    satisfactionSum=0
    for i in range(len(ret)):
        satisfactionSum+=ret[i][1]

    if printValues:
        print("Satisfaction for seed = ", satisfactionSum)
        print("Cost for seed = ", ret[0][0])
    
    retVal = [costForSeed, satisfactionSum]
    return retVal
