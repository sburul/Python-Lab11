# Seyfullah Burul 
# Last Update : December 2, 2020
# Reading data from SQL file and opening a web browser with related data from SQL

# Import necessary libraries
import sqlite3
import base64
import webbrowser
import os

# Function that creates connection to the database
def createConnection(dbFileName):    
    # Define connection object
    conn = None
    try:
        # Check existing of db file 
        isExist = os.path.exists(dbFileName)        
        if(isExist):
            # Create connection object for sqlite3
            conn = sqlite3.connect(dbFileName)
        else:
            raise Exception('Database file not found')     
    except Exception as ex:
        # Error message
        print(ex)
    # Return defined connection object
    return conn

# Function that updates particular data in the database
def updateRow(conn, sql):
    # Define a cursor for connection
    cur = conn.cursor()
    # Execute a sql statement
    cur.execute(sql)
    # Commit changes
    conn.commit()

# Function that select row from the table
def selectRow(conn, sql):
    # Define a cursor for connection
    cursor = conn.cursor()
    # Execute a sql statement
    cursor.execute(sql)
    # Return data
    return cursor.fetchone()

# Main function
def  main():
    try:
        # Create connection object for sqlite3
        with createConnection('week11.db') as conn:
                # Loop for user input
                while True:
                    # Getting number from the user                    
                    userInput = input('Please a number between 1 and 24 to open browser(to quit enter q):')
                    # Check input to quit
                    if(userInput == 'q' or userInput == 'Q'):
                        break
                    # Check input if it an integer
                    elif userInput.isdigit():
                        # Convert input string to integer
                        recordId = int(userInput)
                        # Check if the number is in the expected range
                        if(recordId > 0 and recordId < 25):
                            # Sql query
                            sql =  f"SELECT * FROM Lab10 WHERE id={recordId}"
                            # Get data from db
                            data = selectRow(conn, sql)                    
                            # Get the value
                            encodedLink = data[1]  
                            # Decode base64 data to string
                            stringLink = base64.b64decode(encodedLink).decode('utf-8')
                            # Open link via web browser
                            webbrowser.open(stringLink)
                            # Get city name from the user
                            cityName = input(f"Please enter a city name [Current:{data[2]}]:")
                            # Get country name from the user
                            countryName = input(f"Please enter a country name [Current:{data[3]}]:")
                            # Sql query for update table
                            sql = f"UPDATE Lab10 SET City='{cityName}', Country='{countryName}' WHERE id={recordId}"
                            # Update table
                            updateRow(conn, sql)
                            # Give info
                            print("Your record is updated!")
                        else:
                            # Error message
                            print("The number you entered is not between 1 and 24")
                    else:
                        # Error message
                        print("It is not an expected value!")                    
    except Exception as ex:
        # Error message
        print(ex)

# Call main function
if __name__ == '__main__':
    main()
    

