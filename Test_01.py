import os
import shutil
import PyPDF2
import tkinter as tk
from tkinter import simpledialog

def categorize_documents(source_folder, destination_folder):
    """
    Categorize documents in the source folder and move them to specific folders in the destination folder.

    Parameters:
    - source_folder (str): Path to the folder containing documents to be categorized.
    - destination_folder (str): Path to the folder where categorized documents will be moved.
    """
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Check if it's a known type and move to the corresponding folder
        if filename.lower().endswith('.pdf'):
            move_file(file_path, destination_folder, 'PDF')
        elif filename.lower().endswith('.doc'):
            move_file(file_path, destination_folder, 'DOC')
        elif filename.lower().endswith('.jpg'):
            move_file(file_path, destination_folder, 'JPG')
        elif filename.lower().endswith('.stl'):
            move_file(file_path, destination_folder, 'STL')
        elif filename.lower().endswith('.dxf'):
            move_file(file_path, destination_folder, 'DXF')
        elif filename.lower().endswith('.3mf'):
            move_file(file_path, destination_folder, '3MF')
        elif filename.lower().endswith('.txt'):
            move_file(file_path, destination_folder, 'TXT')
        else:
            # If the document type is unknown, prompt the user
            new_category = prompt_user_for_category(filename)
            if new_category:
                move_file(file_path, destination_folder, new_category)
            else:
                print(f"Skipped {file_path}")

def prompt_user_for_category(filename):
    """
    Prompt the user to input the category for a document.

    Parameters:
    - filename (str): Name of the document for which the category is requested.

    Returns:
    - str: User-inputted category name.
    """
    # Prompt the user for the category of the document
    root = tk.Tk()
    root.withdraw()
    user_input = simpledialog.askstring("Input", f"Enter the category for {filename}:")
    root.destroy()

    return user_input

def move_file(file_path, destination_folder, category):
    """
    Move a file to the specified category folder.

    Parameters:
    - file_path (str): Path to the file.
    - destination_folder (str): Path to the destination folder where the document will be moved.
    - category (str): Category name for the document.
    """
    category_folder = os.path.join(destination_folder, category)
    os.makedirs(category_folder, exist_ok=True)

    destination_path = os.path.join(category_folder, os.path.basename(file_path))
    shutil.move(file_path, destination_path)
    print(f"Moved {file_path} to {destination_path}")

# Example usage
source_folder = 'D:\\DIY\\Test_01'
destination_folder = 'D:\\DIY\\Test_02'

# Create example files for testing
test_files = [
    'document1.pdf',
    'document2.doc',
    'document3.jpg',
    'document4.stl',
    'document5.dxf',
    'document6.3mf',
    'document7.txt',
    'unknown_type.txt'
]

for file in test_files:
    with open(os.path.join(source_folder, file), 'w') as f:
        f.write("Sample content for testing.")

categorize_documents(source_folder, destination_folder)

