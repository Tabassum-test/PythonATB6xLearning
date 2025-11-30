def before_after_ui_test(func):
    def wrapper():
        print("Before Running COde")
        func()
        print("After running code")
    return wrapper()



@before_after_ui_test
def test_ui():
    print("Im testing a UI test")