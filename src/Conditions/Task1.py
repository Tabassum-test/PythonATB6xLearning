"""
Q - You receive an API response code from your test script.
Write an if-else block to check whether the response is successful (status code 200) or not.

I/P response = 404 , O/P ❌ Failed API Request
I/P response = 200 , O/P ✅ Passed API Request


i/p : int code
o/p: string
"""

response_code = int(input("Enter the code: ").strip())

if response_code < 100 or response_code > 599:
    print("Please enter a valid code")
else:
    if response_code == 200:
        print("✅ Passed API Request")
    else:
        print("❌ Failed API Request")
