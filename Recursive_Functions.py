# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:11:50 2021

@author: diogo
"""

# A function that refers to itself is a recursive function

# Calculating factorials is commonly done with a recursive
# funtion 3! = 3*2*1

def factorial(num):
    #Every recursive function must contain a condition
    # when it ceases to call itself
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result

print(factorial(4))

#-----PROBLEM: Calculate Fibonacci Numbers------
# To calculate Fibonacci numbers we sum the 2 previous
# values to calculate the next intem in the list like this
# 1, 1, 2, 3, 5, 8, 13, 21, ...

# The Fibonacci sequence is defined by:
# Fn = Fn-1 + Fn-2
# Where F0 = 0 and F1 = 1

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n-1) + fib(n-2)
        return result

print(fib(4))
print(fib(7))

numFibValues = int(input('How many Fibonacci values should be found:'))
                   
i = 1
while i < numFibValues:
    fibValue = fib(i)
    print(fibValue)
    i+=1
print('All done')

for i in range(1, numFibValues + 1):
    print(fib(i))
print('All done')