class Car:
    def __init__(self, v1, v2):
        self.make = v1
        self.model = v2

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

car1 = Car("Toyota", "Corolla")
car2 = Car(None, None)

print("Car 1 Details:")
print("Make:", car1.get_make())
print("Model:", car1.get_model())

print("\nCar 2 Details (Before Update):")
print("Make:", car2.get_make())
print("Model:", car2.get_model())

car2.set_make("Honda")
car2.set_model("Civic")

print("\nCar 2 Details (After Update):")
print("Make:", car2.get_make())
print("Model:", car2.get_model())