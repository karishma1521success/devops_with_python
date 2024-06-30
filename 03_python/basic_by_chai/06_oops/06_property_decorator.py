#Imp - any attriube with __attirubteName it can be accessed through its method not with its attribute name
# __attribute - means you make that encapuslate and added method for it to make avaiable

class Car:

    def __init__(self,brand, model):
        self.brand = brand
        self.__model = model 
        # to make any attribute read only using property decorator
            #1. add __ before attribute name
            #2.  add @property decorator before method
            #3. add method with same name as attribute but without __
            #4.model attriubte can only accessed by model method not with attribute name


    @property
    # used so that no one can overwrite and gives no access of setter
    def model(self):
        return self.__model
        
# now you cannot override model attribute by adding __ and @property decorator
car1 = Car("toyota" , "model1")
print(car1.brand)
print(car1.model)
# car1.model = "model2" # this will throw error because model attribute is read only

# TypeError: 'str' object is not callable - means model can be accessed as property not as method
# car1.model - like this   car1.model()- not this