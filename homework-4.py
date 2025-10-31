login_details = {"user1": "1234"}

username = input("Enter your username: ")

if username in login_details:
    password = input("Enter your password: ")

    if login_details[username] == password:
        print("Welcome!")
    else:
        print("Access denied.")
else:
    print("Username not found.")
    new_username = input("Enter a new username to register: ")
    new_password = input("Enter a new password: ")

    login_details[new_username] = new_password
    print("registration successful!")
    print("Update login details:", login_details)