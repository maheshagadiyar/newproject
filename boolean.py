a = input("Please enter user name")
b= input("Please enter password")

def login():
    username = "admin"
    password = "Password"
if a == "admin" and b == "password":
    print("valid credentials, logged in successfully")
else:
    print("Invalid credentials")
    login()
