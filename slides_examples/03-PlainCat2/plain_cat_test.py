"""
Test of the PlainCat class.

Date: 8/09/2023.
"""
import datetime
from plain_cat import PlainCat

garfield = PlainCat("Garfield", "male", "Siamese", datetime.date(2020, 10, 10))
print("Hello, kitty!!!")
garfield.meow()
print("Here's some cake.")
garfield.eat("black forest cake")
print("Here's some fish; let's see if you like this.")
garfield.eat("fish")

tom = PlainCat("Tom", "male", "Roman")
tom.set_birth_day(datetime.date(2018, 11, 2))
print(f"{tom.get_name()}, have some vegetable soup.")
tom.eat("vegetable soup")

lisa = PlainCat("Lisa", "female")

print("Kitties, let's hear how you meow.")
garfield.meow()
tom.meow()
lisa.meow()

print("Kitties, have a playfight without hurting each other.")
garfield.fight_with(lisa)
lisa.fight_with(tom)
tom.fight_with(garfield)

