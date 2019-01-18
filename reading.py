# Functions for reading tables and databases

import glob
from database import *


# YOU DON'T NEED TO KEEP THE FOLLOWING CODE IN YOUR OWN SUBMISSION
# IT IS JUST HERE TO DEMONSTRATE HOW THE glob CLASS WORKS. IN FACT
# YOU SHOULD DELETE THE PRINT STATEMENT BEFORE SUBMITTING

#file_list = glob.glob('*.py')
#print(file_list)

# Write the read_table and read_database functions below

def read_table(file_name):
    '''
    (str) -> Table
    This function takes the name of a file and 
    creates a dictionary with the first row having the key names.
    This goes into a Table class and returns in
    REQ: file_name: file must exist so it can be opened
    '''
    table = Table()
    
    
    # open the file
    file = open(file_name, 'r')
    
    file_lines = file.readlines()
    
    # close the file
    file.close()
    
    
    #remove any blank lines that occur in file
    for x in range(0, len(file_lines), 1):
        # removes blank lines
        file_lines[x] = file_lines[x].replace("\n", "")
        #removes empty lines in list
        if file_lines[x] == "":
            file_lines.pop(x)
            
    table.table = table.create_dict(file_lines)
    
    
   
    return table
    
def read_database():
    '''
    () -> Database
    This function finds all files in the same directory
    and reads them. Then return a Database object holding data
    of all .csv files
    REQ: None
    '''
    file_list = glob.glob("*.csv")
    database = Database()
    
    # create loop to find the set each each file name to a table
    for x in range(0, len(file_list) , 1):
        
        database.database[file_list[x]] = read_table(file_list[x])
    
    return database

