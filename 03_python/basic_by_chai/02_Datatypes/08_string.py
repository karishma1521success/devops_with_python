# string - It is combination of characters. Strings can be created using single, double or triple quotes. 
# Immutable
# python does not have a character data type 
# 'a' also treat as a string of length 1
# string has both positive and negative indexing.

team = "India"
print(team)
print(type(team)) 

# ACCESSING CHARACTER
first_char = team[0]   # Indexing starts from 0 
print(first_char)
last_char = team[-1]
print(last_char)
# it can have negative index starting from -1 at the end of the string

# LENGTH OF STRING
print(len(team))   # len(str)

# methods in strings

#1. slicing - str[startIndex : endIndex]  - used to access a range of characters in the string.  End index exclude
# means substring of the original string
print(team[0:3])
print(team[-6:-2])

print(team[:]) # return whole string
print(team[3:]) # return substring from index 3 to end index
print(team[:2])  # return substring from 0 to index 1 
# IMP
print(team[0:5:2]) # return substring containing every 2nd character including 0
# Every 2nd character

# 2. strip() -- str.strip() - to remove extra spaces in string at the start and end
player = "    Virat kholi     "
print(player.strip())

#3. replace() - str.replace(str1, str2) 
print(player.replace('Virat', 'Anushka'))

# 4. split() - str.split("splitter") - convert string into the list
cricketerNames = "Virat, Rohit, Shubham, Dhoni"
cricketerNamesList = cricketerNames.split(", ")
print(cricketerNamesList) 

#5. find() = str.find("string") - find string or character in string
player = "Virat Kholi"
print(player.find("Virat"))  # RETURN -1 IF NOT FOUND

#6. count() - str.count(string) -- return the count that string is present in original string
print(player.count("i"))

#7.  "".join(list) -  list into string
list1 = ["hey", "I" , "am"]
print(" ".join(list1))


# printing each character of the string
for character in player:
    print(character)

# raw string
chai = r"Masala\nchai"
print(chai)

# find string in string
print("Kholi" in player)