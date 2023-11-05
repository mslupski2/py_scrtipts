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

    # List all files in the source folder
    files = os.listdir(source_folder)

    # Segregate files based on their names
    for file in files:
        source_path = os.path.join(source_folder, file)

        if "_T" in file:
            destination_path = os.path.join(termo_folder, file)
        elif "_W" in file:
            destination_path = os.path.join(wide_folder, file)
        elif "_S" in file:
            destination_path = os.path.join(small_folder, file)
        else:
            destination_path = os.path.join(other_folder, file)

        # Move the file to the appropriate folder
        shutil.move(source_path, destination_path)

    print("File segregation completed.")

if __name__ == "__main__":
    # Use the select_folder function to get the source folder path
    source_folder_path = select_folder()

    if source_folder_path:
        # Call the function to segregate files
        segregate_files(source_folder_path)
    else:
        print("Folder selection canceled.")
