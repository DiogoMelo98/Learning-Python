# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:35:26 2021

@author: diogo
"""

'''
def change_name(name):
    return 'Mark'

name = 'Tom'

name = change_name(name)

print(name)
'''

glb_name = 'Sally'

def change_name():
    global glb_name
    glb_name = 'Sammy'
    
change_name()

print(glb_name)