#problem2: find the number is even or odd

num = int(input("enter the number : ").strip())

#if num >= 0:
#     if num % 2 ==0:
#         print("even")
#     else:
#         print("odd")
# else:
#     print("Negative number")

#Use a ternary operator to convert into a one liner
if num >= 0:
    print("even" if num % 2==0 else "odd")
else:
    print("Negative")


