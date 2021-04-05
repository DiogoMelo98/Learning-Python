# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 22:01:20 2021

@author: diogo
"""

# List basics (cont.)
import random 
import math

'''
numList = []
for i in range(5):
    numList.append(random.randrange(1,9))
    
# numList.sort()

# numList.reverse()

# Inserir no índice a o elemento b : (a, b)    
numList.insert(5, 10)
numList.insert(2, 22)
# Remover o elemento 10
numList.remove(10)
#Remover o elemento que existe no índice 2
numList.pop(2)

for k in numList:
    print(k, end=", ")
print()
'''

# LIST COMPREHENSIONS
# Ex.1 #############
evenList = [i*2 for i in range(10)]

for i in evenList:
    print(i)
print()

# Ex.2 ############
numList = [1,2,3,4,5]
listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                for m in numList]

for i in listOfValues:
    print(i)
print()

# Ex.3 ############
multiDList = [[0]*10 for i in range(10)]
multiDList[0][1] = 10
print(multiDList[0][1])
print()

# Ex.4 ############
listTable = [[0]*4 for i in range(4)]
for i in range(4):
    for j in range(4):
        listTable[i][j] = "{} : {}".format(i, j)
for i in range(4):
    for j in range(4):
        print(listTable[i][j], end=" || ")
    print()