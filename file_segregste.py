import os
import shutil
import tkinter as tk
from tkinter import filedialog

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    folder_path = filedialog.askdirectory(title="Select Source Folder")
    return folder_path

def segregate_files(source_folder):
    # Define the target folders
    termo_folder = os.path.join(source_folder, 'Termo')
    wide_folder = os.path.join(source_folder, 'Wide')
    small_folder = os.path.join(source_folder, 'Small')
    other_folder = os.path.join(source_folder, 'Other')

    # Create target folders if they don't exist
    for folder in [termo_folder, wide_folder, small_folder, other_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # List all files and directories in the source folder
    entries = os.listdir(source_folder)

    # Segregate files and move directories
    for entry in entries:
        source_path = os.path.join(source_folder, entry)
        destination_path = None

        if os.path.isfile(source_path):
            if "_T" in entry:
                destination_path = os.path.join(termo_folder, entry)
            elif "_W" in entry:
                destination_path = os.path.join(wide_folder, entry)
            elif "_S" in entry:
                destination_path = os.path.join(small_folder, entry)
            else:
                destination_path = os.path.join(other_folder, entry)
        elif os.path.isdir(source_path):
            # If it's a directory, move it without checking the name
            destination_path = os.path.join(other_folder, entry)

        if destination_path:
            # Move the file or directory to the appropriate folder
            try:
                shutil.move(source_path, destination_path)
            except shutil.Error:
                # Handle the case where the destination already exists
                new_name = os.path.join(other_folder, "renamed_" + entry)
                shutil.move(source_path, new_name)

    print("File segregation completed.")

if __name__ == "__main__":
    # Use the select_folder function to get the source folder path
    source_folder_path = select_folder()

    if source_folder_path:
        # Call the function to segregate files
        segregate_files(source_folder_path)
    else:
        print("Folder selection canceled.")
