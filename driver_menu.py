# ==========================================
# DRIVER_MENU.PY
# ==========================================

""" Display the driver menu and handle driver choices."""

from file_handler import read_lines
from validation import validate_yes_no

def driver_menu():
    print("=================================")
    print("          Driver Menu")
    print("=================================")
    print("1. Select Mall")
    print("2. Enter Parking")
    print("3. Exit Parking")
    print("4. View Parking Fee")
    print("5. Make Payment")
    print("6. View Parking/Payment History")
    print("7. Logout")

    # ----------------------------------------------------------------------------------------------------------
    # For loop to iterate through each line in malls.txt and isolate each variable
    for line in read_lines('malls.txt'):
        stripped_line = line.strip()
        split_line_list = stripped_line.split(',')
        mall_id = split_line_list[0]
        mall_name = split_line_list[1]
        mall_capacity = split_line_list[2]
        pricing_type = split_line_list[3]

    driver_choice = 0
    #Menu Function
    while driver_choice != 7:
        # ----------------------------------------------------------------------------------------------------------
        driver_choice = input("Please enter your choice: ")

        # first check for correct input type
        if driver_choice.isdigit():
            #if correct input type, convert to int and assign back to variable for use
            driver_choice = int(driver_choice)
        else:
            continue


        #----------------------------------------------------------------------------------------------------------
        #Mall Selection Logic:
        if driver_choice == 1:
            print("Available Malls:")

            #go through each line in malls.txt and isolate each variable, to display

            for line in read_lines('malls.txt'):
                stripped_line = line.strip()
                split_line_list = stripped_line.split(',')
                mall_id = split_line_list[0]
                mall_name = split_line_list[1]
                mall_capacity = split_line_list[2]
                pricing_type = split_line_list[3]
                print(f"{int(mall_id)}. {mall_name}")


            mall_choice = input("Please enter the number of the mall you would like to park in: ")
            if mall_choice.isdigit():
                mall_choice = int(mall_choice)

            else:
                print("Please enter a valid number that corresponds to a mall.")


        # ----------------------------------------------------------------------------------------------------------
        #LOGOUT logic using validate_yes_no function
        elif driver_choice == 7:
            logout_choice = input("Are you sure you want to logout? Enter either Yes or No.")
            logout_result = validate_yes_no(logout_choice)
            if logout_result is True:
                exit()
            elif logout_result is False:
                driver_choice = 0
            else: #or if NONE
                print("Please enter either Yes or No.")
                driver_choice = 0



driver_menu()