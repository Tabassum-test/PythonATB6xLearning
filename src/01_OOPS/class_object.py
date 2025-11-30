
print("Outside the class")
class MobilePhone:
    model = None

    def __init__(self):# Automatically called, when the object is createdp[
       print("Default Constructor")


    def talk(self):
        print("Hi, Talking")

iphone = MobilePhone()
iphone.talk()
print("Outside the class")