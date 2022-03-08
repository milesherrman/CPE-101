# Main Program
# Project 2: Barista Coffee Assistant
#
# Name: Miles Herrman
# Section: 3
# Date: 1/25/2022
#
from tkinter import Y
from baristaCoffeeFuncs import *

def main():
    while True:

        #Ask user for coffee type and prompt milk option based on input
        coffee_type = type_prompt()
        if coffee_type == "error":
            break
        elif coffee_type == "AMERICANO" or coffee_type == "ESPRESSO":
            milk_option = milk_prompt()
            if milk_option == "error":
                break
        else:
            milk_option = "No extras"

        #Ask user to input coffee size
        size = size_prompt()
        if size == "error":
            break

        #Ask user if the order is takeout
        takeout = takeout_prompt()
        if takeout == "error":
            break

        #Print out order
        print_order(coffee_type, milk_option, takeout)

        #Return the total due
        total_due(coffee_type, milk_option, size)

        #Prompt user for another order
        another_order = extra_order()
        if another_order == "N":
            break
        print(" ")

if __name__ == '__main__':
    main()