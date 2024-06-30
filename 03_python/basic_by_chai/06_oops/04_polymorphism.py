# polymorphism is many forms
# having same method but functionality is different
# same method name but it functions differently in many form
# both class has same fuel_type() method but have different functions

# parent class
class Car:
    total_cars = 0  # class variable

    def __init__(self,brand, model):
        self.__brand = brand    
        self.model = model
        Car.total_cars += 1  # accessing class variable using class name not self within class
        
    def fuel_type(self):
        return "diesel and petrol"
   
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
    
    def fuel_type(self):
        return "Electric charge"
    
# as you can see both class has fuel_type method but both have different behaviours.

car1 = Car("porshe" ,"model1")
print(car1.fuel_type())

car2 = ElectricCar("tesla", "modelS" , 84)
print(car2.fuel_type())

# accesing class variable
# to access class variable accessed by class name not through object
print(Car.total_cars)

