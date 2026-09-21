# ==========================================
# DISPLAY.PY
# ==========================================

'''Handles code relating to initial display of menu and choices for user. 1. Login, 2. Register, 3. Exit'''

from validation import validate_yes_no
from register import register_user
from login import login_user
from driver_menu import driver_menu
from admin_menu import admin_menu
from owner_menu import owner_menu

# ----------------------------------------------------------------------------------------------------------
def display_function():
    #while loop to check for choice continually
    choice = 0
    while choice != 3:

        print('================================='+'\nSmart Mall Parking System'+'\n================================='+'\n1. Login'+'\n2. Register'+'\n3. Exit')
        user_input = input("Please enter your choice: (1,2,3): ")
        #first check for strings
        if user_input.isdigit():
            choice = int(user_input)
        else:
            print('Please choose a number between 1 and 3')
            continue

        #if digit, check if 1,2,3 or anything else
        if choice == 1:
            #login.py
            # Remember to assign the function to a variable for the return
            login_result = login_user() # Returns role if successful, None if not
            if login_result is not None:
                username, role = login_result

                 #redirect to appropriate menu based on role
                if role == 'admin':
                    admin_menu(username)
                elif role == 'driver':
                    driver_menu(username)
                elif role == 'owner':
                    owner_menu(username)
                else:
                    print('Role not found. Please try again or contact support.')

        elif choice == 2:
            #register.py to register user
            #Remember to assign the function to a variable for the return
            registration_result = register_user()

            #if registration is successful, login user
            if registration_result is True:

                login_result = login_user()
                #Login user based off of role returned
                if login_result is not None:
                    username, role = login_result

                    # Redirect to appropriate menu based on role
                    if role == 'driver':
                        driver_menu(username)

                    else:
                        print('Role not found. Please try again or contact support.')


        #Check for yes and no inputs
        elif choice == 3:
            exit_choice = input('Are you sure you want to exit? Enter either Yes or No.')
            #save result to variable so not running more than once
            exit_result = validate_yes_no(exit_choice)
            #bring in valid choice and finish logic
            if exit_result is True:
                exit()
            elif exit_result is False:
                choice = 0
            else:
                print('Please enter either Yes or No.')
                choice = 0
# -----------------------------------------------------------------------------------------------------------------------------------


