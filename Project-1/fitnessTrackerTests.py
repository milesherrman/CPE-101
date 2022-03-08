# Project 1 Fitness Tracking Tests
# At least 2 tests for each function

# Name: Miles Herrman
# Section: 3
# Date: 1/14/2022

import unittest
from fitnessTrackerFuncs import *

class MyTestCase(unittest.TestCase):
    #Test the compute_equivalent_miles function
    def test_compute_equivalent_miles(self):
        self.assertEqual(compute_equivalent_miles(70, 1, 0), 0)
        self.assertAlmostEqual(compute_equivalent_miles(61, 4, 30), 1.813132575)
        self.assertAlmostEqual(compute_equivalent_miles(55, 2, 60), 4.882864583)

    #Test the convert_lb_to_kg function
    def test_convert_lb_to_kg(self):
        self.assertEqual(convert_lb_to_kg(0), 0)
        self.assertAlmostEqual(convert_lb_to_kg(150), 68.0388555)
        self.assertAlmostEqual(convert_lb_to_kg(250), 113.3980925)
    
    #Test the compute_MET function
    def test_compute_MET(self):
        self.assertEqual(compute_MET(1), 5)
        self.assertEqual(compute_MET(2), 7)
        self.assertEqual(compute_MET(3), 3)

    #Test the compute_calorie_burned function
    def test_compute_calorie_burned(self):
        self.assertAlmostEqual(compute_calorie_burned(45, 150, 5), 267.90299353)
        self.assertAlmostEqual(compute_calorie_burned(85, 190, 7), 640.98271785)
        self.assertAlmostEqual(compute_calorie_burned(15, 110, 3), 39.29243905)

    #Test the compute_BMI function   
    def test_compute_BMI(self):
        self.assertAlmostEqual(compute_BMI(150, 70), 21.52040816)
        self.assertAlmostEqual(compute_BMI(0, 65), 0)
        self.assertAlmostEqual(compute_BMI(250, 80), 27.4609375)

    #Test the BMI_category function
    def test_BMI_category(self):
        self.assertEqual(BMI_category(22), "Normal Weight")
        self.assertEqual(BMI_category(45), "Obese")
        self.assertEqual(BMI_category(14), "Under Weight")


if __name__ == '__main__':
    unittest.main()
