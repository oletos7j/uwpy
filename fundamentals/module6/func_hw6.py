#!/usr/bin/python3
'''
Author: Alex Sotelo
Python 3 required

Requirement(s):
In this activity you will learn to work with functions.

This project is very like the last one, but this time you will place the code you created for working with your ToDo.txt file into Functions.

Hint: Use the HW6_template.py.txtPreview the document

    Re-use the code from your previous assignment
    Following the instructions in the template, place your code into functions
    Test your script
    Upload your python script to canvas

'''
#uses path for the file path and name
path = "./Todo.txt"

#opens the Todo file in r mode
#the comma is used to split the values into two separate strings and removes the \n line delimiter
with open(path,"r") as f:
    lstTable = [row.split(",") for row in f.read().split("\n") if row]
    dicRow = dict(lstTable)
    print(dicRow)
    # closes the file...for now
    f.close()

#creates a showItems function to print the key and value of dictionary dictRow
def showItems(userInput):
    for key, val in userInput.items():
        print(key, val)

#creates an addItems function to append the dictRow dictionary
def addItems(userInput, addKey, newValue):
    userInput[addKey] = newValue

#creates a delItems function to delete the key if found in the dictRow dictionary
def delItems(userInput, Key):
    if Key in dicRow.keys():
        del dicRow[Key]
        print("Key name is deleted.")
    else:
        print("Key name was not found.")

#creates a saveItems function to reopen the file and save it using format option to add a new line
def saveItems(path, userInput):
    with open(path, "w") as f:
        for key, value in userInput.items():
            f.write('{},{}\n'.format(key, value))
    print(f"Saving this current list: {dicRow}")

#Displays a menu of choices to the user
def showMenu():
        print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
showMenu()

#creates a while loop inside the function to prompt user choices and uses functions to run the appropriate tasks
def showTodo():
    while(True):
        strChoice = str(input("Which option would you like to perform? [1 to 4] - \n"))

        #if user chooses 1, then call the showItems function
        if (strChoice.strip() == '1'):
            showItems(dicRow)

        #if user chooses 2, then call the addItems function and prints the dictRow
        elif(strChoice.strip() == '2'):
            addKey = str(input("What key name do you want to add?\n"))
            newValue = str(input("What value name do you want to assign the key?\n"))
            addItems(dicRow, addKey, newValue)
            print(dicRow)

        #if user chooses 3, then call the delItems function
        elif(strChoice.strip() == '3'):
            delKey = str(input("What key name do you want to delete?\n"))
            delItems(dicRow, delKey)

        #if user chooses 4, then save the current dicRow
        elif(strChoice == '4'):
            saveItems(path, dicRow)

        #breaks the loop if 5 is chosen
        elif (strChoice == '5'):
            break

showTodo()