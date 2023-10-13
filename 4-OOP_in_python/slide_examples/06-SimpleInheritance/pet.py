"""
Pet Interface.

Our pets play with the toy we give them and give us kisses.

All classes that implement (inherit) this interface must create the methods defined here.
"""
from abc import ABC, abstractmethod
from typeguard import typechecked

@typechecked
class Pet(ABC):

    @abstractmethod
    def play(self, toy: str):
        pass

    @abstractmethod
    def kiss(self):
        pass
