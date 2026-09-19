# ==========================================
# VALIDATION.PY
# ==========================================

'''Handles Validation functions.'''

# ----------------------------------------------------------------------------------------------------------
#Main Validation for exit choice on display function
#ONLY returns state
def validate_yes_no(exit_choice):
    exit_choice = exit_choice.strip().upper()
    if exit_choice == 'YES':
        return True
    elif exit_choice == "NO":
        return False
    else:
        return None
# ----------------------------------------------------------------------------------------------------------
