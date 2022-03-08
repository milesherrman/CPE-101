# Lab 7 
# Name: Miles Herrman
# Instructor: S. Einakian 
# Section: 3

#unittest for objects
import unittest
from nested_list import *

class TestCases(unittest.TestCase):
   def test_groups_of_3(self):
      self.assertEqual(groups_of_3([1,2,3,4,5,6,7,8,9]),[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
      self.assertEqual(groups_of_3([1,2,3,4,5,6,7,8]),[[1, 2, 3], [4, 5, 6], [7, 8]])
      self.assertEqual(groups_of_3([4,2,3,4]),[[4, 2, 3], [4]])

   def test_final_value(self):
      self.assertEqual(final_value([[-1, 12,3], [8], [], [1,-3]]), [3,8,-3])
      self.assertEqual(final_value([[14,23,34,45], [], [-1], [1,2,3]]), [45,-1,3])
      self.assertEqual(final_value([[], [], [1,2,3,4,5], [5,4,3,2,1]]), [5,1])

   def test_repeat_value(self):
      self.assertEqual(repeat_value([1,2,3,4]), [[1],[2,2],[3,3,3],[4,4,4,4]])
      self.assertEqual(repeat_value([1,5,3,0]), [[1],[5,5,5,5,5],[3,3,3],[]])
      self.assertEqual(repeat_value([1,2,0,2]), [[1],[2,2],[],[2,2]])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()