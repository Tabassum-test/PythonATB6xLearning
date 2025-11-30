"""Question 2 :

An API sometimes fails due to network delays.

Write a program to retry the API call 3 times until the response code becomes 200.

If it still fails after 3 tries, print a failure message.

Hint: Use a while loop with a counter.
Hint: Use a while loop with a counter.

Expected Output Example:

Attempt 1: Response 500

Attempt 2: Response 200

✅ Test Passed
"""

# Simulating API call responses (for example)
responses = [500, 500, 200]  # you can change values to test

attempt = 0
max_attempts = 3

while attempt < max_attempts:
    attempt += 1
    response_code = responses[attempt - 1]  # simulate API response

    print(f"Attempt {attempt}: Response {response_code}")

    if response_code == 200:
        print("✅ Test Passed")
        break
else:
    print("❌ Test Failed after 3 attempts")
