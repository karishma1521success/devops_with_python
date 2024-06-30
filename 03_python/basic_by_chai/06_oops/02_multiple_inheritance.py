# multiple inheritance - means one class inherits more than one class
# parent class - more than one

class Battery:
    def __init__(self,battery):
        self.battery = battery
        print("battery is superb")
    
    def battery_print():
        print("good quality battery")


class Engine:
    def __init__(self):
        print("engine is superb")
    
    def engine_print():
        print("good quality engine")
    
class ElectricCar(Battery,Engine):
    def __init__(self, brand, model, battery):
        super().__init__(battery)
        self.brand = brand
        self.model = model

tesla_car = ElectricCar("tesla", "model1", 84)
tesla_car.battery_print()
tesla_car.engine_print()



