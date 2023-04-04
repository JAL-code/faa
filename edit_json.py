#!/usr/bin/env python3
# Code by JAL-code
# Process the document for supermarket items.
# Note this file is stage 2 for updating json formatting.

import os
import re 
import sys
import json

# SILENTMODE - should the user know if the file was found?
SILENTMODE = False

# check if file exists
def file_exists(filename, location):
    f_exists = False
    if not os.path.exists(filename):
        f_exists=False
        print(f"File {filename} does not exist!")
    else:
        print(f"Error, file {filename} already exists!")
        f_exists=True
        # sys.exit(1)
    return f_exists

# load the list of products
def load_products(file_name):
    print("Loading the products")
    # , encoding='utf8 ' replaced by 2nd line
    with open(file_name, 'r' , encoding='utf8') as data_file:  
        data_loaded = json.load(data_file)
    return data_loaded
#C:\Users\Joseph\Documents\GitHub\faa\title-14.json
# save an indent formatted json file.
def save_list_of_items(data, datasave):
    with open(datasave, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    # set the file names
    # set the record file
    record_file='title-14.json'
    # set the working file.  If working file is corrupted, reload the record file.
    working_file='title-14_w.json'
    # set dir location
    working_dir = os.getcwd()
    relative_location = f"\\faa\\"
    # does this file exist the working folder?
    default_folder = f"{working_dir}\\"
    print(f"{default_folder}\\{record_file}")
    if file_exists(record_file, default_folder):
        print("We can load the data!")
        data = load_products(f"{default_folder}{record_file}")
        save_list_of_items(data, f"{default_folder}{working_file}")
    if file_exists(working_file, default_folder)==False:
        print("We must find the record file!")