#!/usr/bin/env python3
# Code by JAL-code
# Create a json file from tab delimited text file.
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
    print("Loading the data")
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

# save an indent formatted json file.  Size is larger.
def save_list_of_items(data, datasave):
    with open(datasave, 'w') as file:
        json.dump(data, file, indent=4)

# save a json file for a compact size.
def save_compact_list_of_items(data, datasave):
    with open(datasave, 'w') as file:
        json.dump(data, file)

if __name__ == '__main__':
    indent = False
    # set the file names
    # set the record file
    record_file='sdr2023g.txt'
    # set the working file.  If working file is corrupted, reload the record file.
    working_file='sdr2023g_c.json'
    # set dir location
    working_dir = os.getcwd()
    relative_location = f"\\faa\\"
    # does this file exist in the working folder?
    default_folder = f"{working_dir}\\"
    print(f"{default_folder}\\{record_file}")
    if file_exists(record_file, default_folder):
        print("We can load the data!")
        data = load_products(f"{default_folder}{record_file}")
        if indent: 
            save_list_of_items(data, f"{default_folder}{working_file}")
        if not indent:
            save_compact_list_of_items(data, f"{default_folder}{working_file}")
    if not file_exists(working_file, default_folder):
        print("We must find the record file!")

#  Regex101 candidate: \s(?P<column>[c]+[\d]{1,3})\s+|(?P<columntype>[a-zA-Z]+)\s+|(?P<length>[\d]+)|(?P<description>\b[A-Za-z]+\s.*?\.\b)