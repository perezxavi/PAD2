"""
Animal Class, which will be an abstract class, serving as the base for other classes to demonstrate inheritance.

In Python, you can create an abstract class using the `abc` module. You use `ABC` as the base class and the `@abstractmethod` decorator to indicate abstract methods. Subclasses of an abstract class must implement the methods marked as abstract, or else an error will occur.

It is not possible to instantiate an abstract class; it serves as a template for generating other classes.

"""

from typeguard import typechecked
from enum import Enum
from abc import ABC, abstractmethod

Sex = Enum('Sex', 'MALE FEMALE')  # Enum type, ensuring that the 'sex' attribute can only have values MALE or FEMALE

@typechecked
class Animal(ABC):

    def __init__(self, name: str, sex: Sex = Sex.MALE):
        self.__name = name
        self.__sex = sex

    @property
    def name(self):
        return self.__name

    @property
    def sex(self):
        return self.__sex

    def __str__(self):
        return f"Name: {self.name}, Sex: {self.sex.name}\n"

    def sleep(self):
        print(f"({self.name}) Zzzzzzz")

    @abstractmethod
    def eat(self, food: str):
        pass