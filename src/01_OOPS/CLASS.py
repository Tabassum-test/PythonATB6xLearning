"""
class = is a user-defined data type which defines its properties and its methods/ blueprint
object = run-time entity, real world entity
Attributes = Properties | data variables.
behaviour = method, function | data member | Member Function

Note: When a class is created, no memory is allocated,
but when object is created, the memory is allocated.
"""
class Person:
    name = None   #in python, Attributes can be of any data type
    id = None
    age = None
    email = None
    height = None
    gender = None
    address = None

    def talk(self):
        print("I can Talk")

    def walk(self):
        return "I'm Walking"

def function_outside():
    print("outside")

geeta = Person()
amit = Person()
print(geeta.name)
