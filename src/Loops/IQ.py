# for i in range(0,10):
#     if i== 5:
#         print("Five")
#     else:
#         print(i)
# print("+++++++++++++++++++++++++++++++")

for i in range(1,10):
    print(i)
    if i ==5:
        break

# print("+++++++++++++++++++++++++++++++")

# for i in range(1,10):
#     if i ==5:
#         print(i)
#     else:
#         print("no op")

# print("+++++++++++++++++++++++++++++++")

#To print 3*3 stars:
"""
print("*", end="")
You are telling Python:

“After printing the star, don’t go to the next line.
Just stay on the same line.
for row in range(3):          # ↓  outer loop (go down)
    for col in range(3):      # →  inner loop (go right)
        print("*", end="")    # print stars side by side
    print()                   # move cursor to next line
row 0:  *→*→*
          ↓
row 1:  *→*→*
          ↓
row 2:  *→*→*
🧩 Understanding before we start

row → outer loop → controls how many lines (rows) there are

col → inner loop → controls how many stars per line

end="" → keeps printing stars on same line

print() → moves down to the next line
"""

for x in range(3):
    for y in range(3):
        print("*", end="")
    print()

"""
Outer loop → row = 0
   Inner loop → col = 0,1,2 → prints row 0 (***)
Outer loop → row = 1
   Inner loop → col = 0,1,2 → prints row 1 (***)
Outer loop → row = 2
   Inner loop → col = 0,1,2 → prints row 2 (***)
"""
#TO check 3*3 rows and columns:
for row in range(3):
    for col in range(3):
        print(f"({row},{col})", end=" ")
    print()

