from dotenv import load_dotenv
import os

# Load .env from project root
load_dotenv(override=True)


class VWOLoginPage:

    def __init__(self, email, password):
        self.email = email.strip()
        self.password = password.strip()

    def login_confirm(self):
        env_user = (os.getenv("VWO_USERNAME") or "").strip()
        env_pass = (os.getenv("PASSWORD") or "").strip()

        print("DEBUG:", repr(env_user), repr(env_pass))

        if self.email == env_user and self.password == env_pass:
            print("Allowed to login")
        else:
            print("Login Failed")

email = input("Enter the vwo login email:\n")
password = input("Enter the vwo login password:\n")

obj = VWOLoginPage(email, password)
obj.login_confirm()
