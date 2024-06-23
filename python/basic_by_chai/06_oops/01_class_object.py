# class - it is like a blueprint or object constructor for creating objects/instances
# syntax
class MyClass:
    total_objects = 0   # class variable
    # __init__() - constructor it is called when object is created
    def __init__(self, name, marks):
        # self is like this which is used to establish line b/w obj and class
        self.name = name  # self.name tells name is an attribute of class
        self.marks = marks
        #name and marks are the attributes of class
        MyClass.total_objects += 1

    # method of class
    def full_name(self):
        return f"{self.name} {self.marks}"

# object - instance of a class
obj1 = MyClass("karishma" , 57)
print(obj1.name)

print(obj1.full_name()) # this give an error becuase you have add self keyword to the method
# so object cant access any methods without having self in method as a parameter

print(MyClass.total_objects)
