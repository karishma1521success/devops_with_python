
#Imp - if variable not found in function then it searches from upper boundary goes to upward checking
# inside to outer

username = "karishma15@"  # global scope

def name():
    username = "sachin15@"  #function scope
    print(username)

print(username)
name()

#changing value of global variable in function using global keyword

def name1():
    global username   #This is bad practicef
    username = "anisha"

print(username)
name1()
print(username)

# global scope can be used anywhere in the code
# function scope used within that function