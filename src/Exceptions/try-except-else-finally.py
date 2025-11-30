try:
    a = int(input("Enter num 1 : "))
    b = int(input("Enter num 2 : "))
    c=a/b

except ValueError:
    print("ValueError")

except ZeroDivisionError:
    print("Zero div error")

else: #runs only if try block succeeds
    print(c)

finally:
    print("I will always execute")