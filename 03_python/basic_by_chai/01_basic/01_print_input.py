# Imp - first value allocates in memory then its variable give reference to it


print("chai aur python")

def chai(n):
    print(n)

chai("lemon chai")

list = ["hey" , "how" , "are" , "you?"]
# printing
for word in list:
    # print(word) # but this print each word in next line
    # want to print each word in same line
    print(word, end = " ") #through end we print in same line cursor will not go to the next line
    # print(word, end = "-")

    
#input("message") =  Taking inputs in python
# input() method return value in string
num = int(input("Enter a number"))

#Taking multiple inputs in python
a, b = input("Enter two number: ").split()
# a, b is string convert to num using num()
a, b = int(a), int(b)
print(a,b)
