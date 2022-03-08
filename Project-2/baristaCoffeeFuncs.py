# Functions (have at least 4 functions)
# Project 2: Barista Coffee Assistant
#
# Name: Miles Herrman
# Section: 3
# Date: 2/1/2022
#

# Purpose: Give the user 3 attempts to input their coffee order correctly, 
#          then return the value so it can be stored in a variable
# Signature: none -> string 
def type_prompt():
    num_tries = 0
    while num_tries < 3:
        coffee_type = (input("What coffee type would you like? ")).upper()
        if coffee_type == "AMERICANO" or coffee_type == "ESPRESSO" or coffee_type == "FLAT WHITE" or coffee_type == "LATTE":
            return coffee_type
        elif num_tries < 2:
            print("Can you please try again?")
        num_tries += 1
    print("Sorry, we cannot help you here") 
    return "error"

# Purpose: Give the user 3 attempts to input their choice of milk correctly, 
#          then return the value so it can be stored in a variable
# Signature: none -> string  
def milk_prompt():
    num_tries = 0
    while num_tries < 3:
        milk_option = (input("Would you like milk on the side [y/n]? ")).upper()
        if milk_option == "Y":
            return "Milk on the side"
        elif milk_option == "N":
            return "No milk on the side"
        elif num_tries < 2:
            print("Can you please try again?")
        num_tries += 1
    print("Sorry, we cannot help you here")
    return "error"

# Purpose: Give the user 3 attempts to input their coffee size correctly, 
#          then return the value so it can be stored in a variable 
# Signature: none -> string 
def size_prompt():
    num_tries = 0
    while num_tries < 3:
        size = (input("What size do you want [Large, Medium, Small]? ")).upper()
        if size == "LARGE" or size == "MEDIUM" or size == "SMALL":
            return size
        elif num_tries < 2:
            print("Can you please try again?")
        num_tries += 1
    print("Sorry, we cannot help you here")
    return "error"

# Purpose: Give the user 3 attempts to input their takeout choice correctly, 
#          then return the value so it can be stored in a variable
# Signature: none -> string 
def takeout_prompt():
    num_tries = 0
    while num_tries < 3:
        takeout = (input("Is your coffee takeout [y/n]? ")).upper()
        if takeout == "Y":
            return "Takeout"
        elif takeout == "N":
            return "In cafe"
        elif num_tries < 2:
            print("Can you please try again?")
        num_tries += 1
    print("Sorry, we cannot help you here")
    return "error"

# Purpose: Print out the customers order (type of coffee, option of milk on the side, takeout or in cafe
# Signature: string string string -> none
def print_order(coffee_type, milk_option, takeout):
    if coffee_type == "AMERICANO":
        print("Americano")
    elif coffee_type == "ESPRESSO":
        print("Espresso")
    elif coffee_type == "FLAT WHITE":
        print("Flat White")
    else:
        print("Latte")
    
    print(milk_option)
    print(takeout)

# Purpose: Calculate the total cost of the order based on user input, and display that value to the customer
# Signature: string string string -> int
def total_due(coffee_type, milk_option, size):
    total = 0.0

    if coffee_type == "FLAT WHITE":
        if size == "LARGE":
            total += 3.75
        elif size == "MEDIUM":
            total += 3.00
        else:
            total += 2.95

    elif coffee_type == "LATTE":
        if size == "LARGE":
            total += 4.15
        elif size == "MEDIUM":
            total += 3.75
        else:
            total += 2.85

    elif coffee_type == "AMERICANO" or coffee_type == "ESPRESSO":
        if size == "LARGE":
            total += 3.25
        elif size == "MEDIUM":
            total += 2.95
        else:
            total += 2.75
        if milk_option == "Milk on the side":
            total += 0.25
    
    print("Please pay", "{0:}{1:.2f}".format("$",total), "to the cashier")
    print(" ")
    return total

# Purpose: Give the user 3 attempts to place another order
# Signature: none -> string
def extra_order():
    num_tries = 0
    while num_tries < 3:
        another_order = (input("Do you have another order [y/n]? ")).upper()
        if another_order == 'Y':
            return 'Y'
        elif another_order == 'N':
            return 'N'
        else:
            print("Please enter a valid input.")
            num_tries += 1
        
    print("Sorry, we cannot help you here. ")
    return 'N'  