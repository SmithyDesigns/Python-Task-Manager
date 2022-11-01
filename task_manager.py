'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

# =====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime

# ====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''


# used logic from https://stackoverflow.com/questions/68387927/how-do-i-prevent-duplication-in-my-text-file-when-asking-for-registration-from-c
def reg_user():
    # we get input from the user, and confirm their password
    new_user = input("Enter New User Name: ")
    new_user_password = input("Enter New User Password: ")
    new_user_password_confirm = input("Confirm password again: ")

    # validate new user password to see if it matches to created profile
    while new_user_password_confirm != new_user_password:
        new_user_password_confirm = input(
            "Confirm password again: ")  # if it does not match password then promt user again

    # opening user txt file to append new user to the user file
    with open('user.txt', 'a') as user_file:
        user_file.write(f"\n{new_user}, {new_user_password}")  # saving new user details to the txt file


def add_task():
    # ask user to enter task info
    adding_user = input("Enter a Username to add to task: ")
    task_title = input("Enter Title: ")
    task_description = input("Enter task discription: ")

    # suggested format printed for reference
    print("Format for due date of assigned task(10 Oct 2019)")
    task_due_date = input("Enter due date of assigned task: ")
    # date format create
    date_task_assigned = datetime.today()
    date_task_assigned = date_task_assigned.strftime("%d %b %Y")  # formatting the duedate
    task_completion = "No"

    # checking if task is overview
    if date_task_assigned == datetime.today():
        task_completion = "Yes"

    # writing content of task information back into the tasks file
    with open("tasks.txt", "a") as task_file:
        task_file.write(
            f"{adding_user}, {task_title}, {task_description}, {date_task_assigned}, {task_due_date}, {task_completion}\n")


def view_all():
    # open txt file and read the whole file
    with open("tasks.txt", "r") as task_file:
        content_s = task_file.readlines()  # reading all lines

        # user task description, duedaste, title and initial assigned date
        for line in content_s:
            adding_user, task_title, task_description, task_due_date, date_task_assigned, task_completion = line.split(
                ", ")
            print(f'''Added user: {adding_user}
                Task Title: {task_title}
                Task Description: {task_description}
                Due Date of Task: {task_due_date}
                Completed task Time: {date_task_assigned}
                ''')


def view_mine():
    # user = input("Enter user to get all specific tasks: ")
    number_of_user_tasks = 0
    alltask_dict = {}

    # open txt file and read the whole file 
    with open("tasks.txt", "r") as task_file:
        content_s = task_file.readlines()

        # reading each users task information independently and adding up totals
        for line in content_s:
            adding_user, task_title, task_description, task_due_date, date_task_assigned, task_completion = line.split(
                ", ")  # creating a list
            number_of_user_tasks += 1
            alltask_dict[number_of_user_tasks] = line.strip('\n').split(", ")  # creating a all task list

            if adding_user == username:
                print(number_of_user_tasks)

                print(f'''Added user: {adding_user}
                Task Title: {task_title}
                Task Description: {task_description}
                Due Date of Task: {task_due_date}
                Completed task Time: {date_task_assigned}
                Task Complete: {task_completion}
                ''')

        file_editor(alltask_dict)  # add task calls file editor function


def file_editor(task_dic):
    while True:
        # does admin want to edit file 
        task_selection = int(input("Select a task by entering a number or input ‘-1’ to return to the main menu: "))

        # exit if -1
        if task_selection == -1:
            break

        choice = input(f"""Choose an optiuon below:
    m - mark the task as complete 
    e - edit the task
    :""")
        print(task_dic[task_selection])

        # to change taks completion status
        if choice.lower() == "m":
            task_dic[task_selection][-1] = "Yes"

        # edit username or due date
        elif choice.lower() == "e":
            what_to_edit = (input('''Would you like to edit 
            u - Username
            dd - Due Date: ''')).lower()

            # editing username
            if what_to_edit == "u":
                updated_new_username = input("Enter new Username to update to: ")
                # go to position of username to update     
                task_dic[task_selection][0] = updated_new_username

            # editing duedate 
            elif what_to_edit == "dd":
                updated_new_due_date = input("Enter Due Date to update to: ")

                # go to position of due date to update to new duedate   
                task_dic[task_selection][-2] = updated_new_due_date

        print(task_dic)
    with open("tasks.txt", "w+") as file_upate:
        for x in task_dic:
            new_string = ", ".join(task_dic[x])
            file_upate.write(new_string + "\n")


def display_stats():
    print("Display Statistics:\n")
    # open new file to write tasks_overview
    with open("task_overview.txt", "w+") as task_oview:
        task_overview_generated()

    # open new file to write user_overview
    with open("user_overview.txt", "w+") as task_oview:
        user_overview_generated()


# generate task overview funct
def task_overview_generated():
    dictionary_of_tasks = {}  # create a dictionary of tasks
    tasks_completed = 0
    task_uncompleted = 0
    task_overdue = 0
    number_of_user_tasks = 0

    # open tasks file to add number of tasks per user 
    with open("tasks.txt", "r") as task_file:
        content_s = task_file.readlines()

        # username in dictionary list
        for line in content_s:
            # adding_user, task_title, task_description, task_due_date, date_task_assigned, task_completion =
            # line.split(", ")
            number_of_user_tasks += 1
            dictionary_of_tasks[number_of_user_tasks] = line.strip('\n').split(", ")

    # open file to  write and reads each task from function

    # line = username in username list 
    for line in content_s:
        task = line.strip('\n').split(", ")  # cleaning into a list
        print(task)

        # editing task completion and adding counters accordingly
        if task[-1].strip('\n') == 'Yes':
            tasks_completed += 1

        elif task[-1].strip('\n') == 'No':
            task_uncompleted += 1

        # comparing dates to check overdue status date_check = datetime_object
        # and formatting date to display
        date_check = datetime.strptime(task[-2], '%d %b %Y')

        # chicking if taks is overdue
        if date_check < datetime.today() and 'No' == task[-1].strip('\n'):
            task_overdue += 1

        # checking if dict is empty
        if len(dictionary_of_tasks) == 0:
            print("No items found")

        # calculations of %
        incompleted_percent = (task_uncompleted * 100) / (len(dictionary_of_tasks))
        overdue_percent = (task_overdue * 100) / (len(dictionary_of_tasks))

        # print and write to task overview file
        with open("task_overview.txt", "w+") as task_oview:
            task_oview.write(
                f"The total number of Tasks created, tracked using the Task Manager: {len(dictionary_of_tasks)}\n")
            task_oview.write(f"The total number of Completed Tasks: {tasks_completed}\n")
            task_oview.write(f"The total number of Uncompleted Tasks: {task_uncompleted}\n")
            task_oview.write(f"The total number of Tasks that are overdue: {task_overdue: .0f}\n")
            task_oview.write(f"The percentage of tasks that are incomplete: {incompleted_percent: .0f}%\n")
            task_oview.write(f"The percentage of tasks that are overdue: {overdue_percent: .0f}%\n")


def user_overview_generated():
    total_tasks_generated = 0

    # open file to read each task from txt
    with open("tasks.txt", "r") as task_file:
        content_s = task_file.readlines()
        total_tasks_generated = len(content_s)  # calc len of the list

        # open file to read each user from txt
        with open("user.txt", "r") as user_file:
            user_f = user_file.readlines()
            number_of_user_tasks = len(user_f)  # calc len of total users in list
            # writing to user overview file the required printouts
            with open("user_overview.txt", "w") as task_oview:
                # total assigned tasks to user
                task_oview.write(f"\t\t\tTotal number of tasks in system: {total_tasks_generated} \n")

                # for user un the opened user file 
                for line in user_f:
                    usern = line.split(", ")[0]
                    tasks_completed = 0
                    task_uncompleted = 0
                    task_overdue = 0
                    user_specific_tasks = 0

                    percent_uncompleted = 0
                    percent_completed = 0
                    percent_overdue = 0

                    # ceach taks in task file 
                    for line in content_s:
                        task = line.strip('\n').split(", ")  # cleaning data into list

                        # validating if user in user list matches with task number in order to add that task to thta
                        # user taks count
                        if usern == task[0]:
                            user_specific_tasks += 1

                            # checking task completion and addidn different counters
                            if task[-1].strip('\n') == 'Yes':
                                tasks_completed += 1

                            elif task[-1].strip('\n') == 'No':
                                task_uncompleted += 1

                            # comparing dates to check overdue status date_check = datetime_object
                            date_check = datetime.strptime(task[-2], '%d %b %Y')

                            # checking overdue status
                            if date_check < datetime.today() and 'No' == task[-1].strip('\n'):
                                task_overdue += 1

                    # paramaters to prevent zerovalueerror 
                    if user_specific_tasks > 0:
                        percent_uncompleted = (task_uncompleted / user_specific_tasks) * 100
                        percent_completed = (tasks_completed / user_specific_tasks) * 100

                    # percentage of overdue tasks calculation ***
                    if task_overdue > 0:
                        percent_overdue = (user_specific_tasks / total_tasks_generated) * 100

                    percent_usertasks = (user_specific_tasks / total_tasks_generated) * 100

                    task_oview.write(f"\n\t\t{usern}:\n")

                    # % task assigned to specific user
                    task_oview.write(f"Total number of assigned tasks for {usern}: {user_specific_tasks} \n")

                    # % completed tasks
                    task_oview.write(
                        f"Total percentage of complete assigned tasks for {usern}: {percent_completed}% \n")

                    # % uncompleted
                    task_oview.write(
                        f"Total percentage of incomplete assigned tasks for {usern}: {percent_uncompleted}% \n")

                    task_oview.write(f"Total percentage of overdue tasks for {usern}: {percent_overdue}% \n")

                    # % overdue
                    task_oview.write(f"Total percentage of total tasks assigned for {usern}: {percent_usertasks}% \n")

                # defining lists for password and users and opening taks file


user_file = open('user.txt', 'r')
username_list = []
password_list = []

# reading through lines of userfile
for line in user_file:
    data_list = line.strip('\n').split(", ")  # cleaning data into a list
    username_list.append(data_list[0])  # adding user to list
    password_list.append(data_list[1])  # adding password to list

# closing file 
user_file.close()

username = input("Enter Username: ").lower()

# validating if user is in list 
while not username in username_list:
    print('invalid user')
    username = input("Enter Username: ").lower()

# prompt for password to check if index match
password = input("Enter password: ")

# validating if password is in list of passwords
while not (password_list[username_list.index(username)] == password):
    print("wrong password")
    password = input("Enter password: ")

# success
print('Logged in')

# _______________________________Main Menu_____________________________________________________________
while True:
    # admin menu
    if username == 'admin':
        menu = input('''Select one of the following Options below
r - Registering a user.
a - Adding a task.
va - View all tasks.
vm - View my task.
gr - Generate Reports
ds - Display Stats: Number of Tasks and Users.
e - Exit. ''').lower()

    # user menu
    else:
        menu = input('''Select one of the following Options below
a - Adding a task.
va - View all tasks.
vm - view my task.
e - Exit. ''').lower()

    # if r is selected from Main Menu
    # prompt again for login details
    # if not equal to admin detail then denied and exit
    if menu == 'r' and username == 'admin':
        reg_user()

    # generate reports
    elif menu == 'gr':
        task_overview_generated()  # function called to generate both taks and user overview
        user_overview_generated()

    # ___________________________________back to main menu if a is selected_______________________________________________________
    # add task
    elif menu == 'a':
        add_task()

    # ___________________________________main menu va is selected_______________________________________________________
    # view all
    elif menu == 'va':
        view_all()

    # ___________________________________main menu vm is selected_______________________________________________________
    # view user own stats
    elif menu == 'vm':
        view_mine()

    # ________________________________main menu ds is selected__________________________________________
    # display stats but have to be admin
    elif menu == "ds" and username == 'admin':
        while True:
            try:
                with open("task_overview.txt", 'r') as task_overview:
                    with open("user_overview.txt", 'r') as user_overview:
                        task_overview = task_overview.read()
                        user_overview = user_overview.read()

            except FileNotFoundError:
                task_overview_generated()
                user_overview_generated()
                continue

            else:
                print(f"\n\t\tTask Overview:\n{task_overview}")
                print(f"\n\t\tUser Overview:\n{user_overview}")
                break

    # ___________________________________main menu e is selected_______________________________________________________
    # exit program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    # ___________________________________main menu exit_______________________________________________________

    # if user had chosen out of scope character
    else:
        print("You have made a wrong choice, Please Try again")
