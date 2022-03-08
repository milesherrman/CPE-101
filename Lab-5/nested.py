# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Miles Herrman   
# Section: 3

# Purpose: Return a new list made of the products of nested lists from input list
# Signature: list -> list
def product(nested_list):
    product_list = []
    for list in nested_list:
        product = 1
        for num in list:
            product *= num
        product_list.append(product)
    return product_list