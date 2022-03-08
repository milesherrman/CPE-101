# Lab 7 
# Name: Miles Herrman
# Instructor: S. Einakian 
# Section: 3

from utility import *
class Point:
    #Purpose: Initialize the x and y variables (both are integer values)
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    #Purpose: Check equality of 2 points
    def __eq__(self, other) -> bool:
        return type(self) == type(other) == Point and \
            epsilon_equal(self.x, other.x) and \
            epsilon_equal(self.y, other.y)

    #Purpose: Return the coordinate value of the point (x,y) as a string
    def __repr__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"

    #Purpose: Calculate the euclidian distance between two points
    def distance(self, to) -> float:
        return ((self.x - to.x)**2 + (self.y - to.y)**2)**0.5

class Circle:
    #Purpose: Initialize the center and radius variables
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.rad = radius
    
    #Purpose: Check equality of two circles
    def __eq__(self, other) -> bool:
        return type(self) == type(other) == Circle and \
            self.center == other.center and \
            self.rad == other.rad

    #Purpose: Check inequality of two circles
    def __ne__ (self, other) -> str:
        return self.center != other.center and \
            self.rad != other.rad

    #Purpose: Return radius and center point of the circle as a string
    def __repr__ (self) -> str:
        return str(self.rad) + " @ " + "(" + str(self.center.x) + "," + str(self.center.y) + ")"

    #Purpose: Check if two circles have any overlapping points
    def overlaps(self, other) -> bool :
        return Point.distance(self.center, other.center) < (self.rad + other.rad)