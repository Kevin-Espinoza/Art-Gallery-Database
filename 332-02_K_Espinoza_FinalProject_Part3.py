#****************************************************************************************************************************
#  Program name: "Art Gallery DB".  This program uses a MySQL sql script to save a database named Art Gallery. This file is
#  a Python3 program with a UI that lets the user: Print the records, Access any record based off of a primary key, Sort a 
#  report according to style, and Produces a second report showing customers whose art preference is the same as shown in any 
#  given art show. This program uses static sql as it does not not allow modification of the Art Gallery DB. 
#  Copyright (C) 2020 Kevin Espinoza                           
#****************************************************************************************************************************

#****************************************************************************************************************************
#  Program: Art Gallery DB
#  Author information
#  Author name: Kevin Espinoza
#  Author email: k.espinoza1012@csu.fullerton.edu
#  Due Date: 2020-Dec-09
#
#  Purpose:
#  The purpose of this file is to open and query a Database: "Art Gallery DB". 
#
#  This file:
#  File name: 332-02_K_Espinoza_FinalProject_Part3.py
#  Compile and Run: Windows -- py 332-02_K_Espinoza_FinalProject_Part3.py
#                   Linux   -- python3 332-02_K_Espinoza_FinalProject_Part3.py
#  Language: Python 3
#*****************************************************************************************************************************



import os               # Library to add commands to the terminal;  'clear'
import tkinter as tk    # Library for working UI
import mysql.connector  # Library for all MySQL functionality



#==========================================================================================#
#=====  Database Connector  =====  Database Connector  =====  Database Connector  =========#
#==========================================================================================#

# Create a connection to the Art Gallery Database
art_gallery = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Leslieboo1",
    database="Art_Gallery"
)

# Create a cursor to navigate the database
art_gallery_cursor = art_gallery.cursor()

#==========================================================================================#
#=====  Database Connector  =====  Database Connector  =====  Database Connector  =========#
#==========================================================================================#




#==========================================================================================#
#=====  Database Functions  =====  Database Functions  =====  Database Functions  =========#
#==========================================================================================#

# Clear the terminal
def clear():

    # Windows
    try:
        os.system('cls')
    # Linux
    except:
        os.system('clear')



# Print the entire DB
def printDB():

    # Clear the terminal
    clear()

    # Make an object to hold Artist table and print it to te terminal
    art_gallery_cursor.execute("SELECT * FROM Artist")  
    artGallery = art_gallery_cursor.fetchall()
    print("Artists: ")
    for x in artGallery:
        print(x)

    # Make an object to hold Art_Work table and print it to te terminal
    art_gallery_cursor.execute("SELECT * FROM Art_Work")
    artGallery = art_gallery_cursor.fetchall()
    print("\nArt_Works: ")
    for x in artGallery:
        print(x)

    # Make an object to hold Art_Shows table and print it to te terminal
    art_gallery_cursor.execute("SELECT * FROM Art_Shows")
    artGallery = art_gallery_cursor.fetchall()
    print("\nArt_Shows: ")
    for x in artGallery:
        print(x)

    # Make an object to hold Customer table and print it to te terminal
    art_gallery_cursor.execute("SELECT * FROM Customer")
    artGallery = art_gallery_cursor.fetchall()
    print("\nCustomers: ")
    for x in artGallery:
        print(x)



# Access any record based on attribute values
def getRecord():

    # Clear the terminal
    clear()

    # Check the Artist table for user input and save data if they match
    sql = "SELECT * FROM Artist WHERE Name = %s OR Phone = %s OR Address = %s OR Birth_Place = %s OR Age = %s OR Style_of_Art = %s"
    temp = (str(getRecordEntry.get()), str(getRecordEntry.get()), str(getRecordEntry.get()), str(getRecordEntry.get()), str(getRecordEntry.get()), str(getRecordEntry.get()), )   
    art_gallery_cursor.execute(sql, temp)  
    customerArtPreferences = art_gallery_cursor.fetchall()

    # Check the Art_Work table for user input and save data if they match
    sql = "SELECT * FROM Art_Work WHERE Title = %s OR Artist = %s OR Type_of_Art = %s OR Date_of_Creation = %s OR Date_Aquired = %s OR Price = %s OR Location = %s"
    temp = (str(getRecordEntry.get()), str(getRecordEntry.get()), str(getRecordEntry.get()), str(getRecordEntry.get()), str(getRecordEntry.get()), str(getRecordEntry.get()), str(getRecordEntry.get()), )      
    art_gallery_cursor.execute(sql, temp)  
    customerArtPreferences += art_gallery_cursor.fetchall()

    # Check the Art_Shows table for user input and save data if they match
    sql = "SELECT * FROM Art_Shows WHERE Date_and_Time = %s OR Artist = %s OR Contact = %s OR Contact_Phone = %s OR Location = %s"
    temp = (str(getRecordEntry.get()), str(getRecordEntry.get()), str(getRecordEntry.get()), str(getRecordEntry.get()), str(getRecordEntry.get()), )      
    art_gallery_cursor.execute(sql, temp)  
    customerArtPreferences += art_gallery_cursor.fetchall()

    # Check the Customer table for user input and save data if they match
    sql = "SELECT * FROM Customer WHERE Customer_Number = %s OR Phone = %s OR Art_Preference = %s"
    temp = (str(getRecordEntry.get()), str(getRecordEntry.get()), str(getRecordEntry.get()), )      
    art_gallery_cursor.execute(sql, temp)  
    customerArtPreferences += art_gallery_cursor.fetchall()

    # Print all of the tables that matched the user's input
    for x in customerArtPreferences:
        print(x)



# Sort a report based on Art Style
def sortReportArtStyle():

    # Clear the terminal
    clear()

    # Save the query statement into a python variable and execute with proper syntax
    sql = "SELECT * FROM Artist WHERE Style_of_Art = %s"
    temp = (str(sortReportArtStyleEntry.get()), )   
    art_gallery_cursor.execute(sql, temp)  
    customerArtPreferences = art_gallery_cursor.fetchall()
    
    # Print all artists who use this style
    print("These are all the artists who use this art style: ")
    for x in customerArtPreferences:
        print(x)

    

# Print a report showing customers whose art preference is the same as shown in any given art show.
def customerArtPreference():

    # Clear the terminal
    clear()

    # Save the query statement into a pythin variable and execute with proper syntax
    sql = "SELECT Customer_Number, Phone FROM Customer WHERE Art_Preference = %s"
    temp = (str(customerArtPreferenceEntry.get()), )   
    art_gallery_cursor.execute(sql, temp)  
    customerArtPreferences = art_gallery_cursor.fetchall() 
    
    # Prints the customers' numbers and phones
    print("Customers who like this art style: ")
    for x in customerArtPreferences:
        print(x)

#==========================================================================================#
#=====  Database Functions  =====  Database Functions  =====  Database Functions  =========#
#==========================================================================================#




#==========================================================================================#
#====  Main Code  ====  Main Code  ====  Main Code  ====  Main Code ====  Main Code =======#
#==========================================================================================#

# Create the UI window
root = tk.Tk()
root.title("Art Gallery")


# Initial welcome message
welcomeLabel = tk.Label(text="\Welcome to Art Gallery DB. ", anchor="w")

# Print Command 
printLabel  = tk.Label(text="Click here to print the Art Gallery's DB: ", anchor="w")
printButton = tk.Button(root, text="Print", command=printDB)

# Return a Query based on user's input
getRecordLabel = tk.Label(text="Enter a key to query its results. ", anchor="w")
getRecordEntry = tk.Entry(root, width=27)
getRecordSave  = tk.Button(root, text="Search", command=getRecord) 

# sortReportArtStyle:
sortReportArtStyleLabel = tk.Label(text="Enter an art style to return all artists who use that style. ", anchor="w")
sortReportArtStyleEntry = tk.Entry(root, width=27)
sortReportArtStyleSave  = tk.Button(root, text="Search", command=sortReportArtStyle) 

# customerArtPreference:
customerArtPreferenceLabel = tk.Label(text="Enter an Art Show to show who may be interested in it. ", anchor="w")
customerArtPreferenceEntry = tk.Entry(root, width=27)
customerArtPreferenceSave  = tk.Button(root, text="Search", command=customerArtPreference) 


# Put all objects in a grid for tidiness
printLabel.grid(row=0, column=0)
printButton.grid(row=0, column=1)

getRecordLabel.grid(row=1, column=0)
getRecordEntry.grid(row=1, column=1)
getRecordSave.grid(row=1, column=2)

sortReportArtStyleLabel.grid(row=2, column=0)
sortReportArtStyleEntry.grid(row=2, column=1)
sortReportArtStyleSave.grid(row=2, column=2)

customerArtPreferenceLabel.grid(row=3, column=0) 
customerArtPreferenceEntry.grid(row=3, column=1) 
customerArtPreferenceSave.grid(row=3, column=2) 



# Run the Loop
root.mainloop()

# Clear the terminal
clear()

#==========================================================================================#
#====  Main Code  ====  Main Code  ====  Main Code  ====  Main Code ====  Main Code =======#
#==========================================================================================#