class Dog:
    #Attributes
    name = None
    breed = None
    height = None
    weight = None
    race = None

    # def __init__(self, nameGiven, breedGiven):
    #     print("Param C")
    #     self.name = nameGiven
    #     self.breed = breedGiven
    
    def __init__(self, nameGiven, breedGiven):
        print("Param C")
        self.name = nameGiven
        self.breed = breedGiven
        print("Name:", self.name)
        print("Breed:", self.breed)

    def bark(self):
        print("Barking")
        print(self.name)

    def sleep(self):
        print("who is sleeping ->" +self.name)

    def details(self):
        print("Name:", self.name)
        print("Breed:", self.breed)

chow = Dog("chow", "mastiff")
rancho = Dog("rancho", "desi")

chow.sleep()
print(chow.breed)
