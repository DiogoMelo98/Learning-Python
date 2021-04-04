# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 18:05:02 2021

@author: diogo
"""

#Random Acess Memory: RAM

#Ask for a string
orig_string = input("Convert to Acronym: ")
#Convert the string to uppercase
orig_string = orig_string.upper()
#Convert the string into a list
list_of_words = orig_string.split()
#Cycle through the list
for word in list_of_words:
#Get the 1st letter of the word and eliminate the newline
    print(word[0], end="")
#Add a newline
print()