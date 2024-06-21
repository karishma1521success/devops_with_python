# list is a mutable data type
players_list = ["Virat" , "Sachin" , "Rohit" , "Shubhman"]
print(players_list)

# Accessing an element of the list
print(players_list[0]) # can also access throught negative index

# print all elements of a list
for player in players_list:
    print(player)

# length of list ---->>   len(list)
print(len(players_list))


#IMP ------------------------------------------------------
# list comprehension
squared_num = [x**2 for x in range(10)]
print(squared_num)

##IMP ---------------------------------------------------------------------------------
players_list_copy = players_list # here both has same data and reference too. 
# if we change players list then automatically players_list_copy also get changed and viceversa becasue both are pointing to the same data
players_list_copy = players_list.copy() # here both has same data as of now but having different reference in memory
# changing one list will not affect other list becuase both have different reference address in memory


#1. append() - list.append(Value) - add value at the last
players_list.append("Dhoni")
players_list.append("Jadeja")
players_list.append("Bhumrah")
print(players_list)

#2. pop() -- list.pop() - remove last element
players_list.pop()
print(players_list)

#3. remove() - list.remove(value) - remove value from a list - remove from anywhere by just passing removing value
players_list.remove("Jadeja")
print(players_list) 

#4. insert() - list.insert(index,value) - add value at passed index to the list
print(players_list.insert(3,"Yuvraj"))


#5. slicing - list[startIndex:EndIndex]
print(players_list[1:3]) # return sublist
#same as string slicing just string slicing returns substring and list slicing return sublist
players_list[0:1] = ["Virat Kholi"]
print(players_list) 

players_list[0:2] = ["Virat Anushka Kholi" , "Sachin karishma"]
print(players_list)

#inserting an element in list
print(players_list[1:1])  # returns []
players_list[1:1] = ["hardik"]  #so it will insert hardik at index1
print(players_list)

# removing element in list
players_list[1:2] = []  # it will remove index 1 element
print(players_list)
