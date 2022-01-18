
# This is a header block example for lab 03.

# You will need to supply the following information.

# Name: Miles Herrman
# Section: 3

import unittest
from logic import *


class TestCases(unittest.TestCase):
   
   # 3 test cases for the is_odd function
   def test_is_odd (self):
      self.assertTrue(is_odd(5))
      self.assertFalse(is_odd(10))
      self.assertTrue(is_odd(15))

   # 6 test cases for the is_an_interval function
   def test_is_an_interval (self):
      self.assertFalse(is_an_interval(-12))
      self.assertTrue(is_an_interval(-1))
      self.assertFalse(is_an_interval(9))
      self.assertTrue(is_an_interval(34))
      self.assertFalse(is_an_interval(52))
      self.assertTrue(is_an_interval(147))

   # 3 test cases for the is_divisible_in_interval function
   def test_is_divisible_in_interval (self):
      self.assertTrue(is_divisible_in_interval(100,50))
      self.assertFalse(is_divisible_in_interval(85,50))
      self.assertTrue(is_divisible_in_interval(140,35))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

