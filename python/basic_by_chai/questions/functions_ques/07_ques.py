import sys
# num1 = int(sys.argv[1])   # To take input from enviroment argumenets
# num2 = int(sys.argv[2])   # enviroment input treat as string

# def args(num1, num2):
#     return num1 + num2

# print(args(num1, num2))

#  *args - is used as a parameter where you can take any no. of arguments

def sum_all(*args):
    # print(args)  # (1,2) - tuple 
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3))