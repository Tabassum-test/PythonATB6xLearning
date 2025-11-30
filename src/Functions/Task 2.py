def which_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral Triangle"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

# take 3 inputs from user
side1 = int(input("Enter side1: "))
side2 = int(input("Enter side2: "))
side3 = int(input("Enter side3: "))

# call the function
result = which_triangle(side1, side2, side3)

print(result)

