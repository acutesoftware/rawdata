#!/usr/bin/python3
# -*- coding: utf-8 -*-
# errors.py

import os
import random
import logging

data_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'data' ) 
 
logging.basicConfig(filename='errors.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
 
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
        else:
            self.glitch = DataError('BAD_DATA')
    
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
            logging.info('Adding error to col' +  str(col) + ' row ' + str(row))
            self.tbl[row][col] = self.glitch.random_error(self.tbl[row][col])
            
    def swap_columns(self, c1, c2):  
        """
        switch columns around in a table to simulate import errors
        with incorrect column headers
        """
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
        """
        choose one of the random error types already coded
        """
        i = random.randint(1,3)
        if i == 1:
            return self._fixed_val()
        elif i == 2:
            return self._blank_out()
        elif i == 3:
            return self._add_spaces(orig)
    
    def _fixed_val(self):
        """
        return the fixed string specified at class instantiation
        """
        return self.fudge_string
        
    def _blank_out(self):
        """
        blank out the data - useful for checking NULL values or
        breaks in transmission
        """
        return ''
        
    def _add_spaces(self, orig):
        """
        add spaces to start and end of columns
        """
        if type(orig) is str:
            return ' ' + orig + '     '
        else:
            return ' ' + str(orig) + '     ' 
            
