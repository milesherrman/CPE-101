# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Miles Herrman   
# Section: 3

import unittest
from poly import *

class TestPoly(unittest.TestCase):
   #do not delete this part, use this to comapre two lists
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)
   
   def test_polyadd(self):	# Tests for add function
      self.assertListAlmostEqual(poly_add2([1.1, 2.2, 3.3],[4.0 , 1.0, 2.1]), [5.1, 3.2, 5.4])
      self.assertListAlmostEqual(poly_add2([3.4, 1.2, 5.3],[0.2 , 1.5, 1.1]), [3.6, 2.7, 6.4])
      self.assertListAlmostEqual(poly_add2([7.1, 3.0, 5.3],[0.1 , 1.0, 1.7]), [7.2, 4.0, 7.0])

   def test_polymult(self):	# Tests for add function
      self.assertListAlmostEqual(poly_mult2([1, 2, 3],[2 , 4, 1]), [2, 8, 15, 14, 3])
      self.assertListAlmostEqual(poly_mult2([3, 4, 1],[1, 2, 2]), [3, 10, 15, 10, 2])
      self.assertListAlmostEqual(poly_mult2([1, 1, 1],[2, 2, 2]), [2, 4, 6, 4, 2])

if __name__ == '__main__':
   unittest.main()