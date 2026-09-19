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


        for mall_id in mall_ids:

            activity_count = 0

            for line in read_lines('parking_records.txt'):
                stripped_line = line.strip()
                if stripped_line == '':
                    continue
                split_line_list = stripped_line.split(',')
                record_mall_id = split_line_list[2]

                if record_mall_id == mall_id:
                    activity_count += 1

            print(f"Mall ID: {mall_name}")
            print(f"Total Parking Activity: {activity_count}")
            print("---------------------------------")

        # ----------------------------------------------------------------------------------------------------------
        # 2. View Mall Revenue
        if owner_choice == 2:
            mall_ids = ["01", "02", "03"]
            malls = read_lines('malls.txt')

            for mall_id in mall_ids:

                # Find mall name
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
                for payment_line in read_lines('payments.txt'):
                    stripped_line = payment_line.strip()
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
            print(f"Mall ID: {mall_id}")
            print(f"Total Revenue: R{revenue:.2f}")
            print("---------------------------------")

            # ----------------------------------------------------------------------------------------------------------
            # 3. Reporting Stats

            if owner_choice = 3:

                mall_ids = ["01", "02", "03"]
                malls = read_lines('malls.txt')
                #iterate through every mall
                for mall_id in mall_ids:

                    #mall name check for reporting functions
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

                    activity_count = 0
                    revenue = 0

                    #Generate Parking Variables
                    for line in read_lines('parking_records.txt'):
                        stripped_line = line.strip()
                        if stripped_line == '':
                            continue
                        split_line_list = stripped_line.split(',')
                        record_mall_id = split_line_list[2]
                        if record_mall_id == mall_id:
                            activity_count += 1

                    # Generate Payment Variables
                    for payment_line in read_lines('payments.txt'):
                        stripped_payment_line = payment_line.strip()
                        if stripped_payment_line == '':
                            continue
                        split_payment = stripped_payment_line.split(',')
                        payment_record_id = split_payment[1]
                        payment_amount = float(split_payment[2])
                        #Search for matching parking record
                        for parking_line in read_lines('parking_records.txt'):
                            stripped_parking_line = parking_line.strip()
                            if stripped_parking_line == '':
                                continue
                            split_parking_line = stripped_parking_line.split(',')

                            parking_record_id = split_parking_line[0]
                            parking_mall_id = split_parking_line[2]

                            if parking_record_id == payment_record_id and parking_mall_id == mall_id:
                                revenue += payment_amount

                #For every Mall ID - Print relevant statistics
                print("---------------------------------")
                print(f"Mall ID: {mall_name}")
                print(f"Total Parking Activity: {activity_count}")
                print(f"Total Revenue: R{revenue:.2f}")
                print("---------------------------------")





