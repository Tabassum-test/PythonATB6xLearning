class Person:

    # ---------- DEFAULT CONSTRUCTOR ----------
    def __init__(self):
        print("Default Constructor Called")
        self.name = None
        self.age = None
        self.gender = None
        self.city = None
        self.occupation = None

    # ---------- PARAMETERIZED FUNCTION (BEHAVIOR 1) ----------
    def set_details(self, name, age, gender, city, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.city = city
        self.occupation = occupation

    # ---------- INSTANCE METHOD (BEHAVIOR 2) ----------
    def introduce(self):
        print(f"Hello, my name is {self.name}.")

    # ---------- INSTANCE METHOD (BEHAVIOR 3) ----------
    def live_in_city(self):
        print(f"{self.name} lives in {self.city}.")

    # ---------- INSTANCE METHOD (BEHAVIOR 4) ----------
    def work(self):
        print(f"{self.name} works as a {self.occupation}.")

    # ---------- INSTANCE METHOD (BEHAVIOR 5) ----------
    def celebrate_birthday(self):
        print(f"Happy Birthday {self.name}!")
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

    # ---------- PRINT FUNCTION (as required) ----------
    def print_details(self):
        print("------ Person Details ------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("City:", self.city)
        print("Occupation:", self.occupation)
        print("-----------------------------")


# ------------------ MAIN PROGRAM -------------------

p = Person()

# Set values
p.set_details("John", 25, "Male", "Delhi", "Engineer")

# Print all details
p.print_details()

# Behaviors
p.introduce()
p.live_in_city()
p.work()
p.celebrate_birthday()
