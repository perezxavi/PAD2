"""
In this version of the 'Simple Cat' class, we solve the problems from the previous example by creating "private" attributes
and we will use getters and setters to access and modify them.

The use of getters and setters as presented here is not the "Pythonic" way to do it; this will be implemented in the
next version.

Date: 7/09/2023.
"""
import datetime

class PlainCat:

    def __init__(self, name, sex, species='', birth_day=datetime.date.today()):
        """
        Constructor for 'Simple Cat', requires a name and a sex, which cannot be modified once the object is created.
        Additionally, you can specify a breed and birth date, which can be modified.
        """
        if sex not in ['male', 'female']:
            raise ValueError(f"{sex} is an incorrect sex.")
        self.__name = name
        self.__sex = sex
        self.set_species(species)
        self.set_birth_day(birth_day)

    def get_name(self):
        return self.__name

    def get_sex(self):
        return self.__sex

    def get_species(self):
        return self.__species

    def set_species(self, value):
        self.__species = value.upper()

    def get_birth_day(self):
        return self.__birth_day

    def set_birth_day(self, value):
        if not isinstance(value, datetime.date):
            raise TypeError(f"{value} is not an instance of datetime.date")
        self.__birth_day = value

    def meow(self):
        print(f"({self.__name}) Miauuuu!!!")

    def purr(self):
        print(f"({self.__name}) Mrrrrrr!!!")

    def eat(self, food):
        """
        Makes the cat eat. Cats like fish; if you give them something else, they will reject it.
        """
        print(f"({self.__name}) ", end="")
        if food == "fish":
            print("Hmmmm, thanks :-)")
        else:
            print("Sorry, I only eat fish.")

    def fight_with(self, opponent):
        """
        Makes two cats fight. Only two males will fight each other.
        """
        print(f"({self.__name}) ", end="")
        if self.__sex == "female":
            print("I don't like to fight.")
        elif opponent.__sex == "female":
            print("I don't fight against kitties.")
        else:
            print(f"Come here, {opponent.__name}, you're in for it :-@")

