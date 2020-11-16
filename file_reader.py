import os
import sys

def scan_folder(parent):
    # iterate over all the files in directory 'parent'
    for file_name in os.listdir(parent):
        if file_name.endswith(".wav"):
            # if it's a txt file, print its name (or do whatever you want)
            print(file_name)
        else:
            current_path = "".join((parent, "/", file_name))
            if os.path.isdir(current_path):
                # if we're checking a sub-directory, recursively call this method
                scan_folder(current_path)

parent_path = '/home/anam/Desktop/Leipzig'
#scan_folder(parent_path)
shpfiles = []
for dirpath, subdirs, files in os.walk(parent_path):
    for x in files:
        if x.endswith(".wav"):
            print(os.path.join(dirpath, x))
            print("\n")
            print(os.path.split(dirpath))



