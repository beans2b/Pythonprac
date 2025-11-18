correct_username = "admin"
correct_password = "password123"

type_username = input("Type username: ").strip()
type_password = input("Type password: ").strip()

if ((type_username == correct_username) and (type_password == correct_password)):
    print("Login Successful!")
else: 
    print("Invalid Username or Password")  
