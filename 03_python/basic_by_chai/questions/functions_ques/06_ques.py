number = int(input("Enter a number: "))

def cube(number):
    return number ** 3

print(cube(number))

# caluclation cube through lambda function
# lambda is used once where as normal function can be used multiple times

cube1 = lambda num: num ** 3
print(cube1(3))