# errors.py

import os
import random
import rawdata.generate
data_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'data' ) 

def TEST():
    """
    local testing - will be moved to test_create.py
    """
    colLabel = ['DATE', 'name',   'Born']
    colTypes = ['DATE', 'PEOPLE', 'PLACE']
    tbl = rawdata.generate.TableGenerator(3, colTypes, colLabel)
    #generate.show_table(tbl)
    t = TableWithErrors(tbl, 'VVV')
    print(t.tbl)
    t.load_from_file(data_fldr + os.sep + 'countries.csv')

    #generate.show_table(t.tbl)
    print('header = ', t.header)
    
    # add errors to the country file
    t.add_errors(50)
    print(t)
    
    
class TableWithErrors(object):
    """
    holds a table and manages the cleaning and 
    creation of DQ issues
    """
    def __init__(self, tbl, fudge_str):
        self.tbl = tbl.tbl
        if tbl:
            self.header = tbl.tbl[0]
        if fudge_str:
            self.glitch = DataError(fudge_str)
    
    def __str__(self):
        txt = '\n'.join(','.join([col if type(col) is str else str(col) for col in row]) for row in self.tbl)
        return txt
    
    def load_from_file(self, fname, delim=',', quote='"'):
        """
        recreates the internal table tbl from an external file
        Use this for sample data generation based on existing 
        data or for extracting unique lists (ie categories from
        your sales data)
        """
        self.tbl = []
        with open (fname, 'r') as f:
            row = f.readline()
            self.header = [r.strip('\n').strip(quote) for r in row.split(delim)]
            for num, row in enumerate(f):
                if row:
                    if num == 0:
                        self.header = row
                    self.tbl.append([r.strip('\n').strip(quote) for r in row.split(delim)])
        
    
    def add_errors(self, num=3):
        """
        Adds 'num' errors to the table
        """
        for _ in range(0, num):
            col = random.randint(0,len(self.tbl[0])-1)
            row = random.randint(1,len(self.tbl)-1)  # don't mess with header here
            print('Adding error to col', col, ' row ', row)
            self.tbl[row][col] = self.glitch.random_error(self.tbl[row][col])
            
    def swap_columns(self, c1, c2):  
        #self.tbl[c1][:], self.tbl[c2][:] = self.tbl[c2][:], self.tbl[c1][:] 
        for r, _ in enumerate(self.tbl):
            self.tbl[r][c1], self.tbl[r][c2] = self.tbl[r][c2], self.tbl[r][c1]


class DataError(object):
    """
    Class to introduce random errors to data
    """
    def __init__(self, fudge_string):
        if fudge_string == '':
            fudge_string = 'BAD_DATA'
        self.fudge_string = fudge_string
        
    def __str__(self):
        return self.fudge_string
    
    def random_error(self, orig):
        i = random.randint(1,3)
        if i == 1:
            return self._fixed_val()
        elif i == 2:
            return self._blank_out()
        elif i == 3:
            return self._add_spaces(orig)
    
    def _fixed_val(self):
        return self.fudge_string
        
    def _blank_out(self):
        return ''
        
    def _add_spaces(self, orig):
        if type(orig) is str:
            return ' ' + orig + '     '
        else:
            return ' ' + str(orig) + '     ' 
            
    
if __name__ == '__main__':
    TEST()
