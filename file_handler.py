# ==========================================
# FILEHANDLER.PY
# ==========================================

# 1. Function to append to my files
def save_record(filename,line):
    with open(filename,'a') as f:
            f.write(line + '\n')

# 2. Function to read lines and return list of lines from txt file.
def read_lines(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()

    except FileNotFoundError:
        return []
