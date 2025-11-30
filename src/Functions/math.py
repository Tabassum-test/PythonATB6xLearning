# import math
# from src.Functions.userinput import user_input

#built-in functions
# result = max(3,4)
# print(result)

#creat a program to sum of 3 numbers from the user input
#if user doesn't enter any number, use default as 100, 200, 300.
# i/o - int
#o/p - int


#step 2: Rough logic
#return n1 + n2+ n3

#step 3 - write logic
# Take three numbers as input from the user
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

# Define a function with default parameter values
def sum_of_three(n1=100, n2=200, n3=300):
    return n1 + n2 + n3

# Different function calls
result = sum_of_three(num1, num2, num3)   # Uses user input
result1 = sum_of_three()                  # Uses default values
result2 = sum_of_three(n1=10)             # Overrides only the first value

# Print the result of the chosen call
print("The total is:", result2)


