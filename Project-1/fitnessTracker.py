# Main Program
# Project 1 Fitness Tracking
#
# Name: Miles Herrman
# Section: 3
# Date: 1/14/2022

from unicodedata import category
from fitnessTrackerFuncs import *
def main():
    n = False
    while n == False:
        #print welcome statement
        welcome()
        #Input values for given variables
        name = input_name()
        age = input_age()
        height = input_height()
        weight = input_weight()
        duration = input_duration()
        exercise_type = input_exercise_type()
        #Compute non-input variables
        miles = compute_equivalent_miles(height, exercise_type, duration)
        met_value = compute_MET(exercise_type)
        calorie_burned = compute_calorie_burned(duration, weight, met_value)
        BMI = compute_BMI(weight, height)
        #Print info to user
        print_info(name, age, height, weight, calorie_burned, BMI, miles)
        print(" ")
        #Prompt user for another fitness tracking 
        another = input("Do you want to apply fitness tracking for another user? (y/n)  ")
        print(" ")
        if another == 'n':
            n = True

if __name__ == '__main__':
    main()
