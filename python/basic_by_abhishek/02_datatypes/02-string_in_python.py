#String - It is a combination of characters 
name = "karishma gupta"   # name - string variables
print(name + " " + str(type(name)))

#String concatenation - adding/ combining two string
str1 = "Hello"
str2 = "World"
result = str1 + str2
print(result)
result = str1 + " " + str2
print(result)

#String methods  // string in-built functions // string handling function

print(len(name));                   #1. To get the total length of the string
print(name.upper())                 #4. Make all the character upper case
print(name.lower())                 #5. Make all the characters lower case
print(name.capitalize())            #3. make the first letter capital
print(name.replace('a', '@'))       #9. replace the character
print(name.find('a'))               #2. to find the first position index of character a
print(name.isdigit())               #6. Check if the string contains only digits or not name = "123"
print(name.isalpha())               #7. Check if the string contains only alphabets means no digits and no space.
print(name.count('a'))              #8. To count the frequence of given character

print(name*3)                       #10. print the name 3 times

#Imp - 
#1. split built -in method
strName = "My name is sachin jain"
words = strName.split(" ")   # spliting by space so words contains list of words
print(words)   #list -- words = ['My' , 'name' , 'is' , 'sachin' , 'jain']

#2. strip()- remove leading and trailing spaces from string (spaces before and after string)
text = "     Heyyy I am converted stripped string      "
print(text.strip())


#3. substring -   check if substring present or not
#syntax   if substring in string:  print(True)
text2 = "I love cricket"
substring = "love"

if substring in text2:
    print("yes substring " + substring + " is present in string " + text2)
else:
    print("substring" + substring+ " is not present in string " + text2)

print("completed out of if else-- identation matters in python")




            
