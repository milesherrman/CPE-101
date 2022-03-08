# Lab 7 
# Name: Miles Herrman
# Instructor: S. Einakian 
# Section: 3

from tokenize import group
from typing import final

#Purpose: Group elements from input list into groups of 3
def groups_of_3(list_of_val: list) -> list:
    current_group = []
    grouped_list = []
    count = 0
    for idx in range(len(list_of_val)):
        current_group.append(list_of_val[idx])
        if count == 2 or idx == (len(list_of_val) - 1):
            grouped_list.append(current_group)
            count = 0
            current_group = []
        else:
            count += 1
    return grouped_list

#Purpose: Return a list of the final elements from each sublist
def final_value(list_of_lists: list) -> list:
    final_list = []
    for list in list_of_lists:
        if list != []:
            final_list.append(list[len(list) - 1])
    return final_list

#Purpose: Return a list of each value repeated by its corresponding value
def repeat_value(list_of_val: list) -> list:
    repeat_list = []
    final_list = []
    for val in list_of_val:
        for count in range(val):
            repeat_list.append(val)
        final_list.append(repeat_list)
        repeat_list = []
    return final_list