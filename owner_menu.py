# ==========================================
# OWNER/SHAREHOLDER_MENU.PY
# ==========================================

""" Display the OWNER/SHAREHOLDER menu and to handle choices."""

# ----------------------------------------------------------------------------------------------------------
from file_handler import read_lines
from datetime import datetime

# ----------------------------------------------------------------------------------------------------------
def owner_menu(username):

    owner_choice = 0

    while owner_choice != 4:

        print("=================================")
        print("          Owner Menu")
        print("=================================")
        print(f"Logged in user: {username}")
        print("1. View Mall Activity")
        print("2. View Mall Revenue")
        print("3. Compare Mall Performance")
        print("4. Logout")

        owner_choice = input("Enter your choice: ")

        if owner_choice.isdigit():
            owner_choice = int(owner_choice)

            if owner_choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please select 1-4.")
        else:
            print("Invalid input. Please enter a number.")
            owner_choice = 0

        # ----------------------------------------------------------------------------------------------------------
        # 1. View Mall Activity
        # ----------------------------------------------------------------------------------------------------------
        if owner_choice == 1:

            mall_ids = ["01", "02", "03"]

            for mall_id in mall_ids:

                mall_name = ''

                # Find the name of the current mall
                for line in read_lines('malls.txt'):

                    stripped_line = line.strip()

                    if stripped_line == '':
                        continue

                    split_line_list = stripped_line.split(',')

                    stored_id = split_line_list[0]
                    stored_name = split_line_list[1]
                    stored_capacity = split_line_list[2]

                    if stored_id == mall_id:
                        mall_name = stored_name
                        break

                # Count parking activity for this mall
                activity_count = 0
                current_vehicle_count = 0

                for line in read_lines('parking_records.txt'):
                    stripped_line = line.strip()
                    if stripped_line == '':
                        continue
                    split_line_list = stripped_line.split(',')
                    record_mall_id = split_line_list[2]
                    record_exit_time = split_line_list[4]
                    #Functionality for current vehicle count
                    if record_mall_id == mall_id:
                        activity_count += 1

                        if record_exit_time == '':
                            current_vehicle_count += 1

                    if record_mall_id == mall_id:
                        activity_count += 1

                print("---------------------------------")
                print(f"Mall: {mall_name}")
                print(f"Total Parking Activity: {activity_count}")
                print(f"Current Vehicles: {current_vehicle_count} / {stored_capacity}")
                print("---------------------------------")
        # ----------------------------------------------------------------------------------------------------------
        # 2. View Mall Revenue
        # ----------------------------------------------------------------------------------------------------------
        if owner_choice == 2:
            #List of set mall ids
            mall_ids = ["01", "02", "03"]
            malls = read_lines('malls.txt')

            for mall_id in mall_ids: #in mall id list

                # Find mall name assoscribed to mall id
                mall_name = ''
                for line in malls:
                    stripped_line = line.strip()
                    if stripped_line == '':
                        continue
                    split_line_list = stripped_line.split(',')
                    stored_id = split_line_list[0]
                    stored_name = split_line_list[1]

                    if stored_id == mall_id:
                        mall_name = stored_name
                        break

                revenue = 0
                #Pulling variables from Payments
                for line in read_lines('payments.txt'):
                    stripped_line = line.strip()
                    if stripped_line == '':
                        continue
                    split_payment = stripped_line.split(',')
                    payment_record_id = split_payment[1]
                    payment_amount = float(split_payment[2])

                    # Pulling variables from Parking Records for each payment
                    for parking_line in read_lines('parking_records.txt'):
                        stripped_parking_line = parking_line.strip()
                        if stripped_parking_line == '':
                            continue
                        split_parking_line = stripped_parking_line.split(',')
                        parking_record_id = split_parking_line[0]
                        parking_mall_id = split_parking_line[2]

                        if parking_record_id == payment_record_id and parking_mall_id == mall_id:
                            revenue += payment_amount
                #Final Revenue Print
                print("---------------------------------")
                print(f"Mall ID: {stored_name}")
                print(f"Total Revenue: R{revenue:.2f}")
                print("---------------------------------")

        # ----------------------------------------------------------------------------------------------------------
        # 3. Compare Mall Performance
        # ----------------------------------------------------------------------------------------------------------
        if owner_choice == 3:

            mall_ids = ["01", "02", "03"]
            malls = read_lines('malls.txt')

            for mall_id in mall_ids:

                mall_name = ''
                mall_capacity = 0
                pricing_type = ''

                # Find mall information
                for line in malls:

                    stripped_line = line.strip()

                    if stripped_line == '':
                        continue

                    split_line_list = stripped_line.split(',')

                    stored_id = split_line_list[0]
                    stored_name = split_line_list[1]
                    stored_capacity = split_line_list[2]
                    stored_pricing_type = split_line_list[3]

                    if stored_id == mall_id:
                        mall_name = stored_name
                        mall_capacity = int(stored_capacity)
                        pricing_type = stored_pricing_type
                        break

                # --------------------------------------------------
                # Counters
                current_vehicle_count = 0
                activity_count = 0
                completed_sessions = 0
                total_duration_minutes = 0
                outstanding_fees = 0
                revenue = 0

                # --------------------------------------------------
                # Read parking records
                for line in read_lines('parking_records.txt'):
                    stripped_line = line.strip()
                    if stripped_line == '':
                        continue
                    split_line_list = stripped_line.split(',')
                    record_mall_id = split_line_list[2]
                    entry_time = split_line_list[3]
                    exit_time = split_line_list[4]

                    # Only process records belonging to this mall
                    if record_mall_id == mall_id:
                        activity_count += 1

                        # Currently parked
                        if exit_time == '':
                            current_vehicle_count += 1

                        # Completed parking session
                        else:
                            completed_sessions += 1
                            try: #Try except needed for persisten value error
                                entry_datetime = datetime.strptime(entry_time, "%d-%m-%Y %H:%M:%S")
                            except ValueError:
                                entry_datetime = datetime.strptime(entry_time, "%Y-%m-%d %H:%M")

                            try:
                                exit_datetime = datetime.strptime(exit_time, "%d-%m-%Y %H:%M:%S")
                            except ValueError:
                                exit_datetime = datetime.strptime(exit_time, "%Y-%m-%d %H:%M")
                            duration = exit_datetime - entry_datetime
                            duration_minutes = duration.total_seconds() / 60
                            total_duration_minutes += duration_minutes

                # --------------------------------------------------
                # Calculate average parking duration
                if completed_sessions > 0:
                    average_duration_minutes = (total_duration_minutes / completed_sessions)
                else:
                    average_duration_minutes = 0

                # --------------------------------------------------
                # Calculate outstanding fees
                for line in read_lines('parking_records.txt'):

                    stripped_line = line.strip()

                    if stripped_line == '':
                        continue

                    split_line_list = stripped_line.split(',')

                    record_id = split_line_list[0]
                    record_mall_id = split_line_list[2]
                    exit_time = split_line_list[4]
                    fee = float(split_line_list[5])

                    # Only completed sessions for this mall
                    if record_mall_id == mall_id and exit_time != '':

                        payment_found = False

                        # Check whether record has been paid
                        for payment_line in read_lines('payments.txt'):

                            payment_stripped = payment_line.strip()

                            if payment_stripped == '':
                                continue

                            payment_split = payment_stripped.split(',')

                            payment_record_id = payment_split[1]

                            if payment_record_id == record_id:
                                payment_found = True
                                break

                        if payment_found is False:
                            outstanding_fees += fee

                # --------------------------------------------------
                # Calculate revenue
                for payment_line in read_lines('payments.txt'):

                    payment_stripped = payment_line.strip()

                    if payment_stripped == '':
                        continue

                    payment_split = payment_stripped.split(',')

                    payment_record_id = payment_split[1]
                    payment_amount = float(payment_split[2])

                    # Find the parking record linked to the payment
                    for parking_line in read_lines('parking_records.txt'):

                        parking_stripped = parking_line.strip()

                        if parking_stripped == '':
                            continue

                        parking_split = parking_stripped.split(',')

                        parking_record_id = parking_split[0]
                        parking_mall_id = parking_split[2]

                        if (parking_record_id == payment_record_id
                                and parking_mall_id == mall_id):
                            revenue += payment_amount
                            break

                # --------------------------------------------------
                # Display In Depth information
                print("=================================")
                print(f"MALL: {mall_name}")
                print("=================================")
                print(f"Current Vehicles: {current_vehicle_count} / {mall_capacity}")
                print(f"Total Parking Activity: {activity_count}")
                print(f"Total Revenue: R{revenue:.2f}")
                print(f"Average Parking Duration: {average_duration_minutes:.0f} minutes")
                print(f"Outstanding Fees: R{outstanding_fees:.2f}")
                print(f"Pricing: {pricing_type}")
                print("=================================")