
import os
import string

def rename_files():
    #1 Get file names

    directory = r"C:\Users\Anthony\Downloads\prank\prank"
    files = os.listdir(directory)
    #print(files)

    print(os.getcwd())
    saved_path = os.getcwd()
    os.chdir(directory)
    
    #2 Rename and display results

    #why does new file loop not work right?
    
    for file in files:
        print("Old file -" +file)
        os.rename(
            file, file.translate(
                str.maketrans(
                    string.ascii_letters, string.ascii_letters, string.digits)))       

    for file in files:
        print("New file -" +file)

    os.chdir(saved_path)
    print(saved_path)

rename_files()

