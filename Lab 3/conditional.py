# Name: Miles Herrman
# Section: 3

# Purpose: Given two integers, return the smaller value
# Signature: int int -> int
def min_of_2(num_1, num_2):
    if num_1 <= num_2:
        return num_1
    return num_2

# Purpose: Given three integers, return the smallest value
# Signature: int int int -> int
def min_of_3(num_1, num_2, num_3):
    min = min_of_2(min_of_2(num_1,num_2), num_3)
    return min

# Purpose: Check if an integer is odd
# Signature: int -> bool
def rental_late_fee(days_late):
    if days_late <= 2:
        return 0
    elif days_late <= 5:
        return 10
    elif days_late <= 12:
        return 15
    elif days_late <= 22:
        return 30
    else:
        return 100