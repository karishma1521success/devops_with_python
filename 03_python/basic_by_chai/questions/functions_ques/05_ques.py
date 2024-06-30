
# def greet(name):
#     if name == "":
#         name = "Special One"
#     return "Hello " +name+" !"

# another way
def greet(name = "special one"):
    return "Hello "+name+" !"
print(greet("chai"))
print(greet())
