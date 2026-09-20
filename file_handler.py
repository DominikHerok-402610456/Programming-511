# ==========================================
# FILEHANDLER.PY
# ==========================================
"""Functions that will be used to handle file operations."""

# ----------------------------------------------------------------------------------------------------------
# 1. Function to append to my files
# ----------------------------------------------------------------------------------------------------------
def save_record(filename,line):

    with open(filename,'a') as f:
        f.write(line + '\n')

# ----------------------------------------------------------------------------------------------------------
# 2. Function to read lines and return list of lines from txt file.
# ----------------------------------------------------------------------------------------------------------
def read_lines(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()

    except FileNotFoundError:
        return []

# ----------------------------------------------------------------------------------------------------------
# 3. Function to write records primarily for exit function in mall_menu.py
# ----------------------------------------------------------------------------------------------------------
def write_records(filename,records):
    with open(filename,'w') as f:
        for record in records:
            f.write(record + '\n')
