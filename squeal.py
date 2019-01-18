from reading import *
from database import *

# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results

# Note: This function is incomplete and is not used.
# All cases where the constraint has a '>' will not work
'''
def apply_constraints_for_greater(table, constraints):
    
    (Table, list[string])-> Table
    Return a table that has deleted certain rows based off > constraints
    REQ: Table must be hold some sort of dictionary
    
    
    spliter = []
    column1 = []
    column2/number = []
    
    for x in constraints:
        if '>' in x:
            # break the constrait based off >
            spliter = x.split('>')
            # since column1 is always first
            column1 = spliter[0]
            #since column2 is always second
            column2/number = spliter[1]
            
            # this assumes that the user is comparing to a number
            if "'" in columns2/number:
                column2/number.strip("'")
                #then convert the number (that is in a string) to a float
                column2/number = float(column2/number)
            
            
        '''
            
        


def selecting_columns(table, columns):
    '''
    (Table, list[string]) -> Table
    Return table based on the what the columns hold
    REQ: Table must be holding a dictionary
    REQ: columns only have elements/string names that exist in table.
    '''
    table_with_specifc_columns = Table()
    # the case where * was used
    if columns[0] == '*':
        table_with_specifc_columns = table
        
    # case where specific columns were used    
    else:
        for x in columns:
            if x in table.table.keys():
                table_with_specifc_columns.table[x] = table.table[x]
            
    return table_with_specifc_columns
    

def apply_constraints_for_equal(table, constraints):
    '''
    (Table, list[string])-> Table
    Return a table that has deleted certain rows based off constraints
    REQ: Table must be hold some sort of dictionary
    
    '''
    index = 0
    #create a loop that finds all columns that 
    # need to be removed
    for x in range(0, len(constraints), 1):
        # find position of '='
        for y in range(0, len(constraints[x]), 1):
            if constraints[x][y] == '=':
                index = y
                
        # get the name of all columns that need to be removed
        constraints[x] = constraints[x][index+1:] 
    
    # now remove all the columns that we dont need 
    for z in range(len(table.table)):
        
        for a in constraints:
            if a in table.table:
                table.table.pop(a, None)
    return table
        
                        
        

def find_table_in_database(database, table_names, table_index):
    '''
    (Database, list[string], int)-> Table
    Get the table that matched the name
    REQ: table_index is a non-negative number
    REQ: Database must be holding a table
    REQ: table_names must have correct names
    '''
    found_table = database.database[table_names[table_index]]
    return found_table


def merge_dictionary(Dict1, Dict2):
    '''
    (dict, dict) -> dict
    This function gets two dictionarys and combines them and then returns it
    REQ: both Dict1 and Dict2 should not be empty (but still works being empty)
    '''
    combined_dict = Dict1.copy()
    combined_dict.update(Dict2)
    
    return combined_dict


def multiply_table_rows(Table, number):
    '''
    (Table, int)-> dictionary
    Multiply the list that the key holds based off the number of rows of the first Table
    REQ: number must be greater than 0
    REQ: Table object must have a dictionary within it
    '''
    
    for keys in Table.table:
        # 
        Table.table[keys] = Table.table[keys] * (number)
    return Table.table


def find_column(tokens):
    '''
    (list[string])-> list[string]
    This function returns a list of all the columns that is needed
    REQ: tokens must contain an element 'select' and the columns must come after it
    '''
    # create/ initialize empty list to store columns
    columns = []
    # first check if 'select' exists in the query
    # and also get the string of the constraits
    for x in range(0, len(tokens), 1):
        if tokens[x] == "select":
            # since the columns must be after the 
            columns = tokens[x+1].split(',')
        
    # return the columns
    return columns   

def find_constraints(tokens):
    '''
    (list[string]) -> list[string]
    This function finds all the constraints that are in
    in query and returns it. For example, m.movie = r.move
    REQ: if the word 'where' exists, the constraints must come after
    '''
    
    # create/ initialize empty list to store constraints
    constraints = []
    # first check if 'where' exists in the query
    # and also get the string of the constraits
    for x in range(0, len(tokens), 1):
        if tokens[x] == "where":
            # since the constraints must be after the 
            constraints = tokens[x+1].split(',')
    
    # return the constraints
    return constraints
        
def find_tables(tokens):
    '''
    (list[string]) - list[string]
    This function finds all the names of the tables that we need to 
    use 
    REQ: tokens must have the element 'from' and have the names after it
    
    '''
    
    # create/ initialize empty list to store tables
    tables = []
    # first check if 'from' exists in the query
    # and also get the string of the tables
    for x in range(0, len(tokens), 1):
        if tokens[x] == "from":
            # since the tables must be after
            tables = tokens[x+1].split(',')
            
    # in case there is no '.csv' in the name
    for x in range(0, len(tables), 1):
        if ".cvs" not in tables[x]:
            tables[x] = tables[x] + ".csv"
            
    # return the table names
    return tables    

def run_query(database, query):
    '''
    Return a table that is obtained from Database and only returns
    specific parts specified by the query
    
    REQ: query in correct format
    REQ: database is a dictionary
    '''
    # breaks query into a list
    tokens = query.split()

    
    # find the columns that we need from the query (does not include *)
    columns = find_column(tokens)
    
    # find the tables that we need to get/use
    table_names = find_tables(tokens)
    
    
    # find constraints in query (if they exist)
    constraints = find_constraints(tokens)
    
    # Create table since table gets returned
    table = Table()
    
    # get the table we need from the database
    # get one/first table and create case if 2 or more tables
    # exist
    table = find_table_in_database(database, table_names, 0)
    
    # now cover the case where there is more than 1 file
    if len(table_names) > 1:
        
        # we need to create a for loop since we do not know how many
        # files that the query has
        # starts at 1 since we already did one table
        for x in range(1, len(table_names), 1):
            next_table = find_table_in_database(database, table_names, x)
            # now we need to use the cartesian product to combine everything into one table
            table = cartesian_product(table, next_table)
            
    # now call a function that  removes all the unnessary
    # columns that were mention after the 'where' in the query
    table = apply_constraints_for_equal(table, constraints)
    
    # call a function that gets all the 
    table = selecting_columns(table, columns)
    
    return table
    

    


def cartesian_product(Table1, Table2):
    '''
    (Table, Table) -> Table
    Return a table that is the result of Table1 and Table2 
    being multipied together (This means that each row in Table1
    will be multiplied by the number of rows in Table2 and vice versa)
    
    REQ: Table1 and Table2 must be holding some sort of non-empty dictionary
    REQ: keys in Table1 and Table2 must be holding a list (all lists being the same length)
    REQ: Both Table1 and Table2 must have unique keys
    
    '''
    # create a Table since a table is being returned
    table = Table()
    
    # get number of rows from each table (since we need to multiply them, I think)
    Table1_rows = Table1.num_rows()
    Table2_rows = Table2.num_rows()
    
    # lets create a vaiable to hold our dictionary instead of 
    # our table.table since it could get confusing. In the end, let
    # table.table = our variable
    new_dictionary1 = {}
    
    # this uses/gets each key
    for x in Table1.table:
        #assign each key an empty list
        new_dictionary1[x] = []
        
        # the Table.table[x] loop will loop based on the number of rows
        for y in Table1.table[x]:
            # this loops based on Table2_rows
            for z in range(0, Table2_rows, 1):
                
                # adds onto the originally empty list
                new_dictionary1[x].append(y)
        

     
    # at this point we only have the table 1.
    # Now we need to do table 2
    # at this point, its better to create a new function that finds
    # table2
    new_dictionary2 = multiply_table_rows(Table2, Table1_rows)
    
    
    # combine tables
    combined_dictionary = merge_dictionary(new_dictionary1, new_dictionary2)
    
    # Now make our Table Class variable (table)
    # hold the combined dictionary and return it
    
    table.table = combined_dictionary
    
    return table
                


if(__name__ == "__main__"):
    # get query
    query = input("Enter a SQuEaL query, or a blank line to exit:")
    # repeat until nothing is entered
    while (query != ''):
        x = run_query(read_database(), query)
        x.print_csv()
        query = input("Enter a SQuEaL query, or a blank line to exit:")
