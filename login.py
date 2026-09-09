# ==========================================
# LOGIN.PY
# ==========================================
'''Handles all login functions.'''
import re

from file_handler import read_lines

def login(username, password):
    user_list = read_lines('users.txt')
    split_list = user_list.split(',')

    for username,password in split_list:
        if username == username and password == password:
