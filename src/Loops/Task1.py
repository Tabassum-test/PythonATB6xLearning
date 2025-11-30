"""
Question 1. :
Given a Number  you need to calculate the factorial of that number
n = 5
Fact = 5×4×3*2*1 = 120
Fact(0) is 1,
"""

n = int(input("Enter a number: "))

fact = 1

if n == 0:
    fact = 1
else:
    for i in range(1, n + 1):
        fact = fact * i

print(f"Factorial of {n} = {fact}")


#or
print("------------------")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print("------------------")

num = int(input("Enter a num: "))
fact=1

if num <= 0:
    print(fact)
else:
    for i in range(1,num+1):
        fact = fact * i

print("Factorial of:", fact)
