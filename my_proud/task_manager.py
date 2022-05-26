users = {
1: {"username": "John", "password": "123"},
2: {"username": "James", "password": "555"}
}

found = False
while not found:
    input_user = input("Please enter your username: ")
    input_password = (input("Please enter your password: "))
    for key, info in users.items():
        if input_user == info["username"] and input_password == info["password"]:
            username = info["username"]
            password = info["password"]
            found = True
            break
    else:
        print("Wrong username or password. Please try again.")

print(f"You're logged in {username}")










