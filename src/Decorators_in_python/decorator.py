"""
Decorators in python are a way to modify the behaviour
of a function or class without changing its source code.
BEFORE
AFTER
LOGGING
"""
def add_security(func):   # func will be drive_ola_scooter
    def wrapper():
        print("Before function is called")
        print("2. Add helmet, Dashcam, gloves, knee guards")

        func()   # <-- This calls the actual drive_ola_scooter()

        print("3. After the function is called")
        print("4. Secure driving, Leave all the items")
    return wrapper       # returning wrapper function


@add_security
def drive_ola_scooter():
    print("driving the scooter")

@add_security
def drive_zypp_scooter():
    print("Driving zypp scooter")


# ✅ Now call the functions
drive_ola_scooter()
print("\n-------------------\n")
drive_zypp_scooter()


print("__________________________________________")

def block_function(func):
    def wrapper():
        print("This function is blocked!")
    return wrapper

@block_function
def my_function():
    print("Original function executed")

my_function()


f