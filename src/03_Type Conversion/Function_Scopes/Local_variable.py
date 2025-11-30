pb_global_b = 12  #global variable can be accessed outside the function as well

def my_function():
    pb_a = 10   #Local variable is accesses only within this block
    print(pb_a)
    print(pb_global_b)

my_function()
print(pb_global_b)