class VWOLoginPage:

    def __init__(self,email,password):
        self.email = email
        self.password = password


    def login_confirm(self):
        if self.email == "pramod@gmail.com" and self.password == "pass123":
            print("Allowed to login")
        else:
            print("login Failed")

email = input("Enter the vwo login email :\n")
password = input("Enter the vwo login password :\n")

vwo_objectref = VWOLoginPage(email,password)
vwo_objectref.login_confirm()

