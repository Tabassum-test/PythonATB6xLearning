a=10 #global variable available everywhere in the program
class Person:
    b = 11   #Instance variable available only inside class

    def print_info(self):
        c = 20  #LOcal variable available only inside method/Function
        print(c)
        print(self.b)
        print(a)

object_ref = Person()
object_ref.print_info()