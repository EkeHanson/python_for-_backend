from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        """Every vehicle must
          implement how to start
            its engine."""
        pass
    
    @abstractmethod
    def stop_engine(self):
        """Every vehicle must
          implement how to stop 
          its engine."""
        pass
    
    def honk(self):
        """A concrete method
          available to all vehicles."""
        print("Beep beep!")


# Concrete subclass
class Car(Vehicle):
    
    def start_engine(self):
        print("Car engine started with a key turn.")
    
    def stop_engine(self):
        print("Car engine stopped.")


# Another concrete subclass
class ElectricCar(Vehicle):
    
    def start_engine(self):
        print("Electric car motor activated silently.")
    
    def stop_engine(self):
        print("Electric car motor deactivated.")


# Using the abstractions
def operate_vehicle(vehicle: Vehicle):
    vehicle.start_engine()
    vehicle.honk()
    vehicle.stop_engine()

car = Car()
ev = ElectricCar()

operate_vehicle(car)
operate_vehicle(ev)




# docstring

name = "Philip"

sentence = """Philip hsdbsdj sdhfvbsfdhivk
                         sdchsdbvk 
    hdbvhvch hsdbhsdfvbhds sdhjbvsdhjkvb"""