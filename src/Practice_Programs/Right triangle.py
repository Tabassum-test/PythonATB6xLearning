"""
WRIte a program to print stars which is in right angled triangle
*            i | j     | o/p
**          1  | 1     | *
***         2  | 1,2   | **
n = 3       3  | 1,2,3 | ***

"""

rows = int(input("ENter the rows for the RIght angle triangle"))

for i in range(1, rows+1):
    for j in range(i):
        print("*",end="")
    print()


#print(+++++++++++++++++++++++++++++++++++)
#same problem with different solution

for i in range(1,6):
    print("*" * i)