#!/usr/bin/python3
'''
Author: Alex Sotelo
Python 3 required, re library is required for regex
Requirement(s): 1. Create a text file called Todo.txt using the following data, one line per row:

Clean House,low

Pay Bills,high

2. When the program starts, load each row of data from the ToDo.txt text file into a Python list.

Tip: You can use the readlines() method to import all lines as a list.

3. After you load the data into a list, loop through the list and add each item as a "key,value" pair a new dictionary.

Tip: Look back through the lecture notes at "split" and "indexing".

4. After you have added existing data to the dictionary, use the menu structure included in the template to allow the user to Add or Remove tasks from the dictionary using numbered choices.

Tip: Here's a refresher (Links to an external site.)Links to an external site. on working with dictionaries.

For deleting: Use "if" statements to see if the dictionary key a user inputs is in the dictionary, and if it is delete.

For adding: "If" the user wants to add items, ask them for a key, value pair to add to the dictionary by creating a new key and setting it's value to the value input by the user. Follow the syntax:

my_dictionary["key_name"] = new_value

Something like this would work:

    Menu of Options

    1) Show current data

    2) Add a new item.

    3) Remove an existing item.

    4) Save Data to File

    5) Exit Program

6. Save the data from the table into the Todo.txt file when the program exits.
'''

#imports the re module for regex
import re

#initializes the strData variable
strData = ""

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"

#opens the Todo file in r mode
#the comma is used to split the values into two separate strings and removes the \n line delimiter
with open("./Todo.txt","r") as f:
    lstTable = [row.split(",") for row in f.read().split("\n") if row]
    #once list is created, it is converted into a dictionary
    dicRow = dict(lstTable)
    #closes the file...for now
    f.close()

# Step 2 - Display a menu of choices to the user
    while(True):
         print ("""
         Menu of Options
            1) Show current data
            2) Add a new item.
            3) Remove an existing item.
            4) Save Data to File
            5) Exit Program
            """)
         strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
         print()#adding a new line

         # Step 3 -Show the current items in the table
         if (strChoice.strip() == '1'):
             #do a simple print of the current dictionary
            print(dicRow)

            # Step 4 - Add a new item to the list/Table
         elif(strChoice.strip() == '2'):
             #prompts user for a Key string
            Key = str(input("What key name do you want to add?\n"))
             #prompts user for a Value string
            Value = str(input("What value name do you want to assign the key?\n"))
             #Adds the new values as a new entry of the dictionary
            dicRow[Key] = Value
             #creates a list out of the new value
            addList = [Key, Value]
             #appends the newly created list to our initialized list
            lstTable.append(addList)
             #does a print of the current dictionary
            print(dicRow)

            # Step 5 - Remove a new item to the list/Table
         elif(strChoice.strip() == '3'):
            #prompts user for the key to be deleted
            Key = input("What key name do you want to delete?\n")
            # if the key is found, then delete it and print the current dictionary value
            if Key in dicRow:
                del dicRow[Key]
                print("Key name is deleted.")
                print(dicRow)
            else:
                # if not found, do nothing but print the current dictionary value and display 'Key not was not found'
                print("Key name was not found.")
                print(dicRow)
            #for loop to look at items in the dictionary to remove the key from the list
            for Key, Value in dicRow.items():
                remList = [Key, Value]
                lstTable.remove(remList)

            # Step 6 - Save tasks to the ToDo.txt file
         elif(strChoice == '4'):
             #for loop to look at all rows of the list
            for lines in lstTable:
                #uses the strData we previously initialized to add a extra line to each row
                strData += str(f'{lines}\n')
                #uses the imported re module to remove the brackets and replace them with nothing throughout the string
                strData = re.sub(f"[\[\]()']", "", strData)
                #uses the replace method to remove the extra line
                strData = strData.replace(", ", r",")

                #opens the file in write mode to replace everything with the new values
                with open("./Todo.txt", "w") as f:
                    f.write(strData)
            #prints out what is actually being saved
            print(f"Saving this current list: {lstTable}")

        #closes the file
         elif (strChoice == '5'):
            f.close()
            break

