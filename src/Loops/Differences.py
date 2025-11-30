for i in range(0,10):
    if i==5:
        print("Five")
    else:
        print(i)
"""
EXP and result table(ERT)
|i| Condition  | o/p   |
0 | 0==5->False| o/p =0
till 5
"""
print("____________________________")

for i in range(0,10):
    print(i)   #0,1,2,3,4,5 first it will be printed then the condition is checked
    if i == 5:
        break
"""
ERT table:
|i | condition | o/p |
0 | 0==5->False | 0
5 | 5==5->True  | break out of the loop
"""
print("____________________________")

for i in range(0,10):
    if i == 5:  #here first the condition is checked
        break
    print(i)  #prints only till 4

print("____________________________")

for i in range(0, 10):
    if i == 5:  # here first the condition is checked
     print(i)
     break     # prints only 5
print("____________________________")

for i in range(0,10):
    if i == 5:
        break

print(i)  #prints only 5

"""
🧭 Final Summary
Program	Where break is placed	What happens	Output
1️⃣ break before print()	Loop stops before printing 5	0 1 2 3 4	
2️⃣ break after print()	Prints 5, then stops	5	


🧭 FINAL COMPARISON TABLE
Case	Where is print()?	Where is break?	When does it stop?	Output
1️⃣	After break (outside if)	Inside if before print	Stops before printing 5	0 1 2 3 4
2️⃣	Inside if before break	Same line block	Prints 5, then stops	5
3️⃣	Before if	Inside if after print	Prints 0–5, then stops	0 1 2 3 4 5


🧠 Simple Rule to Remember

✅ Python reads top to bottom, inside out.
👉 So wherever print() comes before break, that value will print.
👉 If break comes before print(), that value won’t print.
"""



