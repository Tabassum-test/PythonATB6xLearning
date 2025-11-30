#Conditions:
# Used when you want to execute the certain parts of code only if a specific conditions is true.

#problem 1: WAP to take the user age and let him know if he can go to the club 21.

#step1: i/o : age-int
# o/p: string(result)- can go to club or not.

#step2: Rough logic
'''
age > 21 --> print can go
age< 21--> Print can't go
'''

#Step 3: write the logic

age=int(input("Enter the age: "))
if age<=0 and age >130:
    print("Enter the valid age")
else:
    if age >= 21:
        print("yes,Can go to the club")
    else:
        print("NO,Can't go to the club")




#step4: check for the edge cases:
#Negative ages or extremely high values--> program will break
# Non - numeric input-ABc
#Age more than 100

#step5: Optimize the code.
#HAndle all the edges


"""
NOTE:
.strip(): this function makes sures the extra spaces provided in the input will be removed.

to handle the alphanumeric we have to use TRY cstch()
"""