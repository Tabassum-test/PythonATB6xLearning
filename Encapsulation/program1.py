#ENCAPSULATION: we bind the data variable with the method.
#Hide the data members(class varisbles,instance variables)
#by using only the methods


class Car:

    def __init__(self, O_name, O_make, O_model):
        self.name = O_name
        self.make = O_make
        self.model = O_model


    def start_engine(self):
        print("Starting a car with the name "+self.name)
        print("Starting a car with the make "+self.make)
        print("Starting a car with the model " + self.model)


lambo = Car("Lambo", "1.5+ Turbo", "2025")
lambo.start_engine()