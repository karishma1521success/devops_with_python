# create class
class Car:
    brand = "porshe"
    model = 1
#but above class is taking value itself 
#It's not taking from user
#create object
car1 = Car()
print(car1.brand , car1.model)

class Car_structure:
    def __init__(self, brand, model):
        self.brand = brand   # self - this 
        self.model = model   # this.brand, this.model tell it is attriubtes of class

# __init__ is like a constructure method which is called automatically when object is constructed


# object giving its own input
car2 = Car_structure("Toyota", 2020)
print(car2.brand, car2.model)
