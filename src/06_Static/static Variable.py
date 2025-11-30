"""
What are Static(class) Variables?
A static variable (also called a class variable) is a variable that is defined inside a class but outside all methods, and it is shared by all objects of the class.
All instances use the same copy of this variable.

Example:

class Example:
    count = 0   # static variable
"""
class TestCounter:

    count = 0   # ✅ static/class variable

    def __init__(self):
        TestCounter.count += 1  # accessing the class variable


t1 = TestCounter()
t2 = TestCounter()
print(TestCounter.count)
