# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 21:48:56 2021

@author: diogo
"""

import os

with open('dados.txt', mode='w', encoding='utf-8') as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more")

with open('dados.txt', encoding='utf-8') as myFile:
    lineNum = 1
    while True:
        line = myFile.readline()
        if not line:
            break
        print('Line', lineNum, " : ", line, end="")
        lineNum += 1

#----------PROBLEM: ANALYZE THE FILE---------
with open('dados.txt', encoding='utf-8') as myFile:
    lineNum=1
    while True:
        line = myFile.readline()
        if not line:
            break
        print('Line', lineNum)
        wordList = line.split()
        print('Number of Words :', len(wordList))
        charCount = 1
        for word in wordList:
            for char in word:
                charCount += 1
        avgNumChars = charCount/len(wordList)
        print('Average Word Length : {:.2}'.format(avgNumChars))
        lineNum += 1