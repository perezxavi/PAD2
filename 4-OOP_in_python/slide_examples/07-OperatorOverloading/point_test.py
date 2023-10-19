"""

Test of the 'Point' class."

"""

from point import Point

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(f"The sum of {p1} and {p2} is {p3}, and their difference is {p1 - p2}")
print(f"The opposite point of {p1} is {-p1}")
