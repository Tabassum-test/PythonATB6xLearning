class MathOperation:

    def div(self, a, b):
        return a / b   # instance method

    @staticmethod
    def sum(a, b):
        return a + b   # static method does NOT use self


# Calling the non-static (instance) method → needs an object
t = MathOperation()
print(t.div(10, 10))

# Calling the static method using the classname.method directly
# static methods are called directly without creating an object
print(MathOperation.sum(10, 10))


