#problem 4: find the max bw 3 numbers:

#i/p: 3 numbers-int
#o/p: int or string with max number.

num1 = int(input("enter the num1 : ").strip())
num2 = int(input("enter the num2 : ").strip())
num3 = int(input("enter the num3 : ").strip())

# if num1 >= num2 and num1 >= num3:
#     print(num1)
# elif num2 >= num3 and num2 >= num1:
#     print(num2)
# else:
#     print(num3)


#or just use the max function
print("Maximum number is:", max(num1, num2, num3))

