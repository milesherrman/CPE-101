# Lab 7 
# Name: Miles Herrman
# Instructor: S. Einakian 
# Section: 3

import unittest
from objects import *

class TestCases(unittest.TestCase):
   #Purpose: Test the point intialization function
   def test_point_init(self):
      p1 = Point(1,5)
      self.assertEqual(p1.x, 1)
      self.assertEqual(p1.y, 5)

   #Purpose: Test the point equality function
   def test_point_eq(self):
      p1 = Point(1,5)
      p2 = Point(2,4)
      p3 = Point(1,5)
      self.assertFalse(p1 == p2)
      self.assertTrue(p1 == p3)

   #Purpose: Test the point repr function
   def test_point_repr(self):
      p1 = Point(1,5)
      self.assertEqual(repr(p1),"(1,5)")
      self.assertNotEqual(repr(p1),"(2,7)")

   #Purpose: Test the point distance function
   def test_point_distance(self):
      p1 = Point(0,0)
      p2 = Point(3,0)
      p3 = Point(3,4)
      self.assertEqual(Point.distance(p1,p2), 3)
      self.assertEqual(Point.distance(p2,p3), 4)
      self.assertEqual(Point.distance(p1,p3), 5)

   #Purpose: Test the circle intialization function
   def test_circle_init(self):
      c1 = Circle(Point(2,2),5)
      self.assertEqual(c1.center, Point(2,2))
      self.assertEqual(c1.rad, 5)

   #Purpose: Test the circle equality function
   def test_circle_eq(self):
      c1 = Circle(Point(2,2),5)
      c2 = Circle(Point(0,0),3)
      c3 = Circle(Point(2,2),5)
      self.assertFalse(c1 == c2)
      self.assertFalse(c2 == c3)
      self.assertTrue(c1 == c3)

   #Purpose: Test the cirlce inequality function
   def test_circle_ne(self):
      c1 = Circle(Point(0,0),5)
      c2 = Circle(Point(1,1),5)
      c3 = Circle(Point(1,1),2)
      self.assertFalse(c1 != c2)
      self.assertFalse(c2 != c3)
      self.assertTrue(c1 != c3)

   #Purpose: Test the circle repr function
   def test_circle_repr(self):
      c1 = Circle(Point(0,0),5)
      c2 = Circle(Point(1,1),3)
      self.assertEqual(repr(c1), "5 @ (0,0)")
      self.assertEqual(repr(c2), "3 @ (1,1)")
   
   #Purpose: Test the circle overlap function
   def test_circle_overlap(self):
      c1 = Circle(Point(-1,0),1.5)
      c2 = Circle(Point(1,0),1.5)
      c3 = Circle(Point(0,5),1)
      self.assertTrue(Circle.overlaps(c1,c2))
      self.assertFalse(Circle.overlaps(c2,c3))
      self.assertFalse(Circle.overlaps(c1,c3))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()