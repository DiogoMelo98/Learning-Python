# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:40:04 2021

@author: diogo
"""

# Creat an array of customer ditionaries
# Output should look like this

'''
Enter Customer (Yes/No) : y
Enter Customer Name : Derek Banas
Enter Customer Name : y
Enter Customer Name : Sally Smith
Enter Customer Name : n
Derek Banas
Sally Smith
'''

# Create customer array outside the for so it isn't local
# to the while loop
customers = []

while True:
    # Cut off the 1st letter to cover if the user
    # types a n or y
    createEntry = input('Enter Customer (Yes/No) : ')
    createEntry = createEntry[0].lower()
    if createEntry == 'n':
        # Leave the while when n is entered
        break
    else:
        # Get the customer name by splitting at the space
        fName, lName = input('Enter Customer Name: ').split()
        # Add the dictionary to the array
        customers.append({'fName' : fName, 'lName' : lName})

# Print out customer list
for cust in customers:
    print(cust['fName'], cust['lName'])