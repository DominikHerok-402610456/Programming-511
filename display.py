# ==========================================
# DISPLAY.PY
# ==========================================
'''Handles code relating to initial display of menu and choices,
redirecting from there.'''

from validation import validate_yes_no

def display_function():
    #while loop to check for choice continually
    choice = 0
    while choice != 3:

        print('================================='+'\nSmart Mall Parking System'+'\n================================='+'\n1. Login'+'\n2. Register'+'\n3. Exit')
        user_input = input("Please enter your choice: ")
        #first check for strings
        if user_input.isdigit():
            choice = int(user_input)
        else:
            print('Please choose a number between 1 and 3')
            continue

        #if digit, check if 1,2,3 or anything else
        if choice == 1:
            #login.py
            print(choice)
        elif choice == 2:
            #register.py
            print(choice)

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


