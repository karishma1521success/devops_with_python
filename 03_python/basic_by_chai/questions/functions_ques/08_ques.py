def print_all(**kwargs):
    print(kwargs)  # returns dictionary
    for key, value in kwargs.items():
        print("Key: " , key , " Value: ", value)

print_all(name = "karishma" , age = 12)