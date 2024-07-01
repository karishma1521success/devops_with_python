import os
# importing os module to get all files names using os.listdir(foldername) - method ( to get list of all folders and files inside dir folder name)
# os.listdir(foldername)  - is just like ls command in linux

#project -  list all files in all provided folders given by users
# input - list of all folders names        output - list of all files in all folders


#steps to perform task

#1. read input of all foldernames from the user(folder) and make a list of that all folder names
folders = input("Enter all folder names with some spaces in between: ").split(" ")    # str.split(sep) - converts string into list
# print(folders)  # output - [fold1, fold2, fold3, fold4, ....]

#2. apply for loop on folders
for folder in folders:
    
    #exception handling

    try:
        files = os.listdir(folder)  # return list of all files within folder
    except FileNotFoundError:
        print("you have input wrong folder name looks like doesn't exist:  " , folder)
        break
    except PermissionError:
        print("You don't have perimission to access folder :  ",folder)
        break


    #4. identify module (os module) - there is an inbuilt module(os module - import os) to get all the files within a folder in python 
    print("*****listing files for the folder -- " , folder  )

    #3. insilde for loop list all files name of each folder
    for file in files:
        print(file) #5. print file names


#6. handle errors - means suppose you input that folder name which doesn't exist so handle this suitation
#SUITATION1 -  folder doesn't exist (means wrong folder name input)
#SUITATION2 - folder exist but it's empty has no files in it
#SUITATION3 - folder exist but don't have access permision

# exception handling - when you want to handle error or exception when you are okay with error but don't want program to terminate so you use exception handling


