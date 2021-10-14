# Capstone-Project-III
# Files: Task Manager
# Project Information
# Description

This Task Manager is a programme written in Python programming language. This project was designed to help a small business in managing tasks assigned to each member of a team.
This programme assist a small business to create, store, display and edit tasks and other information to and from text files.

# Features (How it works)

When running the programme, the user will be presented with different fuctions that are used to perform certain actions when called out based on the user's choice from the menu. These functions are blocks of code that store certain information and then output certain results based on actions defined in that function.

After functions are declared, dictionaries and lists are used to store the user's and task's information from the programme. The text files ('user.txt' and 'tasks.txt') are opened and the existing information is stored in specific lists and dictionaries in the programme.

The programme is exercuted, allowing the user to login using with their username and password credentials. The programme also check if the user's credentials are correct by making sure that their 'username' and 'password' they entered matches the corresponding information in the specific 'passwords' and 'usernames' lists. If the 'username' and 'password' entered is incorrect, an appropriate error message is displayed and the programme will repeatedly ask the user to enter their credentials until they match the 'username' and 'password' information stored in the appropriate 'passwords' and 'usernames' lists.

Once the user's details are correct, a successful login message is displayed to the user and the user is presented with the menu options:
 > register users
 > add tasks
 > view all tasks
 > view tasks assigned to the user specifically
 > generate reports
 > or exit the program

Only the 'Admin' user has an extra option in their specific menu that allows them to 'display statistics' and 'generate reports'. These options are not available on other users menu. Specific letters are displayed with each menu option that the user can choose to select an option from the menu (the user can type vm to view my tasks):

> r - register a user
> a - add task
> va = view all tasks
> vm = view my tasks
> e - exit

A while loop is used to display the menu to the user, this is done so that after each option chosen by the user, the user will be able to go back to the main menu in order to select another option if they want or to exit the programme. The corresponding functions to the options in the menu are called out to perform certain actions when the user input the letter that matches to that menu option. 

EXAMPLE:

If the user input 'a' to add task, the fuction 'add_task()' is exercuted. This function ask the user to input all the information related to the task they want to add, (e.g the user is asked to input the username of the person the task is assigned to, the title of the task, the description of the task, the due date of the task, the date the task was assigned, whether or not the task is completed). This information is then added to a specific tasks dictionary and is written from the dictionary to a text file ('tasks.txt'). The same process is followed if the user chooses 'r' to register a user, the reg_user() fuction is exercuted. This function ask the user to input information related to the new user they wish to register(e.g the user is asked to enter a new username and password), if the new user credentials are correct (doesn't exist) they are stored in the appropriate 'usernames' and 'passwords' lists in the program. The users details are then written in the text file ('user.txt'). If they try to register an existing user, an appropriate error message is displayed



 
