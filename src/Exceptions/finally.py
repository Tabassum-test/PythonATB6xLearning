try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c=a/b
    print(c)

except ValueError:
    print("ValueError")

except ZeroDivisionError:
    print("Zero div error")

finally:
    print("I will always execute")