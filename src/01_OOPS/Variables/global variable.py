count = 0  # this becomes global and can be accessible everywhere, after it is declred global inside the function

def increement():
    global count   #you can make any variable GLOBAL by typing a keyword global
    count = count + 1

increement()
print(count)