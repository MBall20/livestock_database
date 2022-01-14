'''
Author: Mitchell Ball
Date: 1/13/22
Project: Relational Database
'''

#import needed libraries
import sqlite3

# Connect to database, creates new if not already present
connection = sqlite3.connect('cattle_database.db')
cursor = connection.cursor()

# Create base table to work with if it does not already exist
cursor.execute("CREATE TABLE IF NOT EXISTS herd (ear_tag INT, birth_date DATE, gender CHAR, polled CHAR, location TEXT)")

# Display menu options
choice = None
while choice != 6:
    # Choice 1 is displayed so I can make minor changes when it comes time to implement it.

    print('1) Select Herd (Inoperable right now)')
    print('2) Display Livestock')
    print('3) Add Livestock')
    print('4) Update Livestock')
    print('5) Delete Livestock')
    print('6) Quit')
    choice = input('> ')
    
    '''
    if choice == '1':
        # Select desired herd
        pass
    '''

    if choice == '2':
        # Display contents of herd
        cursor.execute('SELECT * FROM herd ORDER BY ear_tag ASC')
        pass

    elif choice == '3':
        # Add animal to herd
        pass

    elif choice == '4':
        # Update animal (location)
        pass

    elif choice == '5':
        # Delete an animal
        pass

        



    
'''    
First table columns:
ID, ear tag, birth date,  gender, breed, polled, location
create a link to an additional table with vaccine list
create a link to additional table with medications
decide how to record pedegree

'''


