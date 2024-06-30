# dictionary - unordered list of elements in the form of key value pair
# list has index as key but in dictionary we have value as keys which are defined by yourself
# 1. get(), 2. adding new key-value pair, 3. pop(value) or del dic(key) , 4. popitem()
# Imp - creating dictionary using dict.fromkeys(keysList,valuesList)

players_dict = {"Virat" : "Batter" , "Bhumrah" : "Bowler" , "Rohit" : "Batter" , "Dhoni" : "Batter and wicket Keeper" , "Rishab" : "Batter and wicket Keeper" , "Jadeja" : "All rounder", "Shami" : "Bowler"} 
print(players_dict)
print(len(players_dict)) # return total no. of items

#IMP -----------------------------------------------
# making copy of dictionary
players_dict_copy = players_dict.copy()

# IMP ----------------------------------------------------
# dictionary comprhension
squared_num = {x:x**2 for x in range(6)}
print(squared_num)

# clearing dictionray - clearing/deleting all items just empty dictionary
# dic.clear()
squared_num.clear()
print(squared_num)

# Accesing values using key
print(players_dict["Virat"])
# print(players_dict["sachin"]) # this key is not present so we will get error

#1. get() -- dict.get(value) - accessing values using get method and if key is not present it will not throw error
print(players_dict.get("Rohit"))
print(players_dict.get("sachin")) # key is not present then returns None instead of error

#Printing keys of dictionary
for key in players_dict:
    print(key)

#2. printing key values of dictionary
for key in players_dict:
    print(players_dict[key])

#3. printing key and values of dictionary together
for key in players_dict:
    print(key , players_dict[key])

print("--------------------------------------")
for key, value in players_dict.items():
    print(key,value)

#4.dict[key] = value --> adding new key value pair
players_dict["sachin"] = "Batter"
print(players_dict) 

#5. dict.pop(key) - to remove item having key and its value
players_dict.pop("Shami")
print(players_dict)

del players_dict["Jadeja"] # this is a method to remove key value pair even from memory
print(players_dict)

#6. dict.popitem() - to remove last item of dictionary
players_dict.popitem()
print(players_dict)

#7. Creating dictionary from keys array and value
keys = ["Masala" , "Ginger" , "Lemon"]
Values = ["spicy" , "zesty" , "sour"]
defaultValue = "delicious"

new_dict = dict.fromkeys(keys,Values)
print(new_dict)

new_dict = dict.fromkeys(keys, defaultValue )
print(new_dict)