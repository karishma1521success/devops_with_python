# List - Sequence data type and fundamental data structure
#2. list are resizable/mutable(means can add elements or can also remove elements)
#3. list are dynamic in nature 
#4. list memory allocation is done at runtime
#5. Use list when you don't know the fixed size
#6. List are created using the [] brackets , it can contain any type of elements
#7. Indexing starts from 0 and go till length-1
#8.  list length -- len(list_name)


student_lists = ["abhishek" , "john" , "anisha" , "aryan", "sachin"]
print(student_lists);   # ['abhishek', 'john', 'anisha', 'aryan', 'sachin']
print(type(student_lists))  # <clas 'list'>

#Accessing element by Index
student1 = student_lists[0]  #  'abhishek'

#1. len() -- method to get the lenght of the list
total_students = len(student_lists)   #5

#Operation and maniuplation on list - append, remove, slicing, concatenating, sorting, checking for an element.


#1. Appending element to a list   -- list_name.append(element)
#add new element at the end of the list
student_lists.append("karishma");   # ['abhishek', 'john', 'anisha', 'aryan', 'sachin', 'karishma']


#2. Removing element from a list  -- list_name.remove(element) 
#can remove element from anywhere of the list just provide element name that you want to remove
student_lists.remove("john")   #['abhishek', 'anisha', 'aryan', 'sachin', 'karishma']
print(student_lists)


#3. Slicing a list----   list_name[start:stop]    include start element and exclude stop element
new_list = student_lists[0:2]   #['abhishek', 'anisha']
print(new_list)

#4. Concatenating lists  -- list1 + list2
list1= [1,2,3]
list2 = [4.5,6]
concate_list = list1 + list2
print(concate_list)

#5. Sorting a list -- list_name.sort()
numbers = [1,4,9,2,0]
numbers.sort()
print(numbers)

#6. Checking for an element  -- elementValue in listName
isSachinPresent = "sachin" in student_lists
print(isSachinPresent)

