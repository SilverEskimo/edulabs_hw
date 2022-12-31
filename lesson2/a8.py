# Implement a program that receives a string that represents the full path to the file in the user's computer, and does the following:
# Checks whether the path is a valid Windows or macOS/Linux path and prints an error if the path is invalid.
# For this exercise, valid path is defined as follows:
# For Windows, the path should look like this:
# C:\Users\Documents\my files\doc1.docx
# Valid Windows path for the sense of this exercise should start from uppercase letter followed by semicolon (:) and backslash (\).
# The rest of the folders in the path should be separated by the backslash as well. The filename should have an extension.
# For macOS and Linux, the path should look like this:
# /Users/valeria/src/qgis_technion/qgis_test_proj.qgz
# Valid Linux-like paths or the sense of this exercise should start from slash(/). All the directories should be divided by slash as well,
# and the file should have extension as well
# Print the depth of the path (amount of folders starting from the root folder)
# Print the filename without file’s extension
# Print file’s extension

user_path = input("Please enter a full file path: ").strip()
valid = False

# Check if the path starts with the legal prefixes
if not (user_path[0].isupper() and user_path[1:].startswith(":\\") or user_path.startswith("/")):
    print("Invalid path - wrong prefix")

# Check if the path does not contain "." or if the path ends with "."
elif ("." not in user_path.split("\\") or "." not in user_path.split("/")) and \
        user_path[-1] == ".":
    print("Invalid path - no file extension")
else:
    valid = True

if valid:
    if user_path.__contains__("\\"):
        path = user_path.split("\\")
    else:
        path = user_path.split("/")
    file_name, extension = path[-1].split(".")
    print(f"The path is valid!\nThe depth is: {len(path[1:-1])}\nThe file's name is: {file_name}\nThe file's "
          f"extension is: {extension}")










