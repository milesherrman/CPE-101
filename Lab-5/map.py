# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Miles Herrman   
# Section: 3

# Purpose: Return a list of the cube of each value from the input list
# Signature: list -> list
def cube_all(input_list):
    return [num ** 3 for num in input_list]

# Purpose: Return a list with each element from input list summed with parameter n
# Signature: list int -> list
def add_n_to_all(input_list, n):
    idx = 0
    list_plus_n = []
    while idx < len(input_list):
        new_item = input_list[idx] + n
        list_plus_n.append(new_item)
        idx += 1
    return list_plus_n

# Purpose: Return a list of True/False based on the input integers being divisible by 5
# Signature: list -> list
def div_by_5_all(input_list):
    t_or_f = []
    for num in input_list:
        if num % 5 == 0:
            t_or_f.append(True)
        else:
            t_or_f.append(False)
    return t_or_f