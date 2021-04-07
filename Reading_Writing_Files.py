# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:30:21 2021

@author: diogo
"""

import os

with open("myData.txt", mode='w', encoding='utf-8') as myFile:
    myFile.write('Some random text\nMore random text\nAnd some more')

with open('myData.txt', encoding='utf-8') as myFile:
    print(myFile.read())

print(myFile.closed)

print(myFile.name)

print(myFile.mode)

os.rename('myData.txt', 'myData2.txt')

os.remove('myData2.txt')

#os.mkdir('myDir')

os.chdir('myDir')

print('Current directory :', os.getcwd())

os.chdir('..')

print('Current directory :', os.getcwd())

os.rmdir('myDir')