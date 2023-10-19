"""
In this version of the 'PlainCat' class, we replace the use of getters and setters with properties, which is the "Pythonic" way 
of doing it. We add more functionality to the 'birth day' property and create a read-only property that gives us the cat's age.

Date: 7/09/2023.
"""
import datetime

class PlainCat:

    def __init__(self, name, sex, species='', birth_day=datetime.date.today()):
        """
        Constructor for 'PlainCat', requires a name and a sex, which cannot be modified once the object is created.
        Additionally, you can specify a breed and birth date, which can be modified.
        """
        if sex not in ['male', 'female']:
            raise ValueError(f"{sex} is an incorrect sex.")
        self.__name = name
        self.__sex = sex
        self.species = species  # Invoking the setter through the property
        self.birth_day = birth_day

    @property
    def name(self):
        return self.__name

    @property
    def sex(self):
        return self.__sex

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.__species = value.upper()

    @property
    def birth_day(self):
        return self.__birthday

    @birth_day.setter
    def birth_day(self, value):  # Accept both a date and a formatted string as input
        if isinstance(value, datetime.date):
            self.__birthday = value
        elif isinstance(value, str):  # Formatted date string that we convert to datetime.date
            self.__birthday = datetime.datetime.strptime(value, "%d/%m/%Y").date()
        else:
            raise TypeError(f"{value} is not an instance of datetime.date")

    @property
    def age(self):
        age_cat = datetime.date.today().year - self.birth_day.year
        if not self.__has_a_birthday_this_year():
            age_cat -= 1
        return age_cat

    def __has_a_birthday_this_year(self):
        today = datetime.date.today()
        if today.month > self.birth_day.month:
            return True
        if today.month == self.birth_day.month and today.day >= self.birth_day.day:
            return True
        return False

    def meow(self):
        print(f"({self.name}) Meowww!!!")

    def purr(self):
        print(f"({self.name}) Mrrrrrr!!!")

    def eat(self, food):
        """
        Makes the cat eat. Cats like fish; if you give them something else, they will reject it.
        """
        print(f"({self.name}) ", end="")
        if food == "fish":
            print("Hmmmm, thanks :-)")
        else:
            print("Sorry, I only eat fish.")

    def fight_with(self, opponent):
        """
        Makes two cats fight. Only two males will fight each other.
        """
        print(f"({self.name}) ", end="")
        if self.sex == "female":
            print("I don't like to fight.")
        elif opponent.sex == "female":
            print("I don't fight against kitties.")
        else:
            print(f"Come here, {opponent.name}, you're in for it :-@")

