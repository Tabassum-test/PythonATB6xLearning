"""
Type 5: FUnction with multiple return value
"""
def math_operations(a,b):
    return a+b,a-b, a*b #using return keyword multiple times is not allowed but wrinting in a comma separated line is allowed

sum_r, diff_r, mul_r = math_operations(3,4) #you can assign different variables also
print(sum_r)
print(diff_r)
print(mul_r)