# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 23:50:24 2021

@author: diogo
"""

# Using functions in this problem avoids the use of multiple if's and elif's
# Homework: add area of triangle, paralelogram, rhombuses and trapezoids

import math

def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    elif shape == "parallelogram":
        parallelogram_area()
    elif shape == "triangle":
        triangle_area()
    elif shape == "rhombus":
        rhombus_area()
    elif shape == "trapezoid":
        trapezoid_area()
    else:
        print("Please enter rectangle, circle, triangle, rhombuse or trapezoid")

def rectangle_area():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    
    area = length * width
    
    print("The area of the rectangle is ", area)
    
def circle_area():
    radius = float(input("Enter the circle's radius: "))
    
    area = math.pi * math.pow(radius, 2)
    
    print("The area of the circle is {:.2f}".format(area))
    
def parallelogram_area():
    length = float(input("Enter the length: "))
    height = float(input("Enter the height: "))
    
    area = length * height
    
    print("The area of the parallelogram is ", area)
    
def triangle_area():
    base = float(input("Enter the base: "))
    height = float(input("Enter the height of the triangle: "))
    
    area = base * height / 2
    
    print("The area of the triangle is ", area)
    
def rhombus_area():
    diag1 = float(input("Enter the first diagonal: "))
    diag2 = float(input("Enter the second diagonal: "))
    
    area = 0.5 * diag1 * diag2
    
    print("The area of the rhombus is ", area)
    
def trapezoid_area():
    base1 = float(input("Enter a base: "))
    base2 = float(input("Enter the other base: "))
    height = float(input("Enter the height: "))
    
    area = (base1 + base2) * 0.5 * height
    
    print("The area of the trapezoid is ", area)

def main():
    shape_type = input("Get area for what shape: ")
    get_area(shape_type)
    
main()