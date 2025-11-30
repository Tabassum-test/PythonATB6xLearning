def vwo_login(user):
    if user != "admin":
        raise Exception("Unauthorized access")
    return "Welcome admin"

#print(vwo_login("tabu"))
print(vwo_login("admin"))