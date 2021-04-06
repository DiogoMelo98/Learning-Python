# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:11:27 2021

@author: diogo
"""

# Dictionaries
# While lists organize data based on sequential indexes
# Dictionaries instead use key/value pairs

# A key/value pair could be
# fName : "Derek" where fName is the key and "Derek" is the value

# Create a dictionary about Derek
derekDict = {"fName" : "Derek", "lName" : "Banas", "address" : "123 Main Street"}

# Get a value with the key
print("Name :", derekDict["fName"])

# Dictionaries may not print out in the order created
# since they are unordered
print(derekDict)

# Add a new key value
derekDict['city'] = 'Pittsburgh'

# Check if a key exists
print('Is there a city :', 'city' in derekDict)

# Get the list of values
print(derekDict.values())

# Get the list of keys
print(derekDict.keys())

# Get the key and value with items()
for k, v in derekDict.items():
    print(k, v)
    
# get gets a value associated with a key or the default
print(derekDict.get('mName', 'Not Here'))

# Delete a key value
del derekDict['fName']

# Loop through the dictionary keys
for i in derekDict:
    print(i)
    
# Delete all entries
derekDict.clear()

# List for holding Dictionaries
employees = []

# Input employee data
fName, lName = input('Enter Employee Name: ').split()

employees.append({'fName' : fName, 'lName' : lName})

print(employees)