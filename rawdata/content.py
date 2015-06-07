# content.py

import os

data_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'data' ) 

def TEST():
    #c = Content('finance', [4,3,5])
    #print(c)
    s = Samples()
    print(s.get_list())
    s.get_sample('countries.csv')
    

class Content(object):
    """
    core content object that others are derived
    """
    def __init__(self, content_type, content_range):
        self.content_type = content_type
        self.content_range = content_range
        
    def __str__(self):
        return self.content_type
        
    def save(self):
        pass
    def load(self):
        pass
        
class Samples(object):
    """
    read samples from data subfolder to get lists
    """
    def __init__(self):
        self.filelist = []
        for root, dirs, files in os.walk(data_fldr):
            for f in files:
                self.filelist.append([root + os.sep + f, root,f])

    def __str__(self):
        txt = 'Samples read from :\n'
        for row in self.filelist:
            txt += '   ' + row[0] + '\n'
        return txt    
    
    def get_list(self):
        for row in self.filelist:
            print(row[2][:-4])
            
    def get_sample(self, list):
        with open(data_fldr + os.sep + list) as f:
            for num, line in enumerate(f):
                if num < 10:
                    print(line)
            
            
            
if __name__ == '__main__':
    TEST()