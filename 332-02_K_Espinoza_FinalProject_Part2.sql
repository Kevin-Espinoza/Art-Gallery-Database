 /****************************************************************************************************************************
//  Program name: "332-02 Final Project" 
//  The purpose of this program is to create an Art Gallery Database using the ER Diagram we created.
//  There will be a total of 4 tables with 4 tuples each. The 4 tables will be outputted at the end. Part 3 will 
//  Implement this program with a high level language. Copyright (C) 2020 Kevin Espinoza
//                                                                           
//  This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License  
//  version 3 as published by the Free Software Foundation.                                                                    
//  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied         
//  warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.     
//  A copy of the GNU General Public License v3 is available here:  <https://www.gnu.org/licenses/>.                            
//****************************************************************************************************************************

//*****************************************************************************************************************************
//  Author information
//  Author name: Kevin Espinoza
//  Author email: k.espinoza1012@csu.fullerton.edu
//  332-02 Final Project Part2
//  Due Date: 2020-Dec-02
//
//  Purpose:
//  The purpose of this file is to create an Art Gallery Database that follows an ER Diagram created in Part 1. 
//****************************************************************************************************************************

//*****************************************************************************************************************************
// NOTE:
// All tuples will have one PRIMARY KEY, of which is a UNIQUE value
// Each created table will be in its own respective block
// All created tuples will be under the CREATE TABLE block for its respective table
//****************************************************************************************************************************/




-- Delete old Database if it already exists, this helps prevent errors
DROP DATABASE IF EXISTS Art_Gallery;
CREATE DATABASE Art_Gallery;
-- Make sure we are using the proper Database, in this case Art_Gallery
USE Art_Gallery;       



/*************************************************************************************/

-- Create a table named Artist: Unique Name + No NULL Values --
CREATE TABLE Artist (
    Name varchar(225) PRIMARY KEY, 
    Phone varchar(225) NOT NULL, 
    Address varchar(225) NOT NULL, 
    Birth_Place varchar(225) NOT NULL, 
    Age int NOT NULL, 
    Style_of_Art varchar(225) NOT NULL
);

-- Artist Tuples --
INSERT INTO Artist VALUES("Frida Kahlo", "+52 1551 234 5678", "Londres 247, Del Carmen, Coyoacán", "Coyoacán, Mexico City, Mexico", 47 , "Folk Art");
INSERT INTO Artist VALUES("Andy Warhol", "+1 412 555 5555", "321 E. 6th St.", "Pittsburgh, PA, USA", 59 , "Fine Art");
INSERT INTO Artist VALUES("Vincent van Gogh", "+31 970 1028 1265", "Rue du Pavillon, 37033 Cuesmes", "Zundert, Netherlands", 37 , "Impressionism");
INSERT INTO Artist VALUES("Augusta Savage", "+1 212 555 5555", "Saugerties, NY 12477", "Green Cove Springs, FL", 70 , "Sculpting");

/*************************************************************************************/




/*************************************************************************************/

-- Create a table named Art Work: Unique Title + 1 NULL Value --
CREATE TABLE Art_Work (
    Title varchar(225) PRIMARY KEY,
    Artist varchar(225) NOT NULL, 
    Type_of_Art varchar(225) NOT NULL, 
    Date_of_Creation int, 
    Date_Aquired int NOT NULL, 
    Price double NOT NULL, 
    Location varchar(225) NOT NULL,
    FOREIGN KEY (Artist) REFERENCES Artist(Name)
);

-- Art_Work Tuples --
INSERT INTO Art_Work VALUES("A Few Small Nips (Passionately in Love)", "Frida Kahlo", "Genre Painting", 1935, 1940, 15000000 , "Museo Dolores Olmedo");
INSERT INTO Art_Work VALUES("The Marilyn Diptych", "Andy Warhol", "Pop Art", 1962, 2000, 17300000, "Tate");
INSERT INTO Art_Work VALUES("The Starry Night", "Vincent van Gogh", "Post-Impressionism", 1889, 1929, 100000000, "The Museum of Modern Art");
INSERT INTO Art_Work VALUES("Gamin", "Augusta Savage", "Bust Sculpture", 1930, 1939, 30000, "Smithsonian American Art Museum");

/*************************************************************************************/




/*************************************************************************************/

-- Create a table named Art Shows: Unique Date/Time + No NULL Values --
CREATE TABLE Art_Shows (
    Date_and_Time varchar(225) PRIMARY KEY, 
    Artist varchar(225) NOT NULL,
    Contact varchar(225) NOT NULL, 
    Contact_Phone varchar(225) NOT NULL, 
    Location varchar(225) NOT NULL, 
    FOREIGN KEY (Artist) REFERENCES Artist(Name)
);

-- Art_Shows Tuples --
INSERT INTO Art_Shows VALUES("7-4-2020 -- 13:00", "Frida Kahlo", "Museo Dolores Olmedo", "+52 55 5555 0891", "Mexico City, Mexico");
INSERT INTO Art_Shows VALUES("7-31-2020 -- 12:00", "Andy Warhol", "Tate", "+44 020 7887 8888", "Liverpool");
INSERT INTO Art_Shows VALUES("8-30-2020 -- 10:00", "Vincent van Gogh", "The Museum of Modern Art", "+1 888 999 8861", "New York, NY");
INSERT INTO Art_Shows VALUES("12-21-2020 -- 14:00", "Augusta Savage", "Smithsonian American Art Museum", "+1 202 633 7970", "Washington, D.C.");

/*************************************************************************************/




/*************************************************************************************/

-- Create a table named Customer: Unique Number + No NULL Values --
CREATE TABLE Customer (
    Customer_Number int PRIMARY KEY, 
    Phone varchar(225) NOT NULL, 
    Art_Preference varchar(225) NOT NULL
);

-- Customer Tuples --
INSERT INTO Customer VALUES( 889174181, "+1 323 507 6472", "Modern Art");
INSERT INTO Customer VALUES( 123345454, "+1 213 543 3453", "Pop Art");
INSERT INTO Customer VALUES( 234234322, "+1 234 432 6546", "Fine Art");
INSERT INTO Customer VALUES( 234235435, "+1 453 534 3453", "Fine Art");

/*************************************************************************************/




/*************************************************************************************/

-- Print all Tables in the Database --
SELECT * FROM Artist;
SELECT * FROM Art_Work;
SELECT * FROM Art_Shows;
SELECT * FROM Customer;

/*************************************************************************************/