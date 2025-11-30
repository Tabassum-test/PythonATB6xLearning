def square_number():
    number = int(input("Enter a positive number: "))
    result = number * number
    print("Square of the number is:", result)

square_number()

print("_____________________________")


#🔹 Alternate version (if you want to pass number as argument):
def square_number(number):
    print("Square of the number is:", number * number)

num = int(input("Enter a positive number: "))
square_number(num)

print("_____________________________")

def square_number(number):
    #print(int(input("Enter your number")))
    result = number * number
    return result

output = square_number(6)
print(output)

print("_____________________________")

def square(num):
    if num > 0:
        print(num * num)
    else:
        print("please enter the positive number")

square(int(input("enter your positive number : ")))
