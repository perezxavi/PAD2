"""
"Rectangle" Class (Immutable) defined by its two sides (width and height).

It has properties for its area and perimeter.

"""
from typeguard import typechecked

@typechecked
class Rectangle:

    def __init__(self, width: int, height: int):
        if width <= 0 or height <= 0:
            raise ValueError("The sides must be positive integers.")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def area(self):
        return self.width * self. height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width}, {self.height})"
