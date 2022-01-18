# Name: Miles Herrman
# Section: 3

    # Purpose: Check if an integer is odd
    # Signature: int -> bool
def is_odd(num):
    isOdd = num % 2
    return isOdd == 1

    # Purpose: Check if an integer is within the given intervals
    # Signature: int -> bool
def is_an_interval(num):
    interval_1 = (num >= -10 and num < -4)
    interval_2 = (num >= -2 and num <= 8)
    interval_3 = (num > 27 and num < 52)
    interval_4 = (num >= 10 and num <= 22)
    interval_5 = (num >= 110 and num <= 237)
    return interval_1 or interval_2 or interval_3 or interval_4 or interval_5

    # Purpose: Check if an integer is within a given interval, and check if it's
    #           divisble by a second integer, which must also be within a given interval
    # Signature: int int -> bool
def is_divisible_in_interval(num_1, num_2):
    interval_1 = (num_1 >= 75 and num_1 <= 140)
    interval_2 = (num_2 > 30 and num_2 <= 200)
    is_divisable = num_1 % num_2
    return interval_1 and interval_2 and (is_divisable == 0)
