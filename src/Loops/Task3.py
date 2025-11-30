"""
Question 3 :

Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break con
"""
page_loaded = False
wait_time = 0

while wait_time < 5:
    print(f"Waiting... {wait_time + 1} second(s)")
    wait_time += 1

    # Simulate page load becoming True (for example, after 3 seconds)
    if wait_time == 3:
        page_loaded = True

    if page_loaded:
        print("✅ Page loaded successfully!")
        break
else:
    print("⏰ Timeout! Page did not load within 5 seconds.")
