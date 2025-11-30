"""
Method Overloading is not supported by python, it will be overridden with the second function
"""

class MAthClass:
    def add(self,a,b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


obj = MAthClass()
obj.add(3,4)
obj.add(3.14,4.15)

#print(______________________________________________)
"""
But python supports multiple arguments"""

class MathClass:
    def add(self, *args):
        return sum(args)

obj = MathClass()

print(obj.add(3, 4))        # 7
print(obj.add(3, 4, 5))     # 12
print(obj.add(1, 2, 3, 4))  # 10

""""""
