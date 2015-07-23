# Jim Griffin 
# Written 6/9/15

# This converts basespace formatted data to a new format.
# import things, define function, define old path to data and output directory
# take files, break and collect the parts I want (3rd directory and file)

import glob
import os
import fnmatch
import shutil

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

path_in = "/Users/jimbo/Basespace/George - Jim-23067045/"
new_dir = "/Users/jimbo/Desktop/6.9.15_seq_data/"
new_sub_dir = new_dir + "unpaired/"

if not os.path.exists(new_dir):
    os.makedirs(new_dir)
    
    
for filename in find_files(path_in, '*.gz'):
    split_file = filename.split("/")
    if not os.path.exists(new_sub_dir):
        os.makedirs(new_sub_dir)
    shutil.copy(filename, new_sub_dir+split_file[-1])


