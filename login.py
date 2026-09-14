# ==========================================
# LOGIN.PY
# ==========================================
"""Handles all login functions."""

from file_handler import read_lines

#collect user input for username and password:
print('================================='+'\nLogin Page:'+'\n=================================\n')
users = read_lines("users.txt")

def login():
    entered_username = input("Please enter your username: ")
    username_check = False
    users = read_lines("users.txt")
    #FOR loop to iterate through each line in users.txt
    for line in users:

        #strip newlines and split by comma to get username and password and role
        stripped_line = line.strip()
        split_line_list = stripped_line.split(',')
        #Assign variables to the split list for username, password and role
        stored_username = split_line_list[0]
        stored_password = split_line_list[1]
        role = split_line_list[2]
        #IF Statement to check if username and password match
        #compare username to user input
        print("Checking:",stored_username)
        print(repr(entered_username))
        print(repr(stored_username))

        if entered_username.lower() == stored_username.lower():
            #Only if username is correct, compare password
            password_check = False
            username_check = True


            #apparently better to do while not as password_check is bool

            password_counter = 0
            while password_counter != 3:
                entered_password = input("Please enter your password: ")
                if entered_password == stored_password:
                    print('Login Successful!')
                    return role #will be used elsewhere to determine what to do
                else:
                    print('Incorrect password. Please try again.')
                    password_counter += 1
            print('Too many incorrect password attempts. Please try again later.')
            return None #Break out of the for loop to stop further checks

    #if still no user found after checks, prompt and give register ability as well
    if username_check == False:
        print('No user found with that username. Please try again or register in the main menu.')
        return None



print(users)
login()

