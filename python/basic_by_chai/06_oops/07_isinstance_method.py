# isinstance() - method is used to find that the object belongs to particual class or not

#parent class
class Car:

    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    
    def fullName(self):
        return f"{self.brand} {self.model}"


# child class
class ElectricCar(Car):
    # so it inherits properties from Car class
    def __init__(self,brand, model, battery):
        super().__init__(brand,model) 
        # inheriting parent class constructor through super method
        # This reduces the code like this.brand , this.model which is already written in parent class
        self.battery = battery


car1 = Car("toyata", "model 1")
print(car1.brand, car1.model)

car2 = ElectricCar("tesla" , "model s", 84)
print(car2.brand, car2.model, car2.battery)

print(isinstance(car1,Car)) 
print(isinstance(car2,Car))  #car2 is an electric car still it is inherited with Car class
# both true
    