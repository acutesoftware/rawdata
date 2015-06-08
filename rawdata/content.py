# content.py

import os
import random

data_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'data' ) 

def TEST():
    #c = Content('finance', [4,3,5])
    #print(c)
    s = Samples()
    print(s.get_list())
    col1 = s.get_collist_by_name(data_fldr + os.sep + 'games' + os.sep + 'skills.csv', 'type' )
    print(col1)
    
    # get list of countries from copper production
    country_names_copper = s.get_collist_by_name(data_fldr + os.sep + 'finance' + os.sep + 'mining_copper_rent.csv', 'Country Name')  # country code, Country Name'2006'
    print(country_names_copper)
    # [{'CHILE', 'AUSTRALIA', 'UNITED KINGDOM', 'Cuba', 'SOUTH AFRICA', 'INDONESIA', 
    #   'GUATEMALA', 'PHILIPPINES', 'NORWAY', 'ZIMBABWE', 'AUSTRIA', 'CYPRUS', 'CHINA', ...

    

    # get categories from custom CSV file
    csv_local = data_fldr + os.sep + 'finance_categories.txt'
    lst = []
    with open(csv_local, 'r') as f:
        for line in f:
            #print(line)
            if line[0] != '#' and line != '':
                content = line.split(':')
                if content[0] == 'bills':
                    lst = content[1].split(',')
    print(lst[0:5])
    
    # get food lists
    food = s.get_collist_by_name(data_fldr + os.sep + 'food' + os.sep + 'food_desc.csv', 'Long_Desc')
    for f in food[0]:
        print(f)
    
        
    
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
        for root, _, files in os.walk(data_fldr):
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
        #return res     
                    
if __name__ == '__main__':
    TEST()