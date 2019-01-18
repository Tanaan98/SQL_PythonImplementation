class Table():
    '''A class to represent a SQuEaL table'''
    
    def __init__(self, dictionary = None):
        self.table = {}
        if dictionary != None:
            self.table = dictionary
        self.rows = 0
        
    def get_rows(self):
        '''
        (Table) -> None
        This method gets the number of rows
        '''
        
        keys_list = list(self.table.keys())

        
        # since all keys hold the same amount of rows
        self.rows = len(self.table[keys_list[0]])
        
        
    def create_dict(self, file_lines):
        '''
        (Table, list[string])- Dictionary
        This method organizes the file_lines(which came
        from a file), and returns the dictionary
        REQ:None
        '''
        
        # create keys, since the first row will have the keys
        keys = file_lines[0].split(',')
    
        # make keys hold empty lists
        for x in range(0, len(keys), 1):
            # keys are holding empty lists
            self.table[keys[x]] = []
    
        # remove the keys from the list   
        file_lines = file_lines[1:]
        
        # keep track of the number of lines for num_rows method
        self.rows = len(file_lines)
        
        # make the list hold small lists instead of a long string
        for x in range (0, len(file_lines), 1):
            list_of_elements = file_lines[x].split(',')
    
    
            # add element to the list that is held by the key
            for y in range(0, len(keys), 1):
                self.table[keys[y]] = self.table[keys[y]] + [list_of_elements[y]]
    
        self.set_dict(self.table) 

        return self.table
        

    def set_dict(self, new_dict):
        '''(Table, dict of {str: list of str}) -> NoneType

        Populate this table with the data in new_dict.
        The input dictionary must be of the form:
            column_name: list_of_values
        '''
        self.new_dict = new_dict

    def get_dict(self):
        '''(Table) -> dict of {str: list of str}

        Return the dictionary representation of this table. The dictionary keys
        will be the column names, and the list will contain the values
        for that column.
        '''
        try:
            return self.new_dict
        
        except:
            self.set_dict(self.table)
            return self.new_dict
        
    
    def num_rows(self):
        '''
        (Table)-> int
        Return the number of rows in the Table
        '''
        if self.rows == 0:
            self.get_rows()
        
        return self.rows

    def print_csv(self):
        '''(Table) -> NoneType
        Print a representation of table in csv format.
        '''
        # no need to edit this one, but you may find it useful (you're welcome)
        dict_rep = self.get_dict()
        columns = list(dict_rep.keys())
        print(','.join(columns))
        rows = self.num_rows()
        for i in range(rows):
            cur_column = []
            for column in columns:
                cur_column.append(dict_rep[column][i])
            print(','.join(cur_column))


class Database():
    '''A class to represent a SQuEaL database'''
    
    def __init__(self, dictionary=None):
        self.database = {}
        if dictionary != None:
            self.database = dictionary

    def set_dict(self, new_dict):
        '''(Database, dict of {str: Table}) -> NoneType

        Populate this database with the data in new_dict.
        new_dict must have the format:
            table_name: table
        '''
        self.new_dict = new_dict

    def get_dict(self):
        '''(Database) -> dict of {str: Table}

        Return the dictionary representation of this database.
        The database keys will be the name of the table, and the value
        with be the table itself.
        '''
        return self.new_dict
