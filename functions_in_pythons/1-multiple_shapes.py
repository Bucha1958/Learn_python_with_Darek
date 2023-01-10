#!/usr/bin/python3
"""
    Import a math module for a program that will calculate area of different shapes
"""
import math


# get_shape function will acts as a routing to other functions in this program
def get_shape(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_func()
    elif shape == "circle":
        circle_func()
    elif shape == "triangle":
        triangle_func()
    elif shape == "parallelogram":
        parallelogram_func()
    else:
        print("Rectangle and circle functions are the only functions available now")

# The rectangle function
def rectangle_func():
    width = float(input("Width of the rectangle: "))
    heigth = int(input("Heigth of the rectangle: "))
    area = width * heigth
    print("The area of a rectangle is {:.2f}".format(area))

# The circle function
def circle_func():
    radius = float(input("Radius: "))
    area = math.pi * pow(radius, 2)
    print("Area of a circle is {:.2f}".format(area))

# The function that calculates the area of a triangle
def triangle_func():
    breath = float(input("Breadth of Triangle: "))
    heigth = int(input("Heigth of Triangle: "))
    area = (1 / 2) * breath * heigth
    print("The area of Triangle: {:.2f}".format(area))

# The function that calculates the area of a parallelogram
def parallelogram_func():
    base = float(input("Enter the base: "))
    heigth = float(input("Enter the heigth: "))
    area = base * heigth
    print("The area of parallelogram: {:.1f}".format(area))


def main():
    shape_type = input("Enter the shape type: ")

    get_shape(shape_type)


main()
