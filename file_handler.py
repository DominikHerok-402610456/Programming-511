# ==========================================
# FILEHANDLER.PY
# ==========================================

#Function to append to my files
def save_record(file_name,line):
    with open(file_name,'a') as f:
            f.write(line + '\n')

#Function to read lines and return list of lines from txt file.
def read_lines(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()

    except FileNotFoundError:
        return []
5