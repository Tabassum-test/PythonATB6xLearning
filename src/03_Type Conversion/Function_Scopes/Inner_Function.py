def outer_function():
    var1 = 30

    def inner_function():
        var2 = 90
        print(var1)

    def inner_function2():
        print(var1)

    inner_function()
    inner_function2()

outer_function() #outer function can only be called outside
#inner_function() #inner cant be called outside the function