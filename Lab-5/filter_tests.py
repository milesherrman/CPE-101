# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Miles Herrman   
# Section: 3

import unittest
from filter import *

class TestFilter(unittest.TestCase):
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)
   
   def test_are_even(self):	# Tests for remove duplicate function
      self.assertListAlmostEqual(are_even([1,2,3,4,5,6,7,8]), [2,4,6,8])
      self.assertListAlmostEqual(are_even([-3,0,2,7,11,46]), [0,2,46])
      self.assertListAlmostEqual(are_even([4,3,8,6,45]), [4,8,6])
   
   def test_remove_duplicates(self):	# Tests for remove duplicate function
      self.assertListAlmostEqual(remove_duplicates([1,2,3,4,5,4,6,4,7]), [1,2,3,4,5,6,7])
      self.assertListAlmostEqual(remove_duplicates([0,0,1,1,2,2,1,1,3]), [0,1,2,3])
      self.assertListAlmostEqual(remove_duplicates([9,9,2,6,9,2,1]), [9,2,6,1])
   
   def test_are_divisible_by_n(self):	# Tests for remove duplicate function
      self.assertListAlmostEqual(are_divisible_by_n([1,2,3,4,5,6,7], 2), [2,4,6])
      self.assertListAlmostEqual(are_divisible_by_n([1,2,3,4,5,6,7,8,9], 3), [3,6,9])
      self.assertListAlmostEqual(are_divisible_by_n([1,2,3,4,5,6,7], 0), [])
   
if __name__ == '__main__':
   unittest.main()