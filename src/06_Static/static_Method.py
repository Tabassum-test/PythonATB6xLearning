"""
Definition of Static Method

A static method is a method inside a class that does not use self or cls.
It is defined using the @staticmethod decorator and can be called directly using the class name, without creating an object.

How do we call it
ClassName.method_name()


Example

class Utility:
    @staticmethod
    def greet(name):
        print("Hi", name)

Utility.greet("Amit")   # ✔ calling using class name

"""

class Utility:

    @staticmethod
    def greet(name):
        print("Hi", name)

    def __init__(self, name):
        self.name = name    # instance variable

    def greet_person(self):
        print("Hello", self.name)


amit = Utility("Amit")
Utility.greet("Amit")       # calling static method
amit.greet_person()         # calling instance method
