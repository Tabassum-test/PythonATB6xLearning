"""
What are Exceptions?
Exceptions in python are events that occur during
the execution of a program tht disrupts the normal flow of instructions

A way to handle errors and unexpected situations gracefully.

TYPES of Exceptions:
Python has many built - in exceptions that are raised when specific errors occur.
NameError - Raised when a local or global variable is not found.
TypeError: Raised when an operation is performed on an incompatible data type Ex: (1 + "1")
ZeroDivisionError : Anything divided by 0
ValueError: int("a") invalid ;literal for int()
IndexError: if you are trying to access invalid index
SyntaxError: If the syntax is wrong



To handle the exceptions:
Try:

except:

else:

finally:

"""

try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c=a/b
    print(c)
except(NameError,ValueError,ZeroDivisionError):
    print("Error! Due to the Name, Value")