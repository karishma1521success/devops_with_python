#2. Create a function that takes two numbers as parameters and returns their sum.
num1, num2 = input("Enter two numbers: ").split()
num1, num2 = int(num1) , int(num2)

def sum(num1, num2):
    return num1 + num2

sum = sum(num1, num2)
print(sum)