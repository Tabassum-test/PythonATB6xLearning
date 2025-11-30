#Write a program to calculate the area of a circle given its radius using the formula
#area = πr^2 (pie=3.14)
#Tip: Always ask the interviewer the i/p and o/p
import math

#i/p - r - float
#o/p -> string formatted output of area

# Program to calculate the area of a circle

# Take input from the user
radius = float(input("Enter the radius of the circle: "))

# Formula for area of a circle
area = 3.14159 * (radius ** 2)

# Display the result
print("The area of the circle is:", area)


print("+++++++++++++++++++++++++++++++")

# i/p - r - float
# o/p -> string formatted output of area

# Input
r = float(input("Enter radius: "))

# Processing
#area = 3.14159 * (r ** 2)
area = 3.14 * (pow(radius,2))  #use pow function also directly


# Output (string formatted)
print(f"The area of the circle with radius {r} is {area:.2f}")

print("+++++++++++++++++++++++++++++++")

radius = float(input("enter the radius :"))

area = math.pi * pow(radius,2)

print(f"the radius is {radius} and area is {area:.2f}")