#!/usr/bin/python3
# -*- coding: utf-8 -*-
# content.py

import os
import random
import fnmatch

data_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'data' ) 
print('data_fldr = ', data_fldr)
sample_xtn = '*.sample'

class DataFiles(object):
    """
    read data files from data subfolder to get lists
        columns = [folder, filename, short_name, column_name, dot_form]
            games.skills.area
            games.skills.description
            food.food_desc.NDB_No
            food.food_desc.Refuse
            food.food_desc.SciName
            food.food_desc.N_Factor
            food.garden_produce.method
            food.garden_produce.type
            food.garden_produce.name
            finance.mining_copper_rent.Country Code
            finance.mining_copper_rent.Country Name
            finance.mining_copper_rent.1978
            finance.mining_copper_rent.1979
            world.country.2-alpha code
            world.country.WB-2 code
            world.country.Table Name
            world.country.Short Name        
    """
    def __init__(self):
        self.filelist = []
        self.columns = []
        self.lookup = []
        for root, _, files in os.walk(data_fldr):
            for f in files:
                self.filelist.append([root + os.sep + f, root,f])
                cols = self.get_all_columns(root + os.sep + f)
                for c in cols:
                    if c != '':
                        dot_form = root[len(data_fldr) + 1:] + '.' + f[:-4] + '.' + c
                        self.columns.append([root,f, f[:-4], c, dot_form])
                        self.lookup.append(dot_form)
                   
                
    def __str__(self):
        txt = 'Data files read from :\n'
        txt += data_fldr + '\n'
        for row in self.filelist:
            txt += row[0] + '\n'
        return txt    
    
    def get_list(self, names_only=False):
        if names_only:
            res = []
            for row in self.filelist:
                res.append(row[2][:-4])
            return res
        else:
            return self.filelist
            
    def get_list_fullname(self):
        lst = []
        for row in self.filelist:
            lst.append(row[0])
        return lst
            
    def get_sample(self, filename, col_name):
        set = self.get_collist_by_name(filename, col_name)
        return random.choice(list(set[0]))
    
    def get_collist_by_name(self, filename, col_name):
        with open(filename) as f:
            ndx = 0
            res = []
            for num, line in enumerate(f):
                cols = line.split(',')
                if num == 0:
                    for col_num, col in enumerate(cols):
                        if col.strip('"') == col_name:
                            ndx = col_num
    
                res.append(cols[ndx].strip('"'))
        return [set(res)]            

    def get_all_columns(self, filename):
        line = ''
        res = []
        if os.path.exists(filename) is False:
            return None
        try:
            with open(filename, 'r') as f:
                line = f.readline()
                cols = line.split(',')
                for col in cols:
                    res.append(col.strip('"').strip('\n'))
        except Exception as ex:
            print('DataFiles.get_all_columns: cant read filename ' + str(ex))
        return res       

        
class Samples(object):
    """
    class to manage the list of sample files in /samples folder
    """
    def __init__(self, root_path):
        self.sample_list = []      # filelist = [shortname, fullpath]
        self.samples = []          # list of Sample objects
        self.root_path = root_path # os.getcwd() + os.sep + 'samples'
        for root, _, files in os.walk(self.root_path):
            for basename in files:
                if fnmatch.fnmatch(basename, sample_xtn):
                    filename = os.path.join(root, basename)
                    self.sample_list.append([basename, filename])
                    self.samples.append(Sample(filename))
                
                
    def __str__(self):
        txt = 'List of available sample definitions\n'
        for d in self.sample_list:
            txt += d[0] 
        return txt    
    
    def get_sample_by_name(self, txt):
        """
        returns the first Sample that matches txt
        """
        for s in self.samples:
            if txt + '.sample' in s.fullname:
                return s
        return None
    
    def list(self):
        """
        List all samples available
        """
        res = ''
        for d in self.sample_list:
            #print(d)
            res += d[0] + '\n'
        return res

class Sample(object):
    """
    class to manage a single sample, read from 
    a .sample file - just does parsing really
    """
    def __init__(self, fullname):
        """
        reads the .sample file passed and loads 
        to class.
        """
        self.fullname = fullname
        self.cols = []
        self.lists = []
        self.col_types = []     # list for generate function
        self.col_labels = []    # list for generate function
        
        with open(fullname, 'r') as f:
            for line in f:
                self._parse_line(line)

    def __str__(self):
        res = 'Sample File = ' + self.fullname + '\n'
        for num, c in enumerate(self.cols):
            res += 'Column#' + str(num) + ' = ' + c + '\n'
        for num, l in enumerate(self.lists):
            res += 'List#' + str(num) + ' = ' + l + '\n'
        
        res += '\nDETAILS for generate\n'
        res += ' colLabels = [' + ','.join([c for c in self.col_labels]) + ']\n'
        res += ' colTypes  = [' + ','.join([c for c in self.col_types]) + ']\n'
        return res
      
    
    def _parse_line(self, line):
        """
        takes a line from a sample file and parses into 
        class objects.
        """
        if line[0] != '#':
            parsed = line.split(':')
            if parsed[0] == 'LIST':
                self.lists.append(parsed[1].strip('\n'))
            elif parsed[0] == 'COLUMN':
                self.cols.append(parsed[1].strip('\n'))
                details = parsed[1].strip('\n').split(',')
                self.col_labels.append(details[0].strip(' '))
                self.col_types.append(details[1].strip(' '))
