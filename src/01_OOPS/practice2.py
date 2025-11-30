#With PArameterized COnstructor
class Calculator:
    def __init__(self, a, b):
        print("PC2")
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

object_ref = Calculator(a, b)

output_sum = object_ref.sum()
output_sub = object_ref.sub()
output_mul = object_ref.mul(
output_div = object_ref.div()

print(output_sum, output_sub, output_mul, output_div)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

#With Default COnstructor
class Calculator:

    def __init__(self):
        print("Default Constructor Called")

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b


# Taking input
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))

# Creating object (default constructor)
obj = Calculator()

# Calling static methods (no self needed)
print("Sum =", Calculator.sum(a, b))
print("Sub =", Calculator.sub(a, b))
print("Mul =", Calculator.mul(a, b))
print("Div =", Calculator.div(a, b))

