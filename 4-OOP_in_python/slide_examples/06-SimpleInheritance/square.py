"""
Square Class Derived from the Rectangle Class. An Example of Inheritance.

A square is a rectangle with both width and height having the same value. To determine it, we only need the side length.

This inheritance wouldn't be suitable if the rectangle were not immutable, or if we wanted to hide the "width" and "height" 
properties. In that case, we would violate the Liskov Substitution Principle, which tells us that if we use a class somewhere in our code, and this class is extended, we should be able to use any of the child classes, and the program should remain valid.

"""
from typeguard import typechecked
from rectangle import Rectangle

@typechecked


class Square(Rectangle):

    def __init__(self, side: int):
        super().__init__(side, side)  # calling the constructor of Rectangle

    @property
    def side(self):
        return self.width  # or self.height

    def __repr__(self):  # redefining this method
        return f"{self.__class__.__name__}({self.side})"