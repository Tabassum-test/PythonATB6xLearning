"""
**Factorial**

The factorial of a number `n` is the product of **all positive integers less than or equal to **`**n**`.

- User A number = 5
- n! ->  n*_n-1n-2..... 2*1_
- 0! -> 1
- 1! -> 1
- 2! -> 2*1 -> 2
- 3! -> 3 _ 2 _ 1 -> 6
- `5! = 5 × 4 × 3 × 2 × 1 = 120`
"""

num = int(input("Enter a number: "))

fact = 1
if num <= 0:
    print(fact)
else:
    for i in range(1,num+1):
        fact = fact * i
print(fact)

"""
Edge cases:
Larger number for factorial
invalid, string, blank, symbol, negative
decimal points
"""

num = int(input("Enter a number: "))

fact = 1
if num <= 0:
    print("undefined")

if num == 0:
    print("factorial is", fact)
else:
    for i in range(1,num+1):
        fact = fact * i
print(fact)
