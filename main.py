# Import os module for file and directory operations
import os
# Import shutil module for moving files
import shutil

# Prompt user to enter the folder path to organize
FOLDER_PATH = input("Enter the path of the folder to organize: ")

# Define a dictionary mapping folder names to their corresponding file extensions

FILE_TYPES = {
    "PDFs": [".pdf"],
    "Word_Files": [".docx", ".doc"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv"],
    "Text_Files": [".txt"]
}

# Loop through each folder in FILE_TYPES dictionary

for folder in FILE_TYPES:

    # Create the full path for the folder by joining FOLDER_PATH with folder name
    folder_path = os.path.join(FOLDER_PATH, folder)

    # Check if the folder does not already exist
    if not os.path.exists(folder_path):

        # Create the folder if it doesn't exist
        os.mkdir(folder_path)

# Loop through all items in the specified folder path
for file in os.listdir(FOLDER_PATH):

    # Create the full file path by joining FOLDER_PATH with the filename
    file_path = os.path.join(FOLDER_PATH, file)

    # Check if the current item is a directory
    if os.path.isdir(file_path):

        # Skip directories and continue to the next item
        continue

    # Extract the file extension and convert it to lowercase
    ext = os.path.splitext(file)[1].lower()

    # Loop through each folder and its corresponding file extensions
    for folder, extensions in FILE_TYPES.items():

        # Check if the file extension matches any of the extensions for this folder
        if ext in extensions:

            # Move the file to the corresponding folder
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file))
            break
print("Files have been organized into folders based on their types ✓.")