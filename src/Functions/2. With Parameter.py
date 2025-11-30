"""
Type2: Function with the parameter and no return type:
"""
def greet(name):
    print("hi", name)

greet("Tabu")
greet("ALi")
greet("Huda")
greet(34.56) #it doesn't care about the data type here, it wil push whatever the args are passed
print("_____________________________")

def greet_first_last_name(firstname, lastname):
    print("Your full name is", firstname, lastname)

greet_first_last_name("Tabassum", "TAj")
print("_____________________________")

