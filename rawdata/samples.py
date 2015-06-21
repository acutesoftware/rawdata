#!/usr/bin/python3
# samples.py

import os
import fnmatch

rootPath = os.getcwd() + os.sep + 'samples'
sample_xtn = '*.sample'

def main():
    """
    Generates sample tables - run main() to see examples
    but normal operation is to call from program or api.
    """
    print('samples.py')
    print('Creates random data and strings in various formats')
    s = Samples()
    #print(s)
    #print(s.samples[0])
    f = s.get_sample_by_name('finance_transaction')
    print(f)
    
    #print(f.col_labels)
    #print(f.col_types)
    
    
    
class Samples(object):
    """
    Manages the list of all sample files and allows for
    searching by term.
    Definitions are stored in /rawdata/samples/*.sample
    import rawdata.samples as sample
    s = sample.Sample()
    print(s.list())    # shows list of available samples
    s1 = s.show('finance.bank_transactions') 
    s2 = s.show('course.subjects') 
    """
    def __init__(self):
        """
        scan folder for list of available sample files
        """
        self.sample_list = []  # filelist = [shortname, fullpath]
        self.samples = []       # list of Sample objects
        for root, _, files in os.walk(rootPath):
            for basename in files:
                if fnmatch.fnmatch(basename, sample_xtn):
                    filename = os.path.join(root, basename)
                    self.sample_list.append([basename, filename])
                    self.samples.append(Sample(filename))
                    
        
    def __str__(self):
        res = 'List of available sample definitions\n'
        for d in self.sample_list:
            res += d[0]  #.ljust(30) + d[1] + '\n'
        return res
    
    def get_sample_by_name(self, txt):
        """
        returns the first Sample that matches txt
        """
        for s in self.samples:
            if txt + '.sample' in s.fullname:
                return s
        return None
    

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
    main()	
    
        