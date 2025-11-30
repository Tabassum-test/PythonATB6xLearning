"""ABSTRACTION:
Hide the details and show what is required
Abstraction basically means incomplete
"""
#module name abc is created which is abstractclass
from abc import ABC, abstractmethod

class Animal(ABC): # Inheriting from Abstract class created in the module abc

    def __init__(self,name):
        self.name = name

    @abstractmethod   #use @decorator to hide the details
    def sound(self):
         pass

class Dog(Animal):  #You can complete the function sound here in this class

    def sound(self):
        print("Bark")

dog = Dog("PP")
dog.sound()
