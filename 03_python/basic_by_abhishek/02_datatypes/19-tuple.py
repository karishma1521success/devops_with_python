#1. Tuple - Sequence data type and fundamental data structure
#2. Tuple are not resizable/immutable(means cannot add elements or can also remove elements)
#3. Tuple are static in nature 
#4. Tuple memory allocation is done at complie time
#5. Use Tuple when you know the fixed size and don't need any changes
#6. Tuple are created using the () brackets , it can contain any type of elements
#7. Indexing starts from 0 and go till length-1
#8.  Tuple length -- len(list_name)
#9. cannot add and remove elements - no append and no remove


my_tuple = (1,2,"apple", "banana")
print(my_tuple)         #(1,2,'apple','banana')
print(type(my_tuple))   #<class 'tuple'>

my_tuple[0]       #1
len(my_tuple)     #4


#tuple operations  - accessing element, tuple packing and unpacking, concatenating , checking for an element, using tuples for multiple return values

#1. Accessing tuple element
my_tuple[1]    #2

#2. Tuple packing and unpacking
a,b,c,d = my_tuple      # a=1, b=2, c='apple'  d='banana'

#3. concatenating tuples =    tuple1 + tuple2
tuple1 = (1,3,4)
tuple2 = (3,4,1)
result = tuple1 + tuple2
print(result)       (1, 3, 4, 3, 4, 1)

#4. Checking for an element
is_present = "apple" in my_tuple
print(is_present)


