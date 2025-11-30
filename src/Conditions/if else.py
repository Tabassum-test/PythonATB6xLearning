#problem3: #Find the max bw two numbers:
#logic Building:
#step1: i/p --> user input-two float
#step2: o/p-> int 1 which ever is greater num it will return

num1 = float(input("enter the num: ").strip())
num2 = float(input("enter the num: ").strip())
if num1 > 0 and num2 > 0:
    print("number must be positive")
    if num1 >=  num2:
         print("Max is ", num1)
    else:
         print("MAx is ", num2)