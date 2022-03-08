# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Miles Herrman   
# Section: 3

import unittest
from map import *

class TestMap(unittest.TestCase):
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)
     
   def test_cube_all(self):	# Tests for the cube all function
      self.assertListAlmostEqual(cube_all([1,2,3]), [1,8,27])
      self.assertListAlmostEqual(cube_all([2,4,0]), [8,64,0])
      self.assertListAlmostEqual(cube_all([4,0,5]), [64,0,125])
   
   def test_add_n_to_all(self):	# Tests for the add n to all function
      self.assertListAlmostEqual(add_n_to_all([5,10,12,24], 10), [15,20,22,34])
      self.assertListAlmostEqual(add_n_to_all([1,2,3], 5), [6,7,8])
      self.assertListAlmostEqual(add_n_to_all([6,4,1,10,5], 2), [8,6,3,12,7])
   
   def test_div_by_5_all(self):	# Tests for div by 5 function
      self.assertListAlmostEqual(div_by_5_all([5,10,12,24]), [True, True, False, False])
      self.assertListAlmostEqual(div_by_5_all([0,100,11,25]), [True, True, False, True])   

if __name__ == '__main__':
   unittest.main()