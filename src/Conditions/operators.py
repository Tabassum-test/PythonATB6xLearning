#Operators are a special symbols that perform operations on variables and values
# - like addition, comaprison, logical test etc..
# EX: age = 96
#age : identifier or variable =: operator 96 : literal


#Arithmetic Operators:
a, b = 10, 3
print(a+b) #13
print(a-b) #7
print(a*b) #30
print(a/b) #3.33  div always gives float result
print(a % b) #1
print(a**b) #1000 10 to the power 3
print("------------------")
#note: there is a divmod function which gives both quotient and remainder as a result
q, r = divmod(5,2)
print(q)
print(r)

print("------------------")

#Comparison(Relational) Operator:
x, y = 10, 20
print(x==y) #false
print(x!=y) #true
print(x>y)  #false
print(x<y)  #true

print("------------------")

#Logical operator:
a,b = 5, 10
print(a>0 and b>0) #true
print(a>0 or b<0)  #true
print(not(a>0)) #false

print("------------------")
#AND Gate:          # OR GAte:
#0 0 | 0             0 0 | 0
#0 1 | 0             0 1 | 1
#1 0 | 0             1 0 | 1
#1 1 | 1             1 1 | 1

#Note: No increement and decreement operator!
#We have this increments:

x=5
x += 1
print(x)

x -=1 #x=x-1
print(x)

x *=3 #x=*3
print(x)

print("------------------")
#Assignment Operator:
x = 10
x += 5
print(x)

x*=2
print(x)

#Membership Operator:
# in : if value found
#not in : if value not found

#Ternary Operator: if - else statement
x=10
y=20

print("x is greater than y" if x>y else "x is less than y")




