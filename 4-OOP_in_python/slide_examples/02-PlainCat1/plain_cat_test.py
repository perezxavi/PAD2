"""
Test of the PlainCat class.
"""
from plain_cat import PlainCat

garfield = PlainCat("Garfield", "male")
print("Hello, kitty!!!")
garfield.meow()
print("Here's some cake.")
garfield.eat("black forest cake")
print("Here's some fish, let's see if you like this.")
garfield.eat("fish")

tom = PlainCat("Tom", "male")
print(f"{tom.name}, here's some vegetable soup.")
tom.eat("vegetable soup")

lisa = PlainCat("Lisa", "female")

print("Kitties, let's see how you meow.")
garfield.meow()
tom.meow()
lisa.meow()

print("Kitties, have a fight without hurting each other.")
garfield.fight_with(lisa)
lisa.fight_with(tom)
tom.fight_with(garfield)