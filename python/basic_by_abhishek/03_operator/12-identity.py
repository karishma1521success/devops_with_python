#Identity operator = used to compare the memory locations of two objects if they are same or not

#1. is : Returns True if both operands refer to the same objects
#2. is not: Returns True if both operand refer to different objects

x = [1,2,3]   #list x is reference variable contains memory location
y = x  #now refers to the same object as x

result = x is y    # True


a = "hello"
b = "world"

result = a is not b  # True