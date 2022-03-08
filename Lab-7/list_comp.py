# Lab 7 
# Name: Miles Herrman
# Instructor: S. Einakian 
# Section: 3

from objects import *

#Purpose: Return a list of each points distance to the origin
def point_distance_all(points: list[Point]) -> list[float]:
    dist_list = [Point.distance(point, Point()) for point in points]
    return dist_list

#Purpose: Return a list of points that lay in the first quadrant
def are_in_first_quadrant(points: list[Point]) -> list[Point]:
    list_of_points = [point for point in points if point.x >= 0 and point.y >= 0]
    return list_of_points

#Purpose: Return a list of the distance from the origin to the nearest point on the circle
def circle_distance_all(circles: list[Circle]) -> list[float]:
    dist_to_circle = [Point.distance(circle.center, Point()) - circle.rad for circle in circles]
    return dist_to_circle

#Purpose: Return a list of circles that overlap the unit circle
def overlaps_all(circles: list[Circle]) -> list[Circle]:
    unitCirc = Circle(Point(0,0), 1.0)
    overlap_circles = [circle for circle in circles if Circle.overlaps(circle, unitCirc) == True]
    return overlap_circles