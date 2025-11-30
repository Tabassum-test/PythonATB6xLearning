#ENCAPSULATION: we bind the data variable with the method.
#Hide the data members(class varisbles,instance variables)
#by using only the methods
#protected: _
#private: __

# class Car:
#
#     def __init__(self):
#         self.password = "pramod"
#         self.__password_secure = "pass123"
#
#     def nany(self):
#         self.__password_secure = "345"
#
#
# object_ref = Car()
# print(object_ref.password)
#
# object_ref.nany()
# print(object_ref.__password_secure) #this will not access, because it is private


# print(___________________________________________)
#chatgpt answer

class Car:

    def __init__(self):
        self.password = "pramod"
        self.__password_secure = "pass123"

    def nany(self):
        self.__password_secure = "345"

    def get_password_secure(self):   # Added this only
        return self.__password_secure


object_ref = Car()
print(object_ref.password)

object_ref.nany()
print(object_ref.get_password_secure())   # Correct way

