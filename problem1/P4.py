import os

# using / for the main directory and path

path = "/Seasons"  # Change this to your directory

# get the list of the directories

contents = os.listdir(path)

# get the each item from the directory and print it

for item in contents: print(item)