# The Four Pillars of Object-Oriented Programming (OOP)


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

# class Animal():
#     alive = True

#     def eat(self):
#         print("All animals eat")

#     def sleep(slef):
#         print("All Animals Sleep!")


# class Rabbit(Animal):
#     pass

# rabbit = Rabbit()
# rabbit.eat()
# rabbit.sleep()

# if rabbit.alive:
#     print("The rabbit is alive!")


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

# class Predator():
#     def hunt(self):
#         print("This animal hunts for a living")

# class Prey():
#     def flee(self):
#         print("This animal always flees for its life")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Predator, Prey):
#     pass
    
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# rabbit.flee()
# hawk.hunt()

# fish.flee()
# fish.hunt()

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

