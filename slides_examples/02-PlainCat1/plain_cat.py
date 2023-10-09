"""
We are going to create the 'Simple Cat' class, which we call that because later on, 
we will create another slightly more elaborate class called 'Cat.'

To determine what attributes this class should have, we need to ask ourselves what 
characteristics cats have. All cats have a specific color, belong to a breed, have an age, 
have a certain gender (males or females), and have a weight that can be expressed in kilograms. 
These will be the attributes of the 'Simple Cat' class.

To determine what methods we should implement, we need to consider what actions are associated 
with cats. Well, cats meow, purr, eat, and if they are males, they fight with each other to 
compete for the favor of females. These will be the methods we define in the class.

Although this version is functional, as it is implemented, inconsistent objects can be created. 
I invite you to find situations where this can occur.
"""
import datetime


class PlainCat:

    def __init__(self, name, sex):
        """
        Constructor
        """
        self.name = name
        self.sex = sex
        self.species = ''
        self.birth_day = datetime.date.today()

    def meow(self):
        """
        Meowww.
        """
        print(f"({self.name}) Meow!!!")

    def purr(self):
        """
        To make the cat purr.
        """
        print(f"({self.name}) Mrrrrrr!!!")

    def eat(self, food):
        """
        To make the cat eat. Cats like fish; if you give them a different food, they will reject it.
        
        :param food: The food offered to the cat."
        """
        print(f"({self.name}) ", end="")
        if food == "fish":
            print("Hmmmm :-)")
        else:
            print("I'm sorry, I just eat fish.")

    def fight_with(self, opponent):
        """
        Puts two cats in a fight. Only two males will fight each other.
        :param opponent: The cat to fight against.
        """
        print(f"({self.name}) ", end="")
        if self.sex == "female":
            print("I dont like to fight.")
        elif opponent.sex == "female":
            print("I don't fight against female cats.")
        else:
            print(f"Come here, {opponent.name}, you're going to find out :-@")