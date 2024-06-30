import random

#random is a module in which you have random(), randint(), choice(), shuffle() methods

print(random.random())  # random.random() method give decimal values b/w 0 to 1 (0.6344424353, 0.9838483634)
print(random.randint(1,10)) #random.randint(int1, int2) give random integer values b/w int1 to int2 include

# random.choice(list) give random values from given list
choiceArr = ['karishma', 'sachin', 'aryan', 'anisha']  #list
print(type(choiceArr))
print(random.choice(choiceArr))  

# random.shuffle(list) shuffles the whole provided list
print(random.shuffle(choiceArr))  # it shuffled the list but return the none to see the shuffle list you have to print the list
print(choiceArr)
