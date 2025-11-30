#1.Print numbers 1 to 10 using a for loop.
# for i in range(1,11,1):
#     print(i)

#2.Make a while loop that stops when the user types quit.
"""
while True:
    print("This will never stop")
💡 This is called an infinite loop — it keeps repeating endlessly until something inside stops it.
"""
# while True:
#     text = input("Type something (or 'quit' to stop): ")
#     if text == "quit":
#         break
#     print("You typed:", text)


#3.Given list nums = [3, 5, 8, 2], print only numbers greater than 4 using for and if.
nums = [3, 5, 8, 2]
for n in nums:        # take one number from the list at a time
    if n > 4:         # check if that number is greater than 4
        print(n)      # if yes, print it

