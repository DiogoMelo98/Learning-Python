# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

rand_string = "   this is a string   "

print(rand_string)

rand_string = rand_string.strip()

rand_string = rand_string.capitalize()

rand_string = rand_string.upper()

rand_string = rand_string.lower()

print(rand_string.strip())
print(rand_string.capitalize())
print(rand_string.upper())
print(rand_string.lower())

#Creating a list
a_list = ("Bunch", "of", "random", "words")
print(" ".join(a_list))

#Convert a string into a list
a_list_2 = rand_string.split()
for i in a_list_2:
    print(i)
    
#How many times a string appears on a string
print("How many is :", rand_string.count("is"))

#Index where a string starts
print("Where is string :", rand_string.find("string"))

#Replace a string
print(rand_string.replace("a", "a kind of"))