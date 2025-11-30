
print("Outside the class")

class MobilePhone:
    model = None


    def __init__(self):             #No need to create an object reference,
        print("Directly Called")    # this will get automatically called



    def talk(self):
        print("Hi, talking")

iphone = MobilePhone()   #create an object
iphone.talk()            #using the object reference, we call the method
print("Outside the class")




