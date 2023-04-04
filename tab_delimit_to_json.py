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

# load the lines of data into a dictionary list
def load_products(file_name):
    print("Loading the products")
    # , encoding='utf8 ' replaced by 2nd line
    with open(file_name, 'r' , encoding='utf8') as data_file:  
        data_loaded = data_file.readlines()

    # Get the column names from first line of file
    columns = data_loaded[0].strip().split('\t')

    # Initialize an empty list to hold dictionaries
    processed_data = []

    # process the data lines (exclude first line)
    for line in data_loaded[1:]:
        # Split the line into a list of values
        values = line.strip().split('\t')
        # Create a dictionary with the column names as keys and the values as values
        row = dict(zip(columns, values))
        processed_data.append(row)    
    return processed_data

# save an indent formatted json file.
def save_list_of_items(data, datasave):
    with open(datasave, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    # set the file names
    # set the record file
    record_file='sdr2023g.txt'
    # set the working file.  If working file is corrupted, reload the record file.
    working_file='sdr2023g_w.json'
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