# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 21:59:42 2021

@author: diogo
"""

import random

def guess(x):
    rand_number = random.randint(1, x)
    guess = 0
    while guess != rand_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < rand_number:
            print('Ups. Too low! Try again!')
        elif guess > rand_number:
            print('Ups. Too high! Try again!')
    print(f'Yayy! You got it right! The number was {rand_number}')
    
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if high != low:
            guess = random.randint(low, high)
        else:
            guess = low #or high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C): ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'The computer guessed your number, {guess}, correctly!')