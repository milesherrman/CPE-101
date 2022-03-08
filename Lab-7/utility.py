# Lab 7 
# Name: Miles Herrman
# Instructor: S. Einakian 
# Section: 3

#check equality of two float value
def epsilon_equal(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)