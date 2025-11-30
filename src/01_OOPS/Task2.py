class Calculator:

    # PARAMETERIZED CONSTRUCTOR
    def __init__(self, a, b):
        print("Parameterized Constructor Called")
        self.a = a
        self.b = b

    # SINGLE CALCULATOR FUNCTION
    def calculate(self):
        s = self.a + self.b
        sub = self.a - self.b
        mul = self.a * self.b
        div = self.a / self.b

        return s, sub, mul, div


# ---------------- MAIN PROGRAM ----------------

# Creating object with values (constructor parameters)
value1 = float(input("Enter first number: "))
value2 = float(input("Enter second number: "))

obj = Calculator(value1, value2)

# Call calculator function
sum_val, sub_val, mul_val, div_val = obj.calculate()

# Print results
print("Sum:", sum_val)
print("Subtraction:", sub_val)
print("Multiplication:", mul_val)
print("Division:", div_val)
