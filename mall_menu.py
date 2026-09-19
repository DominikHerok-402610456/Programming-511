# ==========================================
# MALL_MENU.PY
# ==========================================

""" Display the mall menu and to handle driver choices."""

from file_handler import read_lines, save_record, write_records
from datetime import datetime
from pricing import pricing


def mall_menu(username, stored_mall_id):
    #
    # ----------------------------------------------------------------------------------------------------------
    malls = read_lines('malls.txt')
    for line in malls:

        stripped_line = line.strip()
        # Skip empty lines - Protection against traceback error
        if stripped_line == '':
            continue

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
        if stripped_line == '':
            continue
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
    # Persistent loop to handle driver choices
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
        # 1. Enter Parking
        # We must get the following info to complete the record: record_id,username,mall_id,entry_time,exit_time,fee
        entry_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        exit_time = ""
        fee = 0

        if mall_choice == 1:
            #Generate record_id for new record
            highest_id = 0
            for line in read_lines('parking_records.txt'):
                stripped_line = line.strip()
                if stripped_line == '':
                    continue
                split_line_list = stripped_line.split(',')
                record_list = split_line_list[0]

                record_id = int(record_list)
                if record_id > highest_id:
                    highest_id = record_id

            new_record_id = highest_id + 1
            #Check if there are spaces available, if so, save record using variables and save_record function
            if available_spaces > 0:
                #Check if user is already parked in this mall (check for duplicate entry in parking_records.txt)
                already_parked = False
                for line in read_lines('parking_records.txt'):
                    stripped_line = line.strip()
                    split_line_list = stripped_line.split(',')
                    stored_username = split_line_list[1]
                    record_mall_id = split_line_list[2]
                    exit_time_check = split_line_list[4]

                    if stored_username == username and exit_time_check == "" and record_mall_id == stored_mall_id:
                        already_parked = True
                        break


                if already_parked:
                    print("You are already parked in this mall!")

                else:
                    # Create the record string
                    new_record = f"{new_record_id:03d},{username},{stored_mall_id},{entry_time},{exit_time},{fee}"
                    save_record("parking_records.txt", new_record)
                    print("Parking Successful!")

            else:
                print("Parking Unsuccessful! No spaces available.")

        # ----------------------------------------------------------------------------------------------------------
        #2. Exit Parking - record_id,username,mall_id,entry_time,exit_time,fee

        if mall_choice == 2:
            active_record = None
            for line in read_lines('parking_records.txt'):
                stripped_line = line.strip()
                if stripped_line == '':
                    continue

                split_line_list = stripped_line.split(',')
                exit_record_id = split_line_list[0]
                exit_stored_username = split_line_list[1]
                exit_stored_mall_id = split_line_list[2]
                exit_stored_entry_time = split_line_list[3]
                exit_stored_exit_time = split_line_list[4]
                exit_stored_fee = split_line_list[5]

                #only if the username, exit_time is and mall_id match, then we have an active record
                if exit_stored_username == username and exit_stored_exit_time == "" and exit_stored_mall_id == stored_mall_id:
                    active_record = split_line_list
                    break

            if active_record == None:
                print('You are not currently parked in this mall. Please check in first.')
                continue


            # ----------------------------------------------------------------------------------------------------------#
            #Variables for time and parking calculations
            exit_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            #Update record with exit time - Convert to datetime object and calculate parking duration for record
            entry_datetime = datetime.strptime(exit_stored_entry_time, "%d-%m-%Y %H:%M:%S")
            exit_datetime = datetime.strptime(exit_time, "%d-%m-%Y %H:%M:%S")
            #Parking duration variables
            #1 minute = 60 seconds AND 1 hour = 60 minutes = 3600 seconds
            parking_duration_time = exit_datetime - entry_datetime
            parking_duration_seconds = parking_duration_time.total_seconds()
            parking_duration_remainder  =  parking_duration_seconds % 3600 #will be used for part there of calc
            parking_duration_complete_hours =  parking_duration_seconds // 3600
            # ----------------------------------------------------------------------------------------------------------#
            if parking_duration_remainder > 0:
                billable_hours = parking_duration_complete_hours + 1
            else:
                billable_hours = parking_duration_complete_hours

            fee = pricing(stored_mall_id,billable_hours)
            print('Exited Parking Successfully!')

            # ----------------------------------------------------------------------------------------------------------#
            #Update record with exit time and fee
            updated_records = []

            for line in read_lines('parking_records.txt'):
            # re check record now to see if exit time is empty
                stripped_line = line.strip()
                split_line_list = stripped_line.split(',')
                current_record_id = split_line_list[0]

                if current_record_id == active_record[0]:#only if Record_ID matches
                    split_line_list[4] = exit_time #update exit time
                    split_line_list[5] = str(fee) #update calculated fee into record currently being iterated

                updated_records.append(','.join(split_line_list))

                #read all records, copy into updated_records, write all records back with only the one that has been updated
                write_records('parking_records.txt', updated_records)



        # ----------------------------------------------------------------------------------------------------------
        # 3. View Parking Fee - record_id,username,mall_id,entry_time,exit_time,fee
        if mall_choice == 3:
            #Looping through updated records here
            for line in read_lines('parking_records.txt'):
                stripped_line = line.strip()
                if stripped_line == '':
                    continue
                split_line_list = stripped_line.split(',')
                fee_record_id = split_line_list[0]
                fee_stored_username = split_line_list[1]
                fee_stored_mall_id = split_line_list[2]
                fee_stored_exit_time = split_line_list[4]
                fee_stored_fee = float(split_line_list[5])


                if fee_stored_username == username and fee_stored_exit_time != '' and fee_stored_mall_id == stored_mall_id:
                    print(f"Your Parking Fee Total: R{fee_stored_fee:.2f}")



        # ----------------------------------------------------------------------------------------------------------
        # 4. Make Payment - payment_id,record_id,amount,paid_at
        if mall_choice == 4:
            # ----------------------------------------------------------------------------------------------------------
            # Make Payment section
            fee_record_id = None
            fee_amount = None
            for line in read_lines('parking_records.txt'):
                stripped_line = line.strip()
                if stripped_line == '':
                    continue
                split_line_list = stripped_line.split(',')
                fee_stored_record_id = split_line_list[0]
                fee_stored_username = split_line_list[1]
                fee_stored_mall_id = split_line_list[2]
                fee_stored_exit_time = split_line_list[4]
                fee_stored_fee = split_line_list[5]

                #only if conditions are met, update fee_record_id and fee_amount and carry down
                if fee_stored_username == username and fee_stored_exit_time != '' and fee_stored_mall_id == stored_mall_id:
                    fee_record_id = fee_stored_record_id
                    fee_amount = float(fee_stored_fee)
                    break
            #Check if fee_record_id is still NONE
            if fee_record_id is None:
                print('No outstanding parking fee found.')
                continue
            # ----------------------------------------------------------------------------------------------------------
            #Make a new payment logic
            payments_exists = False
            #Search through existing payments again and isolate variables
            for line in read_lines('payments.txt'):
                stripped_line = line.strip()
                if stripped_line == '':
                    continue
                split_line_list = stripped_line.split(',')
                payment_id = split_line_list[0]
                payment_record_id = split_line_list[1]
                payment_amount = float(split_line_list[2])
                payment_paid_at = split_line_list[3]
                #No payment if record already exists in payments.txt
                if payment_record_id == fee_record_id:
                    payments_exists = True
                    break
            if payments_exists:
                print('You have already paid. You may exit now')
            else:
                #otherwise move to payment
                highest_payment_id = 0

                for line in read_lines('payments.txt'):
                    stripped_line = line.strip()

                    if stripped_line == '':  # Ignore blank lines
                        continue

                    split_line_list = stripped_line.split(',')

                    payment_id = int(split_line_list[0])

                    if payment_id > highest_payment_id:
                        highest_payment_id = payment_id
                # generate new payment ID
                new_payment_id = highest_payment_id + 1
                new_payment_id = f"{new_payment_id:03d}"
                payment_paid_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                #Build new payment record
                new_payment = f"{new_payment_id},{fee_record_id},{fee_amount},{payment_paid_at}"
                save_record('payments.txt', new_payment)

                print('Payment successful!')
                print(f'Payment Amount: R{fee_amount:.2f}')
        # ----------------------------------------------------------------------------------------------------------
        # 5. View Payment/Parking History
        if mall_choice == 5:
            #will only be reading already made records and then displaying them for the user
            for line in read_lines('parking_records.txt'):
                stripped_line = line.strip()
                if stripped_line == '':  # Ignore blank lines
                    continue
                split_line_list = stripped_line.split(',')
                history_record_id = split_line_list[0]
                history_username = split_line_list[1]
                history_mall_id = split_line_list[2]
                history_entry_time = split_line_list[3]
                history_exit_time = split_line_list[4]
                history_fee = float(split_line_list[5])






        # ----------------------------------------------------------------------------------------------------------
        # 6. Return to Driver Menu
        if mall_choice == 6:
            print("Returning to Driver Menu")

