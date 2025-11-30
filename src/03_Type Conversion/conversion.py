a ="10"
a = int(a)
print(type(a))

#Classify the triangle

side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

def classify_triangle(a,b,c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                return "Equilateral"
            elif a == b or b == c or a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Not a triangle"     # ✅ return not print
    else:
        return "Not a valid length"     # ✅ return not print

result = classify_triangle(side1, side2, side3)
print(f"Triangle is classified as : {result}")
