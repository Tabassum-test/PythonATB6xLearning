"""
# LOOPs
> Repeat a block of code multiple times.



**Block of Code**

1. something to print that you repeat.
2. somecode that you can execute multiple times.


- For loop
- While


Used to iterate over a sequence (like a list, tuple, dictionary, string, or range).


What is `range()`?

`range()` is a built-in Python function used to generate a sequence of numbers.
 Commonly used in `for` loops.
## Syntax:
range(start, stop, step)
"""


for i in range(0,10,1):
    print(i)
print("_________________________")
# for i in range(0, 10, 1.5): # the number must be int not float so 1.5 it wont execute
#     print(i)

for i in range(3,5): #By default step is always 1
    print(i)
print("_________________________")
for i in range(10):
    print(i)
print("_________________________")
for i in range(1,10,-1): #no output for this as 1-1=0
    print(i)
print("_________________________")
for i in range(10):
    print("Hello world")
print("_________________________")
for i in range(10,0,-2):
    print(i)
print("_________________________")
num = range(10)
print(num)