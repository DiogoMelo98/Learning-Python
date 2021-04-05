# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 22:53:33 2021

@author: diogo
"""

multTable = [[0] * 10 for i in range(10)]

for i in range(1, 10):
    for j in range(1, 10):
        multTable[i][j] = i * j
        
for i in range(1, 10):
    for j in range(1, 10):
        print(multTable[i][j], end=", ")
    print()