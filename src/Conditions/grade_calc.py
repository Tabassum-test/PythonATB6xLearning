"""
Grade calculator:
WAP to calculate and display the letter grade for the given numbers
score (A, B, C, D or F) based on the following scale
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
"""

#logic building
#i/p--> Ask from the interviewer: int
#o/p--> String

score=int(input("Enter the score: ").strip())

if score > 100 or score <= -1:
    print("enter the valid score")
else:
    if score >= 90 and score <=100:
        print("A grade")
    elif score >= 80 and score <=89:
         print("B grade")
    elif score >= 70 and score <=79:
          print("C grade")
    elif score >= 60 and score <= 69:
          print("D grade")
    else:
           print("F grade")




