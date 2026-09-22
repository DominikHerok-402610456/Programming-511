# ==========================================
# DRIVER_MENU.PY
# ==========================================

""" Display the driver menu and handle driver choices."""

from file_handler import read_lines, save_record
from mall_menu import mall_menu
from validation import validate_yes_no


def driver_menu(username):

    # ----------------------------------------------------------------------------------------------------------
    # For loop to iterate through each line in malls.txt and isolate each variable
    # ----------------------------------------------------------------------------------------------------------
    for line in read_lines('malls.txt'):
        stripped_line = line.strip()
        split_line_list = stripped_line.split(',')
        mall_id = split_line_list[0]
        mall_name = split_line_list[1]
        mall_capacity = split_line_list[2]
        pricing_type = split_line_list[3]

    driver_choice = 0
    stored_mall_id = None
    stored_mall_name = None

    #Menu Function
    while driver_choice != 5:
        print("=================================")
        print("          Driver Menu")
        print("=================================")
        print(f"Logged in user: {username}")
        print("1. Select Mall")
        print("2. View Parking Fee")
        print("3. Make Payment")
        print("4. View Parking/Payment History")
        print("5. Logout")

        # ----------------------------------------------------------------------------------------------------------
        driver_choice = input("Please enter your choice: ")

        # first check for correct input type
        if driver_choice.isdigit():
            #if correct input type, convert to int and assign back to variable for use
            driver_choice = int(driver_choice)
        else:
            continue


        #----------------------------------------------------------------------------------------------------------
        # 1. Mall Selection Logic:
        # ----------------------------------------------------------------------------------------------------------
        if driver_choice == 1:
            print("---------------------------------")
            print("Available Malls:")
            print("---------------------------------")

            #go through each line in malls.txt and isolate each variable, to display
            #Main FOR loop to display malls
            for line in read_lines('malls.txt'):
                stripped_line = line.strip()
                split_line_list = stripped_line.split(',')
                mall_id = split_line_list[0]
                mall_name = split_line_list[1]
                mall_capacity = split_line_list[2]
                pricing_type = split_line_list[3]
                print(f"{int(mall_id)}. {mall_name}")


            #second FOR loop to search for selected mall
            while True:

                mall_choice = input("Please enter the number of the mall you would like to park in: ")
                if mall_choice.isdigit():
                    mall_choice = int(mall_choice)



                mall_exists = False

                for line in read_lines('malls.txt'):

                    stripped_line = line.strip()
                    split_line_list = stripped_line.split(',')
                    mall_id = split_line_list[0]
                    mall_name = split_line_list[1]
                    if int(mall_id) == mall_choice:
                        print(f'You have selected {mall_name}')
                        stored_mall_id = mall_id
                        stored_mall_name = mall_name
                        mall_exists = True
                        break
                        #change to mall_menu

                if mall_exists:
                    break
                else:
                    print('Please enter a valid mall number.')
                    continue



            mall_menu(username,stored_mall_id)


        # ----------------------------------------------------------------------------------------------------------
        # 2. View Parking Fee:
        # ----------------------------------------------------------------------------------------------------------
        if driver_choice == 2:

            # Check if a mall has been selected
            if stored_mall_id is None:
                print("Please select a mall first.")
                continue

            fee_found = False

            # Search through parking records
            for line in read_lines('parking_records.txt'):

                stripped_line = line.strip()
                if stripped_line == '':
                    continue
                split_line_list = stripped_line.split(',')

                # Isolate parking record information for use in FEE CALC
                fee_record_id = split_line_list[0]
                fee_username = split_line_list[1]
                fee_mall_id = split_line_list[2]
                fee_entry_time = split_line_list[3]
                fee_exit_time = split_line_list[4]
                fee_amount = float(split_line_list[5])

                # Find completed parking records belonging to this user at the currently selected mall
                # SAME as mall menu
                if (fee_username == username and fee_mall_id == stored_mall_id and fee_exit_time != ''):
                    print("---------------------------------")
                    print("         Parking Fee")
                    print("---------------------------------")
                    print(f"Record ID: {fee_record_id}")
                    print(f"Entry Time: {fee_entry_time}")
                    print(f"Exit Time: {fee_exit_time}")
                    print(f"Parking Fee: R{fee_amount:.2f}")
                    print("---------------------------------")

                    fee_found = True

            # No completed parking record was found
            if fee_found is False:
                print("No completed parking fee found for the selected mall.")
        # ----------------------------------------------------------------------------------------------------------
        # 3. Make Payment
        # ----------------------------------------------------------------------------------------------------------
        # Take same logic from mall menu
        if driver_choice == 3:

            # Check if a mall has been selected
            if stored_mall_id is None:
                print("Please select a mall first.")
                continue

            fee_record_id = None
            fee_amount = None

            # Search parking records for a completed parking session
            for line in read_lines('parking_records.txt'):
                stripped_line = line.strip()
                if stripped_line == '':
                    continue
                split_line_list = stripped_line.split(',')
                record_id = split_line_list[0]
                record_username = split_line_list[1]
                record_mall_id = split_line_list[2]
                exit_time = split_line_list[4]
                record_fee = float(split_line_list[5])

                #Check if variables are valid first
                if (record_username == username and record_mall_id == stored_mall_id and exit_time != ''):
                    fee_record_id = record_id
                    fee_amount = record_fee
                    break

            # Check whether a completed parking fee was found
            if fee_record_id is None:
                print("No parking fee found to pay.")
                continue

            # Check whether this parking record has already been paid
            payment_exists = False

            for line in read_lines('payments.txt'):
                stripped_line = line.strip()
                if stripped_line == '':
                    continue
                split_line_list = stripped_line.split(',')
                payment_record_id = split_line_list[1]
                if payment_record_id == fee_record_id:
                    payment_exists = True
                    break

            if payment_exists:
                print("This parking fee has already been paid.")
                continue

            # Generate the next payment ID
            highest_payment_id = 0
            for line in read_lines('payments.txt'):
                stripped_line = line.strip()
                if stripped_line == '':
                    continue
                split_line_list = stripped_line.split(',')
                payment_id = int(split_line_list[0])
                if payment_id > highest_payment_id:
                    highest_payment_id = payment_id

            new_payment_id = highest_payment_id + 1
            new_payment_id = f"{new_payment_id:03d}"

            # Get payment timestamp
            from datetime import datetime
            paid_at = datetime.now().strftime("%Y-%m-%d %H:%M")

            # Create payment record
            new_payment = f"{new_payment_id},{fee_record_id},{fee_amount},{paid_at}"

            save_record("payments.txt", new_payment)

            print("---------------------------------")
            print("       Payment Successful")
            print("---------------------------------")
            print(f"Payment ID: {new_payment_id}")
            print(f"Parking Record: {fee_record_id}")
            print(f"Amount Paid: R{fee_amount:.2f}")
            print(f"Paid At: {paid_at}")
            print("---------------------------------")

        # ----------------------------------------------------------------------------------------------------------
        # 4. View Parking/Payment History:
        # ----------------------------------------------------------------------------------------------------------
        if driver_choice == 4:

            if stored_mall_id is None:
                print("Please select a mall first.")
                continue

            history_found = False

            print("---------------------------------")
            print("      Parking/Payment History")
            print("---------------------------------")

            for line in read_lines('parking_records.txt'):

                stripped_line = line.strip()

                if stripped_line == '':
                    continue

                split_line_list = stripped_line.split(',')

                history_record_id = split_line_list[0]
                history_username = split_line_list[1]
                history_mall_id = split_line_list[2]
                history_entry_time = split_line_list[3]
                history_exit_time = split_line_list[4]
                history_fee = float(split_line_list[5])

                # Only show this driver's records for the selected mall
                if (history_username == username
                        and history_mall_id == stored_mall_id):

                    history_found = True

                    print("---------------------------------")
                    print(f"Record ID: {history_record_id}")
                    print(f"Entry Time: {history_entry_time}")

                    if history_exit_time == '':
                        print("Exit Time: Still Parked")
                        print("Fee: Not yet calculated")
                    else:
                        print(f"Exit Time: {history_exit_time}")
                        print(f"Fee: R{history_fee:.2f}")

                    # Look for payment associated with this parking record
                    payment_found = False

                    for payment_line in read_lines('payments.txt'):
                        payment_stripped = payment_line.strip()
                        if payment_stripped == '':
                            continue
                        payment_split = payment_stripped.split(',')
                        history_payment_id = payment_split[0]
                        history_payment_record_id = payment_split[1]
                        history_payment_amount = float(payment_split[2])
                        history_paid_at = payment_split[3]

                        if history_payment_record_id == history_record_id:
                            payment_found = True
                            print(f"Payment ID: {history_payment_id}")
                            print(f"Amount Paid: R{history_payment_amount:.2f}")
                            print(f"Paid At: {history_paid_at}")
                            break

                    if payment_found is False and history_exit_time != '':
                        print("Payment Status: Not Paid")

            if history_found is False:
                print("No parking history found for the selected mall.")

            print("---------------------------------")

        # ----------------------------------------------------------------------------------------------------------
        # 5. Logout
        # ----------------------------------------------------------------------------------------------------------
        if driver_choice == 5:
            logout_choice = input("Are you sure you want to logout? Enter either Yes or No: ")
            logout_result = validate_yes_no(logout_choice)
            if logout_result is True:
                print("Logging out.")
                return

            elif logout_result is False:
                driver_choice = 0

            else:
                print("Please enter either Yes or No.")
                driver_choice = 0
