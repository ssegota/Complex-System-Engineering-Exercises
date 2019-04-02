# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import itertools
import matplotlib.pyplot as plt





#Zadane vrijednosti
cijena = [4,3,2,1]
vrijednosti = np.array([[4,7,3,5],[2,2,2,3],[3,1,4,7]])

#Varijable
#Suma zadovoljstava po zadatku
totalValues=vrijednosti[0]+vrijednosti[1]+vrijednosti[2]
comboCost = []
comboCostSatisfaction = []
#Plot axes
satisfaction=[]
cost=[]
#Izrada kombinacija
for L in range(0, len(cijena)+1):
    for subset in itertools.combinations(cijena, L):
        #Pohrani cijenu kombinacije i kombinaciju u listu
        comboCost.append((np.sum(subset), list(subset)))
    
for i in range(1, len(comboCost)):
    #Suma zadovoljstava po zadatku
    currentTotal = vrijednosti[0]+vrijednosti[1]+vrijednosti[2]
    #Uzmi presjek kako bi se vidjelo koji zadaci nisu ispunjeni u kombinaciji

    A = set(comboCost[i][1]) ^ set(cijena)
    #Makni one zadatke koji nisu u trenutnoj kombinaciji
    for k in A:
        currentTotal[k-1]=0

    #Zbroji zadovoljstvo po zadacima u jedinstvenu vrijednost
    currentSatisfaction=np.sum(currentTotal)
    #Pohrani zadovoljstvo, cijenu i pripadnu kombinaciju u listu L
    comboCostSatisfaction.append((currentSatisfaction, comboCost[i][0], comboCost[i][1]))   

#sortiraj sa prvim največim
comboCostSatisfaction.sort()
comboCostSatisfaction.reverse()

print("One Objective problem")
#ispiši samo one kojima je vrijednost cijene manja od 6
for l in comboCostSatisfaction:
    if l[1]<=6:
       print(l)

#Pohrani vrijednosti cijene i zadovoljstva u varijable za osi    
for l in comboCostSatisfaction:
    satisfaction.append(l[0])
    cost.append(l[1])


#MO
#Traži li se fronta sa gornje ili doljnje strane
maxY=False
correct_pareto_front=[]
sorted_list = sorted([[cost[i], satisfaction[i]] for i in range(len(cost))], reverse=maxY)
pareto_front = [sorted_list[0]]
for pair in sorted_list[1:]:
    if maxY:
        if pair[1] <= pareto_front[-1][1]:
            pareto_front.append(pair)
    else:
        if pair[1] >= pareto_front[-1][1]:
            pareto_front.append(pair)

correct_pareto_front.append(pareto_front[0])
for c in range(1,len(pareto_front)):
    if c==len(pareto_front)-1:
        correct_pareto_front.append(pareto_front[c])
        break;
    if maxY and not (pareto_front[c][1]>pareto_front[c+1][1] and pareto_front[c][0]==pareto_front[c+1][0]) and not(pareto_front[c][1]==pareto_front[c-1][1] and pareto_front[c][0]<pareto_front[c-1][0]):
        correct_pareto_front.append(pareto_front[c])
    if not maxY and not (pareto_front[c][1]<pareto_front[c+1][1] and pareto_front[c][0]==pareto_front[c+1][0]) and not(pareto_front[c][1]==pareto_front[c-1][1] and pareto_front[c][0]>pareto_front[c-1][0]):
        correct_pareto_front.append(pareto_front[c])

plt.scatter(cost,satisfaction)
pf_X = [pair[0] for pair in correct_pareto_front]
pf_Y = [pair[1] for pair in correct_pareto_front]
plt.scatter(pf_X, pf_Y, marker='x')
plt.xlabel("Objective 1")
plt.ylabel("Objective 2")
print(correct_pareto_front)
plt.gca().invert_yaxis()
plt.show()
