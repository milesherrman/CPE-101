# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Miles Herrman   
# Section: 3

# Purpose: Return a list of all even values from the given list
# Signature: list -> list
def are_even(input_list):
    return [num  for num in input_list if num % 2 == 0]

# Purpose: Return a list that removes any duplicate entries from given list
# Signature: list -> list
def remove_duplicates(input_list):
    no_duplicates = []
    if input_list == []:
        return []
    else:
        for idx1 in range(len(input_list)):
            count = 0
            for idx2 in range(idx1 + 1):
                if input_list[idx1] == input_list[idx2]:
                    count += 1
            if(count <= 1):
                no_duplicates.append(input_list[idx1])
        return no_duplicates
        
# Purpose: Return a list of given entries that are divisible by n
# Signature: list int -> list
def are_divisible_by_n(given_list, n):
    idx = 0
    div_by_n = []
    if n == 0:
        return []
    else:
        while idx < len(given_list):
            if given_list[idx] % n == 0:
                div_by_n.append(given_list[idx])
            idx += 1
    return div_by_n
