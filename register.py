# ==========================================
# REGISTER.PY
# ==========================================

"""Function relating to registering users."""

# ----------------------------------------------------------------------------------------------------------
from file_handler import read_lines
from file_handler import save_record
# ----------------------------------------------------------------------------------------------------------
#Main Register Function
# ----------------------------------------------------------------------------------------------------------
def register_user():

    # Print Register Art
    print('=================================' + '\nRegister Page:' + '\n=================================\n')

    # ----------------------------------------------------------------------------------------------------------
    while True: #persist check for username

        entered_username = input("Please enter a username. (It may consist of only letters and can include numbers. No spaces are allowed. (e.g JohnDoe123)): ")
        #Validation -
        if not entered_username.isalnum():
            print("Username may only contain letters and numbers. No spaces are allowed.")
            continue
        users = read_lines("users.txt")
        username_exists = False

        for line in users:

            #Break down each line into a list of strings
            stripped_line = line.strip()
            split_line_list = stripped_line.split(',')
            stored_username = split_line_list[0] # Assign variables to the split list for username like in login.py

            if entered_username.lower() == stored_username.lower():
                username_exists = True
                break # no need to check the rest of the lines if the username already exists

        if username_exists == True:
            print('Username already exists. Please choose a different username.')
            continue

        else:
            print('Username is available!')
            break
    # ----------------------------------------------------------------------------------------------------------
    #Register User to text file
    # ----------------------------------------------------------------------------------------------------------
    entered_password = input("Please enter your new password:")
    new_user = entered_username + "," + entered_password + ",driver"
    save_record("users.txt",new_user)
    print('Welcome to Smart Mall Parking System!\n'+'Username:'+entered_username+'\nPassword:'+entered_password+'\n'+'Role:Driver')
    return True #return true to indicate successful registration. This will kick back to display for user login
# ----------------------------------------------------------------------------------------------------------