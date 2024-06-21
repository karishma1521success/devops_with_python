# number - float, integer, complex number

num1 = 15
num2 = 5

add = num1 + num2    # add , sub, mul works same as in mathematics
sub = num1 - num2  
mul = num1 * num2
div = num1 / num2
div = num1 // num2   # float div - / (return float result)     int div = //  (return integer result) 
rem = num1 % num2    # gives remainder
power = num2 ** 2    # gives power  num2 ki power 2
print(add)
print(sub)
print(mul)
print(div)
print(rem)
print(power)
c = num1, num2
print(c)    # (15,5)  - tuple

#Note : In any operation for good practice make sure both operands must be of same data type
#   like int + int     float + float      (int + float (not good practice))

result = (num1 + num2) * num1     # if there is more than one operator in single expression it's good to use brackets
print(result)

# for type casting python has in built function like int(), float(), str()
#### Note : operator overloading - an operator has many functions like + treat as addition and also concatenation

# Built in methods 
# 1. abs() - absolute value 
a = -5
print(abs(a))   #5

# 2. round() - round value    parameters - integer, round upto digit
b = 3.14544
print(round(b,2))   #3.15

# == check value   and is check data type
# True == 1  True
# True is 1  False

# False == 0 True
# False is 0 False
