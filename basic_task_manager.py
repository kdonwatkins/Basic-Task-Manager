#### This program will help a small business with its task delegation and tracking.

#### Please note I added 2 more users to the given text files so it's easier to check that things work properly with diffferent users :)

#### There are 3 stages to this program:

#### (1) Setup and User Login process
#### (2) Identify User's Objective
#### (3) Implement User's Objective (either 4 or 6 choices depending on user)


############################## STAGE 1: SETUP AND USER LOGIN PROCESS ##########################################


from datetime import date   # import current date for later on
date = str(date.today())

login_success = False       # booleans for loops
username_check = False
password_check = False
valid_choice = False

print("Greetings and welcome to our online task manager!")
print("Let's get you logged in to get started!")

user_file = open("user.txt", "r")                       # open and read relavant file
login = user_file.read()

user_name = str.lower(input("\nPlease enter your username here: "))       

while username_check == False:                                      
    
    if user_name in login:                              # verify user's username based on text file
        print("\nGreat! Username found! Now we just need your password!")
        username_check = True
        break
    elif user_name not in login:
        user_name = input("Username not found! Please reenter your username here: ")


user_pword = str.lower(input("Please enter your password here: "))

while username_check == True:
    
    if user_pword in login:                             # verify user's password based on text file
        print("Great! Password found!")
        login_success = True
        break
    elif user_pword not in login: 
        user_pword = input("No match! Please reenter your password here: ")

    
        
############################## STAGE 2: IDENTIFY USER'S OBJECTIVE ##############################################
        

if login_success == True and user_name != "admin":          # menu for non-Admin users
    print("""\nPlease select one of the following options:

    "A" - to add a task
    "VA" - to view all tasks
    "VM" - to view all of your tasks
    "E" - to exit/logout""")
    
elif login_success == True and user_name == "admin":        # menu for Admin users
    print("""\nPlease select one of the following options:

    "R" - to register a new user
    "A" - to add a task
    "VA" - to view all tasks
    "VM" - to view all of your tasks
    "S" - to view statistics
    "E" - to exit/logout""")

user_choice = str.lower(input("\nPlease type your choice (letter only): "))     # user enters choice here


############################## STAGE 3: IMPLEMENTING USER'S OBJECTIVE ###########################################

## CHOICE 1: Register a new user


while user_choice == "r" and user_name != "admin":                                          # this while loop is here to ensure only Admin is allowed to register new students
    user_choice = input("Sorry but only Admin can register new users. Please try again: ")  # "Register" is not in the menu for non-admin users but this loop is just in case they enter "r"!
    break

while valid_choice == False:
    
    if user_choice == "r" and user_name == "admin":
        print("Great! You would like to register a new user! You need to set a new username and password.")
        
        while user_choice == "r":
            user_name = input("\nPlease enter a new username: ")
            pword = input("Please enter a new password: ")          # user must confirm password, passwords must match otherwise they start again
            pword2 = input("Now reenter and confirm the pasword: ")
        
            if pword == pword2:
                valid_choice = True
                print("Great, your username and password have been stored in the 'user.txt' file.")
                
                with open("user.txt", "a") as user_file:                # if passwords match, username and password get written to text file
                    user_file.write("\n" + user_name + ", " + pword)
                    user_file.close()
                    break
                
            elif pword != pword2:
                valid_choice = False
                print("\nWhoops! Please try again!")
        
                
## CHOICE 2: Add a new task
        
    elif user_choice == "a":
        valid_choice = True
        print("\nGreat! You would like to add a task!")

        task_user = input("Please enter the username of the person the task is assigned to: ")  # user is prompted to enter all task details
        task_title = input("Please enter the title of the task: ")
        task_descrip = input("Please enter a description of the task: ")
        task_due = input("Please enter the due date of the task: ")
        
        with open("tasks.txt", "a") as user_file:                           # "append" here means we can write to the file without overwriting anything inside
            user_file.write(f"\n{task_user}, {task_title}, {task_descrip}, {date}, {task_due}, No") # current date module brought in here
            user_file.close()

            print("\nGreat! Your new task has been stored in the 'tasks.txt' file.")


## CHOICE 3: View all tasks
        
    elif user_choice == "va":
        valid_choice = True
        print("\nGreat! You would like to view all tasks! Here they are:")

        task_file = open("tasks.txt", "r")
        
        for line in task_file:
            details = line.strip().split(", ")      # this separates the task items equally as separate items
            
            print(f"\nTask:\t{details[0]}")         # all tasks neatly printed out for user
            print(f"Assigned to:\t{details[1]}")
            print(f"Task description:\t{details[2]}")
            print(f"Date Assigned:\t{details[3]}")
            print(f"Due Date:\t{details[4]}")
            print(f"Task Complete?\t{details[5]}")

        task_file.close()


## CHOICE 4: User views tasks only assigned to them
        
    elif user_choice == "vm":
        valid_choice = True
        print("Great! You will see your personal tasks below (IF you have any assigned to you)!")

        user_file = open("tasks.txt", "r")
        
        for line in user_file:
            details = line.strip().split(", ")          # this separates the task items equally as separate items
            
            if user_name in line:
                print(f"\nTask:\t{details[0]}")         # all the user's tasks neatly printed out for them
                print(f"Assigned to:\t{details[1]}")
                print(f"Task description:\t{details[2]}")
                print(f"Date Assigned:\t{details[3]}")
                print(f"Due Date:\t{details[4]}")
                print(f"Task Complete?\t{details[5]}")

        user_file.close()
        

## CHOICE 5: User (Admin only) wants to view statistics
        
    elif user_choice == "s":
        valid_choice = True
        print("\nGreat! You would like to see the current number of tasks and users!")
        
        task_count = 0
        user_count = 0
        
        user_file = open("tasks.txt", "r")
        for line in user_file:
            task_count += 1
          
        user_file2 = open ("user.txt", "r")
        for line in user_file2:
            user_count += 1

        print(f"\nThe total number of tasks is: {task_count}.")             # shows the number of total tasks
        print(f"The total number of registered users is: {user_count}.")    # shows the number of total registered users

        user_file.close()
        user_file2.close()
        

## CHOICE 6: User wants to exit program
        
    elif user_choice == "e":
        exit()


## Lastly, if the user doesn't select a valid choice in stage 2, they are reprompted to do so here:
        
    else:
        user_choice = input("Invalid input. Please reenter a valid choice (letter only): ")

