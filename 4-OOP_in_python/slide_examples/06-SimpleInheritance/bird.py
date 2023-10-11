""""
Bird Class derived from Animal. In addition to the behaviors defined for animals, birds will groom themselves and fly.

Since the Animal class has the eat() method as abstract, it is mandatory to implement it here.

"""

from typeguard import typechecked
from animal import Animal

@typechecked
class Bird(Animal):

    def eat(self, food: str):
        """
        Our birds eat whatever we give them.
        """
        print(f"({self.name}) Hmmmm, thank you :-)")

    def wash_yourself(self):
        print(f"({self.name}) I'm cleaning my feathers ;-)")

    def flight(self):
        print(f"({self.name}) I'm flying!")