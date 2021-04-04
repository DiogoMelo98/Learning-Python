# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:49:21 2021

@author: diogo
"""

#Solve for x
# x + 4 = 9 : 4 + x = 9

# x will always be the 1st value received and you will
# only deal with addition

# Receive the string and split the string into variables
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()
# Convert the strings into ints
    num1, num2 = int(num1), int(num2)
# Convert the result into a string and join it to the string 'X = '
    return 'x = ' + str(num2 - num1)
# print()
print(solve_eq('x + 4 = 9'))

def solve_eq_2(equation):
    num1, add, x, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    return 'x = ' + str(num2 - num1)
print(solve_eq_2('4 + x = 9'))

def solve_eq_3(equation):
    x, minus, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    return 'x = ' + str(num1 + num2)
print(solve_eq_3('x - 3 = 12'))

#analogous solution for * and / 