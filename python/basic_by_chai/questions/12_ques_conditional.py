# To get the age input from user
# 1. question 1. Age Group Categorization   --Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
age = int(input("Enter your age: "))

if age < 13 :
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("senior")


#2. Question  Movie Ticket Pricing    Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
from datetime import date
age = int(input("Enter your age to watch a movie: "))
price = 0

# # first we check is today a wednesday or not?
today = date.today()

if today.weekday() == 2:  # means wednesday
    if age >=18:
        price = 10
    else:
        price = 6
else:
    # the day is not wednesday.
    if age >= 18:
        price = 12
    else:
        price = 8

print("The cost of the movie ticket is ", price)


#3.Grade Calculator   Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

studentScore = int(input("Enter a student score: "))

if studentScore >= 90:
    print("A")
elif studentScore >= 80:
    print("B")
elif studentScore >= 70:
    print("C")
elif studentScore >=60:
    print("D")
else:
    print("F")
    

#4. Fruit Ripeness Checker   Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

colour = input("What is the color of the banana: ")

if colour == "Green":
    print("Unripe")
elif colour == "Yellow":
    print("Ripe")
elif colour == "Brown":
    print("Overripe")
else: 
    print("You entered wrong colour")


# 8. Password Strength Checker   Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter your password")

lengthOfPassword = len(password)

if lengthOfPassword < 6:
    print("Your password is weak")
elif lengthOfPassword <=10:
    print("Your password is Medium")
else:
    print("Your password is strong. You are ready to go !!!")

#9. Leap Year Checker    Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400)
 
year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 != 0:
        #divisible by 4 and not by 100
        print("year" , year , "is a leap year")
    elif year % 400 == 0:
        # divisible by 4 and divisible by 100 then it must be divisible by 400
        print("year " ,year, "is a leap year" )
    else:
        print("year ", year, "is not a leap year")
else:
    print("year ", year, "is not a leap year")