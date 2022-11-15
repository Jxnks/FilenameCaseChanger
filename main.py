import os

# method to change all files to lowercase
def uppercase_files(path):
    for file in os.listdir(path):
        os.rename(path + file, path + file.upper())
        results = os.listdir(path)
        print(results)

# method to change all filenames to lowercase
def lowercase_files(path):
    for file in os.listdir(path):
        os.rename(path + file, path + file.lower())
        results = os.listdir(path)
        print(results)

# place full path directory below + "\"
uppercase_files(r"placehere")

# place full path directory below + "\"
lowercase_files(r"placehere")