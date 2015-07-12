#!/usr/bin/python3
# content.py

import os
import random
import fnmatch

data_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'data' ) 

rootPath = os.getcwd() + os.sep + 'samples'
sample_xtn = '*.sample'


def TEST():
    s = Samples()
    print(s.get_list())
    col1 = s.get_collist_by_name(data_fldr + os.sep + 'games' + os.sep + 'skills.csv', 'type' )
    print(col1)
    
    # get list of countries from copper production
    fname = data_fldr + os.sep + 'finance' + os.sep + 'mining_copper_rent.csv'
    country_names_copper = s.get_collist_by_name(fname, 'Country Name')  # country code, Country Name
    print(country_names_copper)
    # [{'CHILE', 'AUSTRALIA', 'UNITED KINGDOM', 'Cuba', 'SOUTH AFRICA', 'INDONESIA', 
    #   'GUATEMALA', 'PHILIPPINES', 'NORWAY', 'ZIMBABWE', 'AUSTRIA', 'CYPRUS', 'CHINA', ...

    # get food lists
    food = s.get_collist_by_name(data_fldr + os.sep + 'food' + os.sep + 'food_desc.csv', 'Long_Desc')
    for f in food[0]:
        print(f)
    
    
    f = s.get_sample_by_name('finance_transaction')
    print(f)
    print(s)
    
class Samples(object):
    """
    read samples from data subfolder to get lists
    """
    def __init__(self):
        self.filelist = []
        self.sample_list = []
        self.samples = []
        # data files
        for root, _, files in os.walk(data_fldr):
            for f in files:
                self.filelist.append([root + os.sep + f, root,f])

        # samples from samples folder        
        self.sample_list = []  # filelist = [shortname, fullpath]
        self.samples = []       # list of Sample objects
        for root, _, files in os.walk(rootPath):
            for basename in files:
                if fnmatch.fnmatch(basename, sample_xtn):
                    filename = os.path.join(root, basename)
                    self.sample_list.append([basename, filename])
                    self.samples.append(Sample(filename))
                
                
    def __str__(self):
        txt = 'Data files read from :\n'
        txt += data_fldr + '\n'
        for row in self.filelist:
            txt += row[0] + '\n'
            
            
        txt += '\nList of available sample definitions\n'
        for d in self.sample_list:
            txt += d[0]  #.ljust(30) + d[1] + '\n'            
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
        for row in self.filelist:
            print(row[0])
        
            
    def get_sample(self, filename, col_name):
        lst = self.get_collist_by_name(filename, col_name)
        return random.choice(lst)
    
    def get_collist_by_name(self, filename, col_name):
        with open(filename) as f:
            ndx = 0
            res = []
            for num, line in enumerate(f):
                #print('line',line, 'num',num)
                cols = line.split(',')
                if num == 0:
                    for col_num, col in enumerate(cols):
                        if col.strip('"') == col_name:
                            ndx = col_num
    
                res.append(cols[ndx].strip('"'))
        return [set(res)]            
   
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
        for l in self.sample_list:
            res += l + '\n'
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
                

   
if __name__ == '__main__':
    TEST()