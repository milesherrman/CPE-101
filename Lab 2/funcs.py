#Lab 2 Functions
#Name: Miles Herrman
#Section: 3
import math

#1)purpose statement: This function computes the given formula
# signature:int int -> float

def do_math (x, y):
   return (x ** 2 - (3/5) * x * (y ** 2))/((2 * x ** 2 * y) / 5 + 4)
   
#2)purpose statement: This function computes the "+" version of the quadratic formula
# signature: 3 floats -> 1 float
def quadratic_formula1 (a, b, c):
   return (-1*b + math.sqrt(b**2 - 4*a*c)) / (2*a)
   
#3)purpose statement: This function computes the "-" version of the quadratic formula
# signature: 3 floats -> 1 float
def quadratic_formula2 (a, b, c):
   return (-1*b - math.sqrt(b**2 - 4*a*c)) / (2*a)
 
#4)purpose statement: This function computes the Manhatten distance between two points
# signature: 4 integers -> 1 integer
def distance (x1, y1, x2, y2):
   return abs(x1 - x2) + abs(y1 - y2)
    
#5)purpose statement: This function checks if a given number is positive
# signature: 1 integer -> 1 boolean
def is_positive (num):
   return num > 0
    
#6)purpose statement: This function checks if a given number is divisable by 7
# signature: 1 integer -> 1 boolean
def divisable_by_7 (num):
   div = num % 7
   return div == 0