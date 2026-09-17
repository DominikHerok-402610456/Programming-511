# ==========================================
# MALL_MENU.PY
# ==========================================

""" Display the mall menu and to handle driver choices."""

from file_handler import read_lines

def mall_menu(stored_mall_id):
    # ----------------------------------------------------------------------------------------------------------
    malls = read_lines('malls.txt')
    for line in malls:

        stripped_line = line.strip()
        split_line_list = stripped_line.split(',')
        mall_id = split_line_list[0]
        mall_name = split_line_list[1]
        mall_capacity = split_line_list[2]
        pricing_type = split_line_list[3]

        if mall_id == stored_mall_id:
            print(f'{mall_name} has {mall_capacity} seats and pricing is {pricing_type}')
            break
    # ----------------------------------------------------------------------------------------------------------
    # Calculate info needed for mall_menu capacity and current_vehicles inital display
    current_vehicles = 0
    for line in read_lines('parking_records.txt'):
        stripped_line = line.strip()
        split_line_list = stripped_line.split(',')

        # IF exit time is not recorded, then car is still parked
        mall_id = split_line_list[2]
        exit_time = split_line_list[4]
        # State duplication no manual check
        # Check if mall_id matches the stored_mall_id and only counts exit time if true
        if mall_id == stored_mall_id:
            # add 1 to current_vehicles if exit time is empty
            if exit_time == '':
                current_vehicles += 1
    # ----------------------------------------------------------------------------------------------------------
    available_spaces = int(mall_capacity) - current_vehicles
    print("=================================")
    print(f"   {mall_name}")
    print("=================================")
    print(f"Currently Parked Vehicles: {current_vehicles} ")
    print(f"Maximum Parking Capacity: {mall_capacity}")
    print(f'Spaces currently available: ',+available_spaces,'/',+int(mall_capacity))
    print("---------------------------------")
    print("1. Enter Parking")
    print("2. Exit Parking")
    print("3. View Parking Fee")
    print("4. Make Payment")
    print("5. View Payment/Parking History")
    print("6. Return to Driver Menu")

    # ----------------------------------------------------------------------------------------------------------
    # Functions for choice 1-6
    mall_choice = 0
    while mall_choice != 6:

        mall_choice = input("Please enter your choice: ")
        if mall_choice.isdigit():
            #if correct input type, convert to int and assign back to variable for use
            mall_choice = int(mall_choice)
            if mall_choice in range(1, 7):
                mall_choice = int(mall_choice)
            else:
                print('Please enter a valid choice between 1 and 6')
        else:
            print("Please enter a valid number")

        # ----------------------------------------------------------------------------------------------------------
        if mall_choice == 1:
            if available_spaces > 0:
                print("Parking Successful!")
                #use save record? 
            else:
                print("Parking Unsuccessful! No spaces available.")





            print(f"Current Parking Capacity: {current_vehicles}")

        # ----------------------------------------------------------------------------------------------------------


        if mall_choice == 2:
            print("")

        if mall_choice == 3:
            print("Parking Fee coming soon!")

        if mall_choice == 4:
            print("Payment coming soon!")

        if mall_choice == 5:
            print("Payment History coming soon!")

        if mall_choice == 6:
            print("Returning to Driver Menu")


mall_menu('02')
