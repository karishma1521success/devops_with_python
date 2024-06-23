# encapsulation - It describes the idea of wrapping data and the methods that work on data within one unit.
# encapsulate make attributes private and object can accessed that attribute using method only

# parent class
class Car:

    def __init__(self,brand, model):
        self.__brand = brand    
        self.model = model
        # to encapsulate anything add __before attribute name 
        # self.__brand is encapsulate means private it cannot be accessed by objects through attribute name
        # It can be accessed using get method
    
    # to accessed encapsulate brand attribute by object
    def get_brand(self):
        return self.__brand

    def fullName(self):
        return f"{self.__brand} {self.model}"



# child class
class ElectricCar(Car):
    # so it inherits properties from Car class
    def __init__(self,brand, model, battery):
        super().__init__(brand,model) 
        # inheriting parent class constructor through super method
        # This reduces the code like this.brand , this.model which is already written in parent class
        self.battery = battery

car2 = ElectricCar("tesla" , "model s", 84)
print(car2.get_brand(), car2.model, car2.battery)
# accessing brand keyword using get method

