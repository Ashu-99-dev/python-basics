class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

class Fortuner(ToyotaCar):
    def __init__(self, name, type):  # Accept both name and type
        super().__init__(name)  # Call parent's __init__ to set name
        self.type = type
    

car1 = Fortuner("Fortuner", "4x4")  # Pass both name and type

print(car1.name, car1.type)   # Now this works! Inherited from ToyotaCar
car1.start()
car1.stop()