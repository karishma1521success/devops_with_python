# Functions - Functions is a block of code that return the specific task.
# It only runs when it called

#syntax
def add(a,b):
    return a + b

#calling a function 
addition = add(2,3)
print(addition)

#returning multiple values
def stats(a,b):
    add = a+b
    mul = a*b
    return add , mul

addition1 , multiplication1 = stats(3,4)
print(addition1, multiplication1)

# Lambda function - function which has no name (anonymys)
# used only one time

square = lambda num: num ** 2
print(square(2))

# *args - used as a paramter where you can paas anyy no. of arguments
# print(args) - return tuple of passed arguments
def sum_all(*args):
    print(args)
    return sum(args)

# **kwargs - is used as a parameter where you can pass any no. of arguments in the form of key value pair
def print_all(**kwargs):
    print(kwargs)  # returns dictionary
    for key, value in kwargs.items():
        print("Key: " , key , " Value: ", value)

print_all(name = "karishma" , age = 12)
print_all(name = "Sachin", age= 22 , gender = "Male" )


# yield keyword - it returns the value and it also stores the state of function so that it can recontinue where it left

# recursive function - function which calls itself
# should have base value
# faith


