# The Four Pillars of Object-Oriented Programming (OOP)
class Car:  #Template for creating an object
    wheel = 4
    doors = 4
    #Methods
    def start(self):
        print("I trun the key to start")

    def stop(self):
        print("I step on the brakes to stop")
ford = Car() #Instances of the class
toyota = Car()

print(ford.wheel)
print(ford.doors)
print(ford.stop())



# Inheritance – Creating a new class (child) based on an existing class (parent) 
# to reuse code and establish relationships.

# Abstraction – Hiding complex implementation details and showing only the essential features.

# Polymorphism – The ability of objects of different types to respond 
# to the same interface or method call in their own way.

# Encapsulation – Bundling data and methods that operate
#  on that data within a single unit (class) and restricting direct access to some components.

# Quick Definitions
# Concept	What it means
# Abstraction	Hiding complexity; you interact with a simplified interface.
#  Example: pressing "Start" on a car without knowing how the engine works.
# Inheritance	"Is-a" relationship. Example: Car inherits from Vehicle. Child classes reuse parent methods/fields.
# Polymorphism	"Many forms." Example: A draw() method behaves differently for Circle, Square, and Triangle.
# Encapsulation	Data hiding. Keeps internal state private and exposes only necessary methods via getters/setters.

class Animal():
    alive = True

    def eat(self):
        print("All animals eat")

    def sleep(slef):
        print("All Animals Sleep!")

class Rabbit(Animal):
    pass

rabbit = Rabbit()
rabbit.eat()
rabbit.sleep()

if rabbit.alive:
    print("The rabbit is alive!")


# # Demonstrate the inheriance concept
# # with python code using Car, Keke,
# # Bicycle and Vehicle
# # also implement methods like brake, speed and 
# # variables like number of doors, number of tyres etc


# class Vehicle():
#     num_of_tyres = 4
#     def brake(self):
#         print("I just applied the brake")
#     def speed(self):
#         print("Overspeeding is not allowed")

# class Car(Vehicle):
#     pass
# class Keke(Vehicle):
#     pass
# class Bicycle(Vehicle):
#     num_of_tyres = 2

# car = Car()
# keke = Keke()
# bicycle = Bicycle()

# car.speed()
# car.brake()
# print(car.num_of_tyres)

# keke.speed()
# keke.brake()
# print(keke.num_of_tyres)

# bicycle.speed()
# bicycle.brake()
# print(bicycle.num_of_tyres)


#Multi-level Inheriance: when a drerived (child)
#class inherit form another derived class

# class Organism:
#     plant_animal = True
#     alive  = True


# class Animal(Organism):
#     def eat(self):
#         print("Every Animal will eat")


# class Dog(Animal):
#     def bark(self):
#         print("Every dog should bark")


# dog = Dog()

# print(dog.plant_animal)
# dog.eat() 
# dog.bark() 



#Multiple Inheriance=> when a child class 
#is derieved from more than one parent classes
class Predator():
    def hunt(self):
        print("This animal hunts for a living")
class Prey():
    def flee(self):
        print("This animal always flees for its life")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Predator, Prey):
    pass
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()

fish.flee()
fish.hunt()

#Method Overriding
#This is an ability of OOP to allow a child class provide its own specific
#  implementation of a method already implemented in one of its parent class

class House:
    def __init__(self, name, no_doors): #Constructor
        print("House created")
        self.name = name
        self.no_doors = no_doors

    def purpose(self):
        print("This is the house of God")
    
    def proximity(self):
        print("This is the close to Asorock")
    
class Duplex(House):
  def purpose(self):
        print("This is my personal residential house")
    

duplex = Duplex("My Duplex", 10)
duplex.purpose()



#Method Chaining
#This is used to call multiple methods sequentially
class Car:
    def turn_on(self):
        print("Yes I started the car")
    def drive(self):
        print(" I stepped on the accelarator")
    def brake(self):
        print("Applied the brakes")
    def turn_off(self):
        print("Finally turned off the car")


car = Car()

car.turn_on().drive().brake().turn_off()





class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start(self):
        return f"{self.brand} engine started first in {self.year}"

#The self keyword is refering 
#to the particular object calling the method
car1 = Vehicle("Corvet", "2026")
car2 = Vehicle("Camry", "2021")

print(car1.start())
print(car2.start())



#Procedural Programming
current_year = 2026
birth_year = 2004
age = current_year - birth_year
# print(age)

#Functional programming
def calc_age(birth_year, current_year):
    age = current_year - birth_year
    return age
# print(calc_age(2004, 2026))



# Class	A blueprint or template (e.g., "Student")

# Object	A specific instance built from that blueprint (e.g., boma, friday)

# Attribute	Data stored inside the object (self.name, self.grade)

# Method	A function defined inside a class that acts on
# the object (is_passing())

# self	A reference to "this particular object"

# __init__	The setup function that runs when you create an object



#OOP => Object Oriented Programming
#CLASS =>Is the blueprint that will decsribe ow objected are created
class Student:
    def __init__(self, name, age, grade):
        # print("Hello World")
        self.name = name
        self.age = age
        self.grade = grade
    def is_passing(self):
        return self.grade >= 50
boma = Student("Boma Emmanuel", 21, 86)
friday = Student("Friday Gauis", 17, 35)
print(boma.is_passing())
print(boma.name)
print(friday.name)
print(friday.is_passing())
# Class Work
# Create a class called Book with the following: Attributes: title, author, pages
# A method called is_long() that returns True if the book
#  has more than 300 pages, otherwise False
# Then create two objects from the class and test them:
# book1 = Book("Things Fall Apart", "Chinua Achebe", 209)
# book2 = Book("Half of a Yellow Sun", "Chimamanda Ngozi Adichie", 433)
# print(book1.is_long())   # Expected: False
# print(book2.is_long()) 


#THE 4 PILLARS OF OOP
# 1.Inheritance
# 2.Encapsulation
# 3.Abstraction
# 4.Polymorphism


class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    pass

# rabbit = Rabbit()

# print(rabbit.alive)

# rabbit.eat()
# rabbit.sleep()

# There are two types of Inheritance
# 1. Multi-level
# 2. Multiple

class Organism:
    alive = True

class Animal(Organism):
    is_animal = True
    is_plant = False

    def is_mammal(self):
        print("This organism is a mammal")

class Dog(Animal):
    def bark(self):
        print("The dog barks")

dog = Dog()

# print(dog.alive)
# dog.is_mammal()
# dog.bark()

#MULTIPLE Inheritance
# => This occurs when a child class 
# derived from more than one parent class

class Prey:
    def flee(self):
        print("The animal fless")

class Predator:        
    def hunt(self):
        print("The animal hunts")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass
# rabbit = Rabbit()
# hawk = Hawk()
# shark = Fish()
# rabbit.flee()
# hawk.hunt()
# shark.flee()
# shark.hunt()




#                     Class Work
# Using multiple inheritance, create the following:

# A class Father with a method speak() that prints "Father speaks"

# A class Mother with a method cook() that prints "Mother cooks"

# A class Child that inherits from both Father and Mother

# Then create a Child object and call both methods on it.

# python
# child = Child()
# child.speak()   # Expected: Father speaks
# child.cook()    # Expected: Mother cooks

#DEALING    with the super function
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        return self.length * self.width 
class Cube(Rectangle):
    def __init__(self, length, width, height):
        self.height = height
        super().__init__(length, width)
    def volume(self):
        return self.length * self.width * self.height

square = Square(3,4)
cube = Cube(3,4,5)

print(square.area())
print(cube.volume())












def __init__(self, length, width):
    # self.length = length
    # self.width = width
    super().__init__(length, width)
def area(self):
    return self.length * self.width 
class Cube(Rectangle):
def __init__(self, length, width, height):
    self.height = height
    super().__init__(length, width)
def volume(self):
    return self.length * self.width * self.height

square = Square(3,4)
cube = Cube(3,4,5)
print(square.area())
print(cube.volume())




#                 Class Work 
# Create the following:

# A parent class Person with __init__ that stores name and age

# A child class Student that:

# Uses super().__init__() to set name and age

# Adds its own attribute course

# Has a method intro() that prints "My name is <name>, I am <age> and I study <course>"

# Then create one Student object and call intro().

# python
# s = Student("Ada", 20, "Python")
# s.intro()
# # Expected: My name is Ada, I am 20 and I study Python


