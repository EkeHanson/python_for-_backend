# PROCEDURAL PROGRAMMING
# birth_year = int(input("Please enter the birth  year: "))

# currect_year = 2026

# age = currect_year - birth_year

# print(age)


#FUNCTIONAL PROGRAMING
def even(num):
    if num % 2 ==  0:
        print(f"{num} is an even number")
even(10)

# OOP = Object Oriented Porgramming
# Class = is a blue print for creating entities

class Car:
    def __init__(self, color, model, year, make):
        print("Just created a class")
        self.color = color
        self.model = model
        self.year = year
        self.make = make



    def driving1(self):
        print("I m browsing please")

car1 = Car("red", "Corve", 2026, "chorolet")
car2 = Car("Cyan", "Lancrsuiser", 2018, "toyota")

print(car1.color)
print(car2.color)

car1.driving1()
car2.driving1()