# Lab 7 
# Name: Miles Herrman
# Instructor: S. Einakian 
# Section: 3

#list comprehension tests
import unittest
from list_comp import *
from objects import *

class TestCases(unittest.TestCase):
   #Purpose: Test the point_distance_all function
   def test_distance1(self):
      self.assertEqual(point_distance_all([Point(1,0), Point(2,0), Point(0,5)]), [1.0,2.0,5.0])
      self.assertEqual(point_distance_all([Point(1,1), Point(2,2), Point(-4,0)]), [1.4142135623730951,2.8284271247461903,4.0])
      self.assertEqual(point_distance_all([Point(5,6), Point(-5,-6), Point(10,-2)]), [7.810249675906654, 7.810249675906654, 10.198039027185569])

   #Purpose: Test the are_in_first_quadrant function
   def test_quad(self):
      self.assertEqual(are_in_first_quadrant([Point(5,5), Point(3,-3), Point(-0.5,9)]), [Point(5,5)])
      self.assertEqual(are_in_first_quadrant([Point(5,-5), Point(3,3), Point(0.5,9)]), [Point(3,3),Point(0.5,9)])
      self.assertEqual(are_in_first_quadrant([Point(5,5), Point(3,3), Point(-2,2)]), [Point(5,5), Point(3,3)])

   #Purpose: Test the circle_distance_all function
   def test_distance2(self):
      self.assertEqual(circle_distance_all([Circle(Point(10,0),5)]), [5.0])
      self.assertEqual(circle_distance_all([Circle(Point(0,13),5),Circle(Point(-10,0),1)]), [8.0,9.0])
      self.assertEqual(circle_distance_all([Circle(Point(3,4),2),Circle(Point(-5,-5),1)]), [3.0,6.0710678118654755])
   
   #Purpose: Test the overlaps_all function
   def test_overlap(self):
      self.assertEqual(overlaps_all([Circle(Point(2,2),3)]), [Circle(Point(2,2),3)])
      self.assertEqual(overlaps_all([Circle(Point(2,2),3),Circle(Point(10,10),3),Circle(Point(-15,4),7)]), [Circle(Point(2,2),3)])
      self.assertEqual(overlaps_all([Circle(Point(0,0),1),Circle(Point(2,2),3),Circle(Point(3,4),9)]), [Circle(Point(0,0),1),Circle(Point(2,2),3),Circle(Point(3,4),9)])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()