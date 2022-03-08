# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Miles Herrman   
# Section: 3

# Purpose: Add two polynomials together using lists and return the result
# Signature: list list -> list
def poly_add2(poly1, poly2):
    poly3 = []
    poly3.append(poly1[0] + poly2[0])
    poly3.append(poly1[1] + poly2[1])
    poly3.append(poly1[2] + poly2[2])
    return poly3

# Purpose: Multiply two polynomials together using lists and return the result
# Signature: list list -> list
def poly_mult2(poly1, poly2):
    poly3 = []
    poly3.append(poly1[0]*poly2[0])
    poly3.append((poly1[0]*poly2[1]) + (poly1[1]*poly2[0]))
    poly3.append((poly1[1]*poly2[1]) + (poly1[0]*poly2[2]) + (poly1[2]*poly2[0]))
    poly3.append((poly1[1]*poly2[2]) + (poly1[2]*poly2[1]))
    poly3.append(poly1[2]*poly2[2])
    return poly3