"""
Dog class that implements the Pet interface.

"""
from enum import Enum
from typeguard import typechecked
from animal import Animal, Sex
from pet import Pet

Size = Enum("Size", "SMALL MEDIUM LARGE")

@typechecked
class Dog(Animal, Pet):

    def __init__(self, name: str, size: Size = Size.MEDIUM, sex: Sex = Sex.MALE):
        super().__init__(name, sex)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value: Size):
        self.__size = value

    def eat(self, food: str):
        print(f"({self.name}) Woof! I love eating {food}! :-)")

    def play(self, toy: str):
        print(f"({self.name}) {toy}? I love playing! Woof woof! :-)")

    def kiss(self):
        print(f"({self.name}) Muah ;-)")

    def __str__(self):
        return super().__str__() + "Size: " + self.size.name + "\n"



