# ==========================================
# PARKING_ADMIN_MENU.PY
# ==========================================

""" Display the admin menu and to handle admin choices."""

# ----------------------------------------------------------------------------------------------------------
from file_handler import read_lines
from datetime import datetime

# ----------------------------------------------------------------------------------------------------------

def admin_menu(username):

    #Selecting which mall
    admin_mall_choice = 0
    while admin_mall_choice not in [1, 2, 3]:

        print("===============================")
        print("      Select Admin Mall")
        print("===============================")
        print("1. Gateway Theatre of Shopping")
        print("2. Pavilion Shopping Centre")
        print("3. La Lucia Mall")

        admin_mall_choice = input("Please select the mall: ")

        if admin_mall_choice.isdigit():
            admin_mall_choice = int(admin_mall_choice)

            if admin_mall_choice not in [1, 2, 3]:
                print("Invalid choice. Please select 1, 2 or 3.")
        else:
            print("Invalid input. Please enter a number.")
            admin_mall_choice = 0

        if admin_mall_choice == 1:
            stored_mall_id = "01"
        elif admin_mall_choice == 2:
            stored_mall_id = "02"
        elif admin_mall_choice == 3:
            stored_mall_id = "03"

    for line in read_lines('malls.txt'):#mall_id,name,capacity,pricing_type
        stripped_line = line.strip()
        if stripped_line == '':
            continue
        split_line_list = stripped_line.split(',')
        mall_id = split_line_list[0]
        mall_name = split_line_list[1]
        mall_capacity = split_line_list[2]
        mall_pricing_type = split_line_list[3]

        if mall_id == stored_mall_id:
            print(f"Mall Name: {mall_name}")
            print(f"Mall Capacity: {mall_capacity}")
            print(f"Mall Pricing Type: {mall_pricing_type}")
            break




    #Menu selections
    admin_choice = 0
    while admin_choice != 4:

        #Display section - in while loop for persistence
        print("=================================")
        print("          Parking Admin Menu")
        print("=================================")
        print(f"Logged in user: {username}")
        print(f"Current Mall: {mall_name}")
        print(f"Maximum Capacity: {mall_capacity}")
        print("1. View Current Vehicles")
        print("2. View Parking Capacity")
        print("3. View Daily Activity")
        print("4. Logout")

        # get choice
        admin_choice = input("Enter your choice: ")
        # validate numeric input
        if admin_choice.isdigit():
            #if correct input type, convert to int and assign back to variable for use
            admin_choice = int(admin_choice)
        else:
            print("Invalid input. Please enter a number.")



        # ----------------------------------------------------------------------------------------------------------
        # 1. View Currently Parked Vehicles
        # ----------------------------------------------------------------------------------------------------------
        #Will read from parking records.
        if admin_choice == 1:

            vehicle_count = 0


            for line in read_lines('parking_records.txt'):
                stripped_line = line.strip()

                if stripped_line == '':
                    continue

                split_line_list = stripped_line.split(',')
                #assign variables for record restructure and display
                admin_record_id = split_line_list[0]
                admin_username = split_line_list[1]
                admin_mall_id = split_line_list[2]
                admin_entry_time = split_line_list[3]
                admin_exit_time = split_line_list[4]

                if admin_mall_id == stored_mall_id and admin_exit_time == '':
                    #Print every record and add to counter
                    vehicle_count += 1
                    print("---------------------------------------------------------------------------------------")
                    print(f"Record ID: {admin_record_id} Username: {admin_username} Entry Time: {admin_entry_time}")
                    print("---------------------------------------------------------------------------------------")

            if vehicle_count == 0:
                print("No vehicles are currently parked.")
            else:
                print(f"Currently parked vehicles: {vehicle_count}")

        # ----------------------------------------------------------------------------------------------------------
        # 2. View Parking Capacity
        # ----------------------------------------------------------------------------------------------------------
        # Will read from parking records.
        if admin_choice == 2:
            #Same counter to count vehicles, will compare against total mall capacity in calcs
            vehicle_count = 0

            for line in read_lines('parking_records.txt'):

                stripped_line = line.strip()
                if stripped_line == '':
                    continue
                split_line_list = stripped_line.split(',')
                admin_mall_id = split_line_list[2]
                admin_exit_time = split_line_list[4]

                if admin_mall_id == stored_mall_id and admin_exit_time == '':
                    vehicle_count += 1

            #set calc variables
            available_spaces = int(mall_capacity) - vehicle_count
            occupancy_percentage = (vehicle_count / int(mall_capacity)) * 100
            print(f"Currently Parked Vehicles: {vehicle_count}")
            print(f"Maximum Parking Capacity: {mall_capacity}")
            print(f"Available Spaces: {available_spaces}")
            print(f"Current Occupancy: {occupancy_percentage:.1f}%") #added for enhanced capacity metrics



        # ----------------------------------------------------------------------------------------------------------
        # 3. View Daily Activity
        # ----------------------------------------------------------------------------------------------------------
        # Will read from parking records.
        if admin_choice == 3:

            daily_activity_count = 0



            for line in read_lines('parking_records.txt'):

                stripped_line = line.strip()
                if stripped_line == '':
                    continue
                split_line_list = stripped_line.split(',')
                admin_record_id = split_line_list[0]
                admin_username = split_line_list[1]
                admin_mall_id = split_line_list[2]
                admin_entry_time = split_line_list[3]
                admin_exit_time = split_line_list[4]

                today = datetime.now().date()
                entry_datetime = datetime.strptime(admin_entry_time, "%d-%m-%Y %H:%M:%S")

                if admin_mall_id == stored_mall_id and entry_datetime.date() == today:
                    daily_activity_count += 1


        # ----------------------------------------------------------------------------------------------------------
        # 4. Logout
        # ----------------------------------------------------------------------------------------------------------
        if admin_choice == 4:
            print('Returning to main menu.')
            return