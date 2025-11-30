"""Build a Test Framework with Encapsulation + Inheritance

🎯 Goal:

Create a simple automation structure that uses:

A BaseTest class for setup/teardown (Parent class)

A LoginTest class that inherits BaseTest (Child class)

Encapsulate sensitive data (like credentials) as private variables


✅ Requirements:

Create a BaseTest class:

Has a protected variable _driver = "Chrome".

Method setup() prints "Launching browser: Chrome".

Method teardown() prints "Closing browser".

Create a LoginTest class that inherits BaseTest:

Has private variables for username and password.

Method run_test() that prints:

"Running login test with user: <username>".

Use encapsulation: access private vars only through a method (e.g., get_user()).

Create an object of LoginTest and call:

setup()

run_test()

teardown()"""




# ------------------ BaseTest (Parent Class) ------------------

class BaseTest:

    def __init__(self):
        self._driver = "Chrome"   # Protected variable

    def setup(self):
        print(f"Launching browser: {self._driver}")

    def teardown(self):
        print("Closing browser")


# ------------------ LoginTest (Child Class) ------------------

class LoginTest(BaseTest):

    def __init__(self):
        super().__init__()   # Call parent constructor
        self.__username = "admin"         # Private variable
        self.__password = "password123"   # Private variable

    # Encapsulated getter (private data accessed safely)
    def __get_username(self):
        return self.__username

    def run_test(self):
        # Use encapsulation to access private username
        user = self.__get_username()
        print(f"Running login test with user: {user}")


# ------------------ Run the Test ------------------

test = LoginTest()
test.setup()
test.run_test()
test.teardown()
