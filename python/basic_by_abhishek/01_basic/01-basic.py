#printing, variables, type() function , type casting

#Python - It is a high- level language.        Loosely typed language(don't need to tell what type of data you will stored in variable)

#To check the python is installed or not
#Run command in terminal - python --version  - windows
#                          python3 --version - macos and linux

# Printing in Python
print("hello world")


#VARIABLES
name = "Karishma Gupta"        #String
age = 21                       #Int
isFemale = True                #Boolean
height =  4.11                 #Float

#Multiple assignments - python allows us to assgin multiple variables at the same time in one line of code.
name, age, isFemale, height = "Sachin jain" , 22, False, 5.3

sbirthYear = kBirthYear = 2002  # if multiple variable has same value
print(sbirthYear)


#To know the type of variable -   type(variable)
print(type(age))


#Type casting is needed to concatenate the different datatypes
print("My name is " + name + " and my age is " + str(age) + " also I am a " +
"female and my height is " + str(height));
