# Project 1 Fitness Tracking
#
# Name: Miles Herrman
# Section: 3
# Date: 1/14/2022

# purpose: Provide intro statements to user
# signature: none -> str
def welcome():
    print(" ")
    print("Welcome to Fitness Tracker Application!")
    print("To begin, you must specify the participant's age, name, height (in inches),")
    print("weight (in lb), exercise duration (in minutes), and exercise type (1-4)!")
    print("Now you can compute the burned calories and BMI")

# purpose: Ask user for name
# signature: none -> str
def input_name():
    print(" ")
    name = input("Enter the name: ")
    return name

# purpose: Ask user for age input, cast to int
# signature: none -> int
def input_age():
    print(" ")
    age = input("Enter age: ")
    while int(age) <= 0:
        print(" ")
        print("Error: Age must be an integer > 0!")
        print(" ")
        age = input("Enter age: ")
    return int(age)

# purpose: Ask user for height input, cast to float
# signature: none -> float
def input_height():
    print(" ")
    height = input("Enter height in inches: ")
    while float(height) <= 0.0:
        print(" ")
        print("Error: Height must be greater than 0!")
        print(" ")
        height = input("Enter height in inches: ")
    return float(height)

# purpose: Ask user for weight input, cast to float
# signature: none -> float
def input_weight():
    print(" ")
    weight = input("Enter weight in lb: ")
    while float(weight) <= 0.0:
        print(" ")
        print("Error: Weight must be greater than 0!")
        print(" ")
        weight = input("Enter weight in lb: ")
    return float(weight)
    

# purpose: Ask user for duration unput, cast to float
# signature: none -> float
def input_duration():
    print(" ")
    duration = input("Enter duration of exercise in minutes: ")
    while float(duration) <= 0.0:
        print(" ")
        print("Error: Duration must be greater than 0!")
        print(" ")
        duration = input("Enter duration of exercise in minutes: ")
    return float(duration)

# purpose: Ask user for exercise type input
# signature: none -> int
def input_exercise_type():
    print(" ")
    exercise_type = int(input("Enter exercise type: 1) Low-impact 2) High-impact 3) Slow-paced 4) Fast-paced  "))
    while int(exercise_type) < 1 or int(exercise_type) > 4:
        print(" ")
        print("Error: Exercise type must be an integer between [1,4]!")
        print(" ")
        exercise_type = int(input("Enter exercise type [1,4]: "))
    return exercise_type

# purpose: Print user info
# signature: str int float float float float float str
def print_info(name, age, height, weight, calorie_burned, BMI, miles):
   category = BMI_category(BMI)
   print("           Name :  ", name)
   print("            Age :  ", age)
   print("         Height :  ",'%.2f'%height, " inches")
   print("         Weight : ",'%.2f'%weight, " lb")
   print("{0:}{1:6.2f}".format("          Miles :  ", miles))
   print("{0:}{1:7.2f}".format("Burned Calories : ", calorie_burned))
   print("            BMI :  ",'%.2f'%BMI)
   print("   BMI Category : ", category)
  

# purpose: Convert the input weight from pounds to kilos
# signature: float -> float
def convert_lb_to_kg(weight):
    return weight * 0.45359237

# purpose: Convert exercise type to MET type
# signature: int -> int
def compute_MET(exercise_type):
    if exercise_type == 4:
        return 4
    elif exercise_type == 3:
        return 3
    elif exercise_type == 2:
        return 7
    else:
        return 5
   
# purpose: Calculate the total calories burned during the activity
# signature: float float int -> float
def compute_calorie_burned(duration, weight, met_value):
    return duration * compute_MET(met_value) * 3.5 * convert_lb_to_kg(weight) / 200
    

# purpose:
# signature: float float -> float
def compute_BMI(weight, height):
    return 703 * weight / height ** 2
    

# purpose: Return the BMI category of the user
# signature: float -> string
def BMI_category(BMI):
    if BMI < 18.59:
        return "Under Weight"
    elif BMI < 25:
        return "Normal Weight"
    elif BMI < 30:
        return "Over Weight"
    else:
        return "Obese"
    

# purpose: Compute the total distance the user travelled
# signature: float int float -> float
def compute_equivalent_miles(height, exercise_type, duration):
    
    stride_length = 0.413 * height / 12

    if exercise_type == 1:
       steps_per_min = 120
    elif exercise_type == 2:
       steps_per_min = 227
    elif exercise_type == 3:
       steps_per_min = 100
    else:
        steps_per_min = 152

    return stride_length * steps_per_min * duration / 5280