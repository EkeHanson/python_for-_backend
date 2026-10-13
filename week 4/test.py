#Method Chaining
#This is used to call multiple methods sequentially
class Car:
    def turn_on(self):
        print("Yes I started the car")
        return self
    def drive(self):
        print(" I stepped on the accelarator")
        return self
    def brake(self):
        print("Applied the brakes")
        return self
    def turn_off(self):
        print("Finally turned off the car")
        return self


car = Car()

car.turn_on().drive().brake().turn_off()
