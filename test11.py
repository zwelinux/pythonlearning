user = "zlh"
pwd = "12345678"

username = input("Enter your username : ")
password = input("Enter your password : ")

if username == user and password == pwd:
    print("Hello " , username)

elif username == user and password != pwd:
    print("Wrong Password")

elif username != user or password != pwd:
    print("Username or Password Wrong")

else:
    print("Something went wrong. Try again")