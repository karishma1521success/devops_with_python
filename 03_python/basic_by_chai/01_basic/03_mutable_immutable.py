#Internal working of python
#1. data object take memory allocation in memory 
#2. then variable reference to the data object  - it stores memory address where the data object is stored

#Mutable data types - These are those data which can be changed 

list1 = [1,2,3]    # memory - 1. [1,2,3] data allocated in memory    2. list1 variable is referencing to [1,2,3] - 1001 
list1[0] = 44      # list1 has changed and list is mutable then data will be [44,2,3] and list1 still refering to that same memory allocation - 1001 just memory has changed
print(list1)       # [44,2,3]

#LIST IS MUTABLE

list1 = [1,2,3]     # [1,2,3] data memory allocated first and then list1 reference to [1,2,3] = 1001
list2 = [1,2,3]     #[1,2,3] new memory allocation happen doesn't matter the same data is already present or not list 2 = 1002
# you can see both list1 and list2 has same data but they will reference to different memory allocation
list1[0] = 44
print(list1)  #[44,2,3]
print(list2)  #[1,2,3]


#Immutable - means it cannot be changed

tuple1 = (1,2,3)
# tuple2[0] = 44   cannot happened we can't change the value
