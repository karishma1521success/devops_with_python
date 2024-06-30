# rescursive function to calculate factorial of a number

number = int(input("Enter a number: "))

def factorial(number):
    if number == 1:
        return 1  # because factorial of number 1 is 1
    
    return number * factorial(number-1)

print(factorial(number))