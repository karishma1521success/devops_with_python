#1. 
 
# Input a list
# list = []
# n = int(input("Enter number of elements: "))

# for i in range(n):
#     ele = int(input())
#     list.append(ele)

# total_positive_element = 0

# # print total elements which are positive
# for element in list:
#     if element > 0:
#         total_positive_element += 1

# print(total_positive_element)
    

#2. Sum of Even Numbers   Problem: Calculate the sum of even numbers up to a given number n.

# number = int(input("Enter the number: "))
# sum = 0
# for i in range(number+1):
#     if i % 2 == 0:
#         sum  = sum + i


# print(sum)

# 3. Multiplication Table Printer   Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# number = int(input("Enter the number: "))

# for i in range(1,11):
#     if(i == 5):
#         continue
#     else:
#         print(number, " * ", i , " = ", (number*i))



#4. everse a String   Problem: Reverse a string using a loop

# str1 = input("Enter any string here that you want to reversed: ")

# length_of_str1 = len(str1)
# reverse_str = ""
 
# index = length_of_str1 -1
# while index >= 0:
#     char = str1[index]
#     reverse_str = reverse_str + char
#     index = index -1

# print(reverse_str)



# 5. Find the First Non-Repeated Character   Problem: Given a string, find the first non-repeated character.

# str2 = input("Enter the string over here: ")
# length_of_str2 = len(str2)


# for index in range(length_of_str2):
#     #check this character is non-repeated char or not
#     non_repeat_char = True
#     character = str2[index]
#     for j in range(length_of_str2):
#         if character == str2[j] and index != j:
#             non_repeat_char = False
#             break

#     if non_repeat_char == True:
#         print(character)
#         break


# 6. Factorial Calculator   Problem: Compute the factorial of a number using a while loop.

# number = int(input("Enter a number to calculate factorial"))
# fact = 1
# i = 1
# while i <= number:
#     fact = fact * i
#     i = i + 1

# print(fact)

#7. Validate :Input   Problem: Keep asking the user for input until they enter a number between 1 and 10.

# while (True):
#     number = int(input("Enter number b/w 1 to 10 : "))
#     if number>=1 and number<=10:
#         print("Valid number" , number)
#         break
#     else:
#         print("Enter valid number, try again")


#8. check if number is prime

# number = int(input("Enter a number: "))

# is_prime = True

# if number >1:
#     for i in range(2,(number//2)+1):
#         if (number % i) == 0:
#             is_prime = False
#             break;

# if is_prime==True:
#     print("prime number")
# else: 
#     print("non - prime number") 

#9. Remove duplicate items in list
# items = ["apple" , "banana" , "orange" , "apple" , "mango"]

#first create empty set
# unique_item = set()

# for item in items:
#     if item in unique_item:
#         # item is already present in unique_item set
#         print("Duplicate item")
#         break
#     unique_item.add(item)

