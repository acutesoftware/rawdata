# create.py

import random

class Table(object):
    """
    holds a table and manages the cleaning and 
    creation of DQ issues
    """
    def __init__(self, tbl, fudge_str):
        self.tbl = tbl
        self.glitch = DataError(fudge_str)
        
    def add_errors(self, num=3):
        """
        Adds 'num' errors to the table
        """
        for i in range(1, num+1):
            col = random.randint(0,len(self.tbl))
            print('col = ', col)
            self.tbl[col][i] = self.glitch.random_error(self.tbl[col][i])
            
    def swap_columns(self, c1, c2):  
        #self.tbl[c1][:], self.tbl[c2][:] = self.tbl[c2][:], self.tbl[c1][:] 
        for rownum, r in enumerate(self.tbl):
            #print('rownum = ', rownum, 'c2 = ', c2, 'c1 = ', c1)
            #print('self.tbl[rownum][c1] = ', self.tbl[rownum][c1])
            #print('self.tbl[rownum][c2] = ', self.tbl[rownum][c2])
            self.tbl[rownum][c1], self.tbl[rownum][c2] = self.tbl[rownum][c2], self.tbl[rownum][c1]

class DataError(object):
    def __init__(self, fudge_string):
        self.fudge_string = fudge_string
    
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
        return ' ' + orig + '     '
            