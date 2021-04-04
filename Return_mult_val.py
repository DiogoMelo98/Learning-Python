# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 21:13:25 2021

@author: diogo
"""

# Return multiple values & exception handling
def mult_divide(num1, num2):
        return (num1*num2),(num1/num2)

try:
    mult, divide = mult_divide(5, 0)
    print('5 * 0 =', mult)
    print('5 / 0 =', divide)
except ZeroDivisionError:
    print('Cannot divide by zero!')

