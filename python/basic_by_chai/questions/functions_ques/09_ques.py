# generate all even numbers upto limit

limit = int(input("Enter a number: "))
def even_generator(limit):
    for i in range(2, limit+1, 2):
        #range(2, limit+1, 2) end 2 represents gap means every 2nd number
        # print(i)
        yield i


# even_generator(limit) is now iterable object
for num in even_generator(limit):
    print(num)

# but no we don't have to print we want to return every number in loop
# but we used return(i) - it will give only 2 and that function will get terminate and other even numbers didn't get generated
# case - you want to return something but you don't want to exit the function and also want to recontinue where it left - use yield keyword
