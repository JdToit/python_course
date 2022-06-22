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

f = open('user.txt', 'r')
user_file = f.read().strip()
users = {}
counter = 0
for line in user_file.split('\n'):
    line_list = line.strip().split(', ')
    username = line_list[0]
    password = line_list[1]
    counter += 1
    users[counter] = {"username": username, "password": password}

# while loop
# while Found is false, it will run the code
# if Found is true, it will exit the program
# condition that checks if the user is a registered user
found = False
while not found:
    input_user = input("Please enter your username: ")
    input_password = (input("Please enter your password: "))
    for key, info in users.items():
        if input_user == info["username"] and input_password == info["password"]:
            username = info["username"]
            password = info["password"]
            found = True

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

    choose_option = input("Choose 'r' to register a new user\nChoose 'a' to add a task\nChoose 'va' to view all tasks,"
                          "\nChoose 'vm' to view tasks that are assigned to you\nChoose 'q' to quit: ")
# Code for if they choose to register a user
# Also double-checks that they answered their passwords correctly, else it prints an error and asks them to try again
    print("")
    if choose_option == 'r':
        print("")
        correct = False
        while not correct:
            new_username = input("New username: ")
            new_password = input("New password: ")
            confirm_password = input("Confirm password: ")
            break

        if new_password == confirm_password:
            print("")
            print("Registry successful")
            correct = True
            file = open('user.txt', 'a')
            file.write(new_username + ', ' + new_password + '\n')

        else:
            print("")
            print("Passwords do not match. Try again")
            print("")
# Code for if they choose to add a new task
# Asks for the name of the person, the title of the task, the description of the task, the date the task was assigned,
# and the due date of the task
# Writes all the details to 'tasks.txt'
# Option to quit once they're done adding tasks
    elif choose_option == 'a':
        enter_username = input("Enter the username of the employee: ")
        while enter_username == username:
            print("")
            print("Please enter a new task to be added")
            print("")
            new_task_name = input("Enter the username of the person the task is assigned to: ")
            new_task_title = input("Enter the title of the task: ")
            new_task_des = input("Describe the task: ")
            new_task_assi = input("The date that the task was assigned to the user: ")
            new_task_due = input("Enter the due date of the task: ")
            ask_continue = input("Would you like to add more tasks? Press y to continue. If not, press 'q' to quit ")
            file = open('tasks.txt', 'a+')
            content = file.read()

            if content.endswith('\n'):

                file.write(new_task_name + ", " + new_task_title + ", " + new_task_des + ", " + new_task_assi
                           + ", " + new_task_due + '\n')
            else:
                file.write('\n' + new_task_name + ", " + new_task_title + ", " + new_task_des + ", " + new_task_assi
                           + ", " + new_task_due + '\n')

            if ask_continue == 'q':
                print("")
                print("The task was added successfully")
                print("")
                break

            elif ask_continue == 'y':
                choose_option == 'a'

            else:
                print("")
                print("Error: Please choose either 'y' or 'q'")
                choose_option == 'a'


        else:
            print("This is not a registered user")

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

        f = open('tasks.txt', 'r')
        tasks = f.readlines()
        for i in tasks:
            if i.startswith(username):
                print("______________________________")
                print(i)


# code for if they want to quit the process
# finds 'quit' to be true, which ends the process
    elif choose_option == 'q':
        print("")
        print("Goodbye")
        print("")
        quit = True
# else code
# if the user did something other than what was written above, it will prompt an error message and run the program
# again
    else:
        print("")
        print("Error. Please try again.")
        print("")