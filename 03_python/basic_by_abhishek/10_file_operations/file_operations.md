open(path,'r/w'), with open(path,'r') as file,  file.readLines() , file.write(str) 
# file operations in python - read /write

#for both operations you have to open file either in read or write mode

# 1. open(path,'r/w')  --- open file in read or write mode
#It's inbuilt function in python
syntax --   with open(path, 'r') as file:
# path should be in str format

# 2. fileVariable.readLines() - to read all content of file you can store all lines in variable - list of lines

# 3. file.write(str) - updated text to write something 
