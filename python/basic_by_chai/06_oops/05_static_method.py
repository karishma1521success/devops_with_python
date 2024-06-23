# @staticmethod - called decorator(decorator added more functionality to method)
# It added functionality of making method static (means object cannot be accessed it can only be accesed by class only)
# static methods are callable by class only not by objects



class Student:
    # Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def general_description():
        return "students are intelligent"
    # No 'self' parameter needed because this method does not interact with instance-specific data

# Creating an instance of Student
student1 = Student("karishma", 88)

# Accessing the static method through the instance
print(student1.general_description())  # Outputs: "students are intelligent"

# Accessing the static method through the class
print(Student.general_description())   # Outputs: "students are intelligent"

# both class and instance can accessed static variable here
# In this python version we cannot restrict to access static methods 


    