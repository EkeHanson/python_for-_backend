
#**kwargs is a parameter that will pack all arguements into a dictionary,
#It is useful for a functionthat accepts varying amount of arguements



def greet(**kwargs):
    for key, value in kwargs.items():
        if key == "Nigeria":
            print("You are welcome to Abuja")
        elif key == "Japan":
            print("You are welcome to Tokyo")

greet(Nigeria="Lagos", SouthAfrica="Pretoria")



# The name height and age will be inside a dictionary

# print(f"Hello {first} you are {height}cm tall and {age} years old! Welcome to our class")

# def greet2(**kwargs):
#     firstNmae = kwargs.get("first", "Hanson")
#     user_height = kwargs.get("height", 12.3)
#     user_age = kwargs.get("age", 26)

#     print(f"Hello {firstNmae} you are {user_height}cm tall and {user_age} years old! Welcome to our class")

# greet2(first = "Lawson", height = 23.4, age = 34)

import random

x = random.randint(1, 6)
y = random.randint(1, 6)

# print(f"{x} , {y}")

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

cards = suits + ranks

# print(cards)
random.shuffle(cards)

# print(cards)

my_choice = random.choice(cards)
print(my_choice)