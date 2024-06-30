# use import sys - to use command line arguments 
# This file shows how to take inputs from command linee 
import sys

#function that take 3 parameters and return the sum of two values
def addition(num1, num2):
    return num1+num2

def subtraction(num1, num2):
    return num1-num2

def multiplication(num1, num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

#command line args must be in this format   num1 operation num2   (operation = add, sub, mul, div)
num1 = float(sys.argv[1])     #sys.argv[1]  give first agrument given by user in command line 
operation = sys.argv[2]       #sys.argv[1], sys.argv[2], sys.argv[3] return string.
num2 = float(sys.argv[3])

if operation == "add":
    add = addition(num1,num2)
    print("The sum of two values are: " + str(add) )
elif operation == "sub":
    sub = subtraction(num1, num2)
    print("The sub of two value are " + str(sub) )
elif operation == "mul":
    mul = multiplication(num1, num2)
    print("The mul of two values are " + str(mul))
elif operation == "div":
    div = division(num1, num2)
    print("The division of two value are " + str(div))
else:
    print("You have entered the wrong operation")

