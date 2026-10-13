class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Cow:
    def speak(self):
        print("Moo!")

# Same call — different behavior
for animal in [Dog(), Cat(), Cow()]:
    animal.speak()

# Output:
# Woof!
# Meow!
# Moo!

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: {shape.area()}")

# Output:
# Circle: 78.5
# Square: 16

# Without polymorphism — messy
for item in items:
    if item.type == "circle":
        print(3.14 * item.r ** 2)
    elif item.type == "square":
        print(item.side ** 2)
    elif item.type == "triangle":
        print(0.5 * item.b * item.h)

# With polymorphism — clean
for shape in shapes:
    print(shape.area())





class Card:
    def pay(self):
        print("Paid with Card")

class Cash:
    def pay(self):
        print("Paid with Cash")

class Transfer:
    def pay(self):
        print("Paid via Transfer")

# Your turn:
# payments = [Card(), Cash(), Transfer()]
# for p in payments:
#     p.pay()