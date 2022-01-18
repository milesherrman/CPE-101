#Lab 2 Test Cases
#Name: Miles Herrman
#Section: 3
##############################################################
#3 test cases for each function

import math
import unittest
from funcs import *

class TestCases(unittest.TestCase):

   #testing mathematical expressions

   # 3 test cases for the given mathematical equation
   def test_do_math(self):
      self.assertAlmostEqual(do_math(9,5), -0.3253012)
      self.assertAlmostEqual(do_math(3,10), -4.2749999999)
      self.assertAlmostEqual(do_math(4,6), -1.660377358)
   
   # 3 test cases for the "+" version of the quadratic formula
   def test_quadratic_formula1(self):
      self.assertEqual(quadratic_formula1(1,2,1), -1)
      self.assertEqual(quadratic_formula1(3,5,2), -2/3)
      self.assertAlmostEqual(quadratic_formula1(1,8,3), -0.394448724)

   # 3 test cases for the "-" version of the quadratic formula   
   def test_quadratic_formula2(self):
      self.assertEqual(quadratic_formula2(1,2,1), -1.0)
      self.assertEqual(quadratic_formula2(3,5,2), -1.0)
      self.assertAlmostEqual(quadratic_formula2(1,8,3), -7.60555127)
      
   # 3 test cases for the Manhatten distance formula
   def test_distance(self):
      self.assertAlmostEqual(distance(1,1,2,2), 2)
      self.assertAlmostEqual(distance(4,6,2,9), 5)
      self.assertAlmostEqual(distance(0,0,10,15), 25)
      
   # 3 test cases for checking a positive number
   def test_is_positive(self):
      self.assertEqual(is_positive(5), True)
      self.assertEqual(is_positive(-5), False)
      self.assertEqual(is_positive(0), False)

   # 3 test cases for checking divisibility by 7
   def test_dividable_by_7(self):
      self.assertFalse(divisable_by_7(10))
      self.assertTrue(divisable_by_7(21))
      self.assertTrue(divisable_by_7(0))
      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

