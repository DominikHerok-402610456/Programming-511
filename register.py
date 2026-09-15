# ==========================================
# REGISTER.PY
# ==========================================
"""Function relating to registering users."""
from file_handler import read_lines #Import read_lines
#Print Register Art
print('================================='+'\nRegister Page:'+'\n=================================\n')

#Main Register Function
def register():
    users = read_lines("users.txt")
    username_check = False

    username_is_taken = True #initially true, must be changed to false to continue

    while username_is_taken:
        entered_username = input("Please enter a unique username: ")

        if entered_username.lower() == stored_username.lower():
            print('A username match has been found, please try another')
        else:
            username_is_taken = False  # break the loop

    for line in users:

        #strip newlines and split by comma to get username and password and role
        stripped_line = line.strip()
        split_line_list = stripped_line.split(',')
        #Assign variables to the split list for username, password and role
        stored_username = split_line_list[0]

        #checks for if user name match, might do login again or prompt for another
        if entered_username.lower() == stored_username.lower():
            username_check = True







    if username_check == True:
        #
    else:
        password = input("Please enter your password: ")


register()
