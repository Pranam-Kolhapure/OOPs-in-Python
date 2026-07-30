class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting...")

    def stop(self):
        print(f"{self.brand} {self.model} has stopped.")


class Car(Vehicle): #Multiple Inheritance
    def start(self): 
        print(f"{self.brand} {self.model}: Turn the key, engine roars to life.")


class Bike(Vehicle):
    def start(self):#Method overriding
        print(f"{self.brand} {self.model}: Kick-start the engine.")


class Truck(Vehicle):
    def start(self):
        print(f"{self.brand} {self.model}: Heavy diesel engine rumbles awake.")


# Test - polymorphism in action
vehicles = [Car("Toyota", "Corolla"), Bike("Honda", "Shine"), Truck("Volvo", "FH16")]

for v in vehicles:
    v.start()
    v.stop()
    print()

