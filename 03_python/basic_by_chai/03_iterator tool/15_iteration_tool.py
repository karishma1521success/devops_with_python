# Read file in python
print("hello")
f = open('basic_by_chai/16_file_to_read.py')  # this to open a file

print(f.readline())   # This is read a line in file whenn it has no line further it will return '' empty string
# We wrote only 1 readline() so it will print only 1 line to print further lines you have to use more readline() method


# To print all the lines of file
for line in open('basic_by_chai/16_file_to_read.py'):
    print(line, end = '')

    

