"""
Constructor: Its a special type of function
Called automatically when you create an object
Two types:
 1.Default with no argument - DC
2. Parameterised - with argument

Constructor doesn't return anything
__init__name of the constructor
self - current object

Constructors are used to initialize the attribute values
"""

class Dog:
    #Attributes
    name = None
    breed = None
    height = None
    weight = None

#Behaviour
    def bark(self): #Methods are always available in class and its a reference to the class DOG
        print("Barking")
        print(self.name) #always use self to access attribute

    def talk(self):
        print("Talking")

print("Outside")
chow = Dog()
chow.bark()

rancho = Dog()
rancho.talk()