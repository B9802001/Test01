import os
import shutil
import PyPDF2
import tkinter as tk
from tkinter import simpledialog
from pathlib import Path

source_folder = 'D:\\DIY\\Test_01'
destination_folder = 'D:\\DIY\\Test_02'

def search_file(file_name, directory):
    for root, dirs, files in os.walk(directory):
        if file_name in files:
            return file_name
    return None
    

def categorize_documents(source_folder, destination_folder):

    for filename_source in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename_source)

        if  filename_source.lower().endswith('psm'):
            symbolname = Path(file_path).stem
            print(symbolname)
            file_path2 = os.path.join(source_folder, symbolname) + '.dra'
            print(file_path2)           


        if  filename_source.lower().endswith('fsm'):
            symbolname = Path(file_path).stem
            print(symbolname)
            file_path2 = os.path.join(source_folder, symbolname) + '.dra'
            file_path3 = search_file(filename_source, destination_folder)
            
            if  filename_source == search_file(filename_source, destination_folder):
                print('YES')
            else :
                print('No same file')


        if  filename_source.lower().endswith('ssm'):
            symbolname = Path(file_path).stem
            print(symbolname)
            file_path2 = os.path.join(source_folder, symbolname) + '.dra'
            file_path3 = search_file(filename_source, destination_folder)
            
            if  filename_source == search_file(filename_source, destination_folder):
                print('YES')
            else :
                print('No same file')


        if  filename_source.lower().endswith('pad'):
            symbolname = Path(file_path).stem
            print(symbolname)

                                    
categorize_documents(source_folder, destination_folder)
