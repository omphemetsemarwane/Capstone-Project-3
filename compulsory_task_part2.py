#this is a continuation of task_manager.py tasks#

#in this program only the user with the username admin is allowed to register users#

#the user is asked to enter their username and if their username is not "admin", they won't be allowed access to login#

#an appropriate error message will display if a user with a username that is not "admin" tries to login#

username = input("Enter username:")
if username != "admin":
    print("Your username is not admin, only the user with the username admin can register new users.")

#once the user enters a username "admin",the user is provided with a new menu option that allows them to display statistics and register a new user#

elif username == "admin":
    menu = (input("""
Please select one of the following options:
r - register a new user
d - display statistics = total number of tasks & users
e - exit
"""))

#if the user choose "r" (register a new user): the user should enter a new username and password#

#the user should be asked to confirm the password#

#to confirm if the new password matches the confirmed password a boolean statement True or False is used#

#if the confirmed password matches the new password, both username and password are stored in user.txt file in the order of (username, comma, space, password)#

    if menu == "r":
        new_username = (input("Enter a new username: "))
        new_username_password = (input("Enter a new password: "))
        new_password = False

        while new_password == False:
            confirmed_password = input("Re-enter your password for confirm: ")

            if new_username_password == confirmed_password:
                new_password = True

            elif new_password == False:
                print("Your passwords do not match!")

        with open("user.txt", "a") as f:
            f.write(str(new_username) + "," + " " + str(new_username_password) + "\n")

#if the user choose "d" (display statistics = total number of tasks & users), the total number of tasks and the total number of users are displayed in a user-friendly manner#

#to count the number of tasks and users both num_tasks and num_users variables are declaired zero(0)#

#both the increment variables num_tasks += 1 and num_user += 1 are used for the for loop to be exercuted#

#the task.txt file is opened using with open("tasks.txt", "r") as f: to calculate the total number of tasks stored in a task.txt file#

#the user.txt file is opened using with open("user.txt", "r") a f: to calculate the total number of users stored in user.txt file#

#the print() function is used to display the total number of tasks in tasks.txt and users in user.txt#

    elif menu == "d":

        num_tasks = 0
        num_users = 0

        with open("tasks.txt", "r") as f:
            for line in f:
                num_tasks += 1
        print("Total number of tasks: {}".format(num_tasks))

        with open("user.txt", "r") as f:
            for line in f:
                num_users += 1
        print("Total number of users: {}".format(num_users))

#if the user choose "e" (exit): the program will stop#

    elif menu == "e":
        exit