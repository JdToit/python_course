# This is a program that lets people add and view tasks to employees

# These are the different options a user can run
# 'r' stands for "register a new user"
# 'a' stands for "add a new task"
# 'va' stands for "view all tasks"
# 'vm' stands for "view my tasks"
# 'q' stands for "quit process"

# block of code that opens 'user.txt'
# counter to iterate over each line
# checks the username and password
# continues to the next line 
user_file = open('user.txt', 'r')
users = {}
counter = 0
for line in user_file:
    line_list = line.strip().split(', ')
    username = line_list[0]
    password = line_list[1]
    counter += 1
    users[counter] = {"username": username, "password": password}

choose_option = 'r' or 'a' or 'va' or 'vm' or 'q'

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

# Prompts the users for their username's and passwords
# input_user = input("Please enter your username: ")
# input_password = (input("Please enter your password: "))
print("")
print(f"You're logged in, {input_user}")
print("")
# This is the block of code where viewers must choose which option they want to run
quit = False
while not quit:
# They are prompted to choose an option
    print("Please choose one of the following: ")
    print("")
    choose_option = input("Choose 'r' to register a new user\nChoose 'a' to add a task\nChoose 'va' to view all tasks,"
                          "\nChoose 'vm' to view tasks that are assigned to you\nChoose 'q' to quit: ")
# Code for if they choose to register a user
# Also double-checks that they answered their passwords correctly, else it prints an error and asks them to try again
    print("")
    if choose_option == 'r':
        print("Please enter a new username and password")
        print("")
        new_username = input("New username: ")
        new_password = input("New password: ")
        confirm_password = input("Confirm password: ")
        while new_password != confirm_password:
            print("")
            print("Passwords do not match. Try again")
            print("")
            new_username = input("New username: ")
            new_password = input("New password: ")
            confirm_password = input("Confirm password: ")
        if new_password == confirm_password:
            print("")
            print("Registry successful")
# Code for if they choose to add a new task
# Asks for the name of the person, the title of the task, the description of the task, the date the task was assigned,
    # and the due date of the task
# Writes all the details to 'tasks.txt'
    elif choose_option == 'a':
        print("")
        print("Please enter a new task to be added")
        print("")
        new_task_name = input("Enter the username of the person the task is assigned to: ")
        new_task_title = input("Enter the title of the task: ")
        new_task_des = input("Describe the task: ")
        new_task_assi = input("The date that the task was assigned to the user: ")
        new_task_due = input("Enter the due date of the task: ")
        file = open('tasks.txt', 'a')
        file.write("Username of the person the task is assigned to: " + new_task_name + '\n' +
                   "Title of the task: " + new_task_title + '\n' +
                   "Description of the task: " + new_task_des + '\n' +
                   "The date the task was assigned to the user: " + new_task_assi + '\n' +
                   "Due date of the task: " + new_task_due + '\n' + '\n')
# code for if they choose to view all tasks of all people
# opens 'tasks.txt' and all the details in the file
    elif choose_option == 'va':
        print("")
        print("This is a display of all current tasks:")
        print("")
        f = open('tasks.txt', 'r')
        if f.mode == 'r':
            contents = f.read()
            print(contents)
            print("")
# code for if they want to view the tasks assigned to them
# opens the 'tasks.txt' file and reads the respective lines
    elif choose_option == 'vm':
        file = open('tasks.txt')
        content = file.readlines()
        print("tenth line")
        print({input_user})
        print("first three lines")
# code for if they want to quit the process
# finds 'quit' to be true, which ends the process
    elif choose_option == 'q':
        print("")
        print("Goodbye")
        print("")
        quit = True
# else code
# if the user did something other than what was written above, it will pront an error message and run the program again
    else:
        print("")
        print("Error. Please try again.")
        print("")

    file = open('user.txt', 'a')
    file.write("Username: " + input_user + '\n' + "Password: " + input_password + '\n' + '\n')