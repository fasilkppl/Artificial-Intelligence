class vehicle:
    def generic_behaviour(self):
        print("im the parent - vehicle")
    
class Car(vehicle):
    def __init__(self, wheels, colour):
        self.wheels = wheels
        self.colour = colour
        print(f"no of Wheels : {wheels}")
        print(f"Colour : {colour}")

    def specific_behaviour_car(self):
        print("inside Car")
        
class Bike(vehicle):
    def __init__(self):
        self.wheels = 2
        self.colour = "red"

    def specific_behaviour_bike(self):
        carobj.generic_behaviour() #accessing parent function with car object and bike object inside child Bike.
        bikeobj.generic_behaviour()
        carobj.specific_behaviour_car()
        print("inside BiKe")
        
        '''
carobj is an instance of Car.

Python “knows” that carobj has all the methods defined in Car (and any parent class Car inherits from).

So, anywhere you have access to carobj, you can call:

carobj.specific_behaviour_car()
carobj.generic_behaviour()  # inherited from Vehicle

Even if you’re inside a Bike method, as long as you have the reference carobj, Python allows you to call its methods.
'''

if __name__ == "__main__":
    carobj = Car(4, "Black")
    carobj.generic_behaviour()# generic_behaviour is a function in vehicle parent class and can be accessed by object of child class.
    carobj.specific_behaviour_car()
    
    bikeobj = Bike()
    bikeobj.specific_behaviour_bike()
    
        