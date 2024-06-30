# tuple is an ordered collection of elements
# It is immutable

players = ("Sachin" , "Dhoni" , "Virat", "Rohit", "Rishab", "Shubhman")
print(players)

print(players[0])  # accesing an element
print(players[-1]) # can also accessed element with negative index

#len(tuple) - length of tuple
print(len(players))

# error - players[0] = "sachin tendulkar"

#1. slcing --> tuple[start:end]
print(players[1:5])

#2. count() -- tuple.count(value)
print(players.count("Sachin"))

# assigning tuples elements
tuple1 = ("batter" , "keeper")
(sachin,dhoni) = tuple1
print(sachin)
print(dhoni)