# Project 3 : Automatic File Sorter
# Name : Anshu Pulipati
# Major : Computer Science

import os, shutil

path = r'C:\Users\anshu\Downloads\Python Tutorial\Automatic_Sorter\\'
if not os.path.exists(r'C:\Users\anshu\Downloads\Python Tutorial\Automatic_Sorter\\'):
    os.mkdir(r'C:\Users\anshu\Downloads\Python Tutorial\Automatic_Sorter\\')
os.listdir(path)
path = r'C:\Users\anshu\Downloads\Python Tutorial\Automatic_Sorter\\'
folder_names = ['CSV Files', 'Text Files', 'Image Files','TSV Files']
for folder in folder_names:
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)
file_names = os.listdir(path)
for file in file_names:
    if ".csv" in file and not os.path.exists(path + 'CSV Files\\' + file):
        shutil.move(path + file, path + 'CSV Files\\' + file)
    elif ".txt" in file and not os.path.exists(path + 'Text Files\\' + file):
        shutil.move(path + file, path + 'Text Files\\' + file)
    elif ".png" in file and not os.path.exists(path + 'Image Files\\' + file):
        shutil.move(path + file, path + 'Image Files\\' + file)
    elif ".tsv" in file and not os.path.exists(path + 'TSV Files\\' + file):
        shutil.move(path + file, path + 'TSV Files\\' + file)

