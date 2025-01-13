import os

# Specify the directory you want to list
directory = '/'

# Use os.scandir() to list files and directories
with os.scandir(directory) as entries:
    for entry in entries:
        print(entry.name)

