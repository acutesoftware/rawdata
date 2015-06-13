
import os
import random
import binascii
import string
import rawdata.content


root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) )

dat_fldr = root_fldr + os.sep + 'data' 
names    = dat_fldr + os.sep + 'names.csv'  # http://www.cs.princeton.edu/introcs/data/names.csv
places   = dat_fldr + os.sep + 'countries.csv'  
wordList = dat_fldr + os.sep + 'nouns.txt'

def TEST():
    print('generate.py')
    print('Creates random data and strings in various formats')
    s = StringGenerator()
    print('Random Strings....\n  ', s.random_hex_string(20), '\n  ', s.random_letters(50))
    print('Random Block ....')
    print(s.random_block(30,11))
    print('Data Table ....')
    colLabel = ['DATE', 'name', 'password', 'Born',  'Quote', 'Score']
    colTypes = ['DATE', 'PEOPLE', 'STRING', 'PLACE', 'WORD',  'INT']
    tbl = TableGenerator(5, colTypes, colLabel)
    print(tbl)
    #save_table(tbl, 'test123.csv')
    print('password generator = ', s.generate_password(10))
    
    n = NumberGenerator()
    print('random_currency = ', n.random_currency())

     
    # table with a custom list
    custom_list = ['Carved Statue', '1984 Volvo', '2 metre Ball of string']
    tbl = TableGenerator(8, ['PEOPLE', 'INT', custom_list], ['Name', 'Age', 'Fav Possession'])
    print(tbl)
 
    # table with loaded list
    
    
class Structure(object):
    """
    core container to manager data generation
    structures
    """
    pass

    

class NumberGenerator(Structure):
    def random_int(self, min_v=0, max_v=100):
        return random.randrange(min_v, max_v)
        
    def random_currency(self, start=9, end=499):
        cents = random.choice(['00','10','50','95','99'])
        dollars = random.randint(start,end)
        sign = random.choice(['$', '+$', '-$', '-', '', '$ ', ''])
        return sign + str(dollars) + '.' + cents
        

class StringGenerator(Structure):
    def random_letters(self, sze=20):
        lst = [random.choice(string.ascii_letters + string.digits) for _ in range(sze)]
        return "".join(lst)

    def generate_password(self, sze=18):
        if sze < 8: sze = 8
        first_half = sze - 6
        n = NumberGenerator()
        return self.random_letters(first_half).lower() + str(n.random_int(10,99)) + self.random_letters(4).upper()
        
    def random_hex_string(self, sze=30):
        return binascii.b2a_hex(os.urandom(sze))
        
    def random_block(self, cols=40, rows=5):
        return ''.join([self.random_letters(cols) + '\n' for _ in range(0,rows)])

def get_list_string(num = 40):
    s = StringGenerator()
    return [s.random_letters(num) for _ in range(0,100)]
    
class TableGenerator(Structure):
    """
    holds a table and manages the cleaning and 
    creation of DQ issues
    """
    def __init__(self, tot_rows, col_types, col_label):
        self.tot_rows = tot_rows
        self.col_types = col_types
        col_label = col_label
        self.tbl = []
        s = StringGenerator()
        n = NumberGenerator()      
        # verify the col_types required and assign defaults to empty sets
        cols = len(col_types)
        #colTypes = fill_colList_blanks(col_types, cols)
        colTypes = col_types
        
        
        #print('Generating columns - ', colTypes)
        wordLists = load_lists(colTypes)
        self.tbl.insert(0, col_label) # column headers
        for _ in range(0,tot_rows):
            thisRow = []
            txt = ''
            for c in range(0, cols):
                if colTypes[c] == 'INT':
                    txt = str(n.random_int())
                elif colTypes[c] == 'STRING':
                    txt = s.random_letters()
                elif colTypes[c] == 'CURRENCY':
                    txt = n.random_currency(9, 499)
                elif isinstance((colTypes[c]), (list, tuple)):
                    # getting random data from passed list
                    txt = get_rand_text_from_list(colTypes[c])
                else:
                    for lst in wordLists:
                        if lst['name'] != 'INT':
                            if lst['name'] == colTypes[c]:
                                txt = get_rand_text_from_list(lst['lst'])
                thisRow.append(txt)
            self.tbl.append(thisRow)
        

    def __str__(self):
        txt = '\n'.join(','.join([col if type(col) is str else str(col) for col in row]) for row in self.tbl)
        return txt

    def get_column(self, ndx):
        res = []
        for r in self.tbl:
            res.append(r[ndx])
        return res    

        
    def save_table(self,  fname, delim=',', qu='"'):
        with open(fname, "wt") as f:
            f.write('\n'.join(delim.join([qu + col + qu if type(col) is str else qu + str(col) + qu for col in row]) for row in self.tbl))

def get_rand_text_from_list(lst):
    return lst[random.randrange(0, len(lst))]
    
def fill_colList_blanks(partialCols, numRequiredCols):
    """
    no idea why this function is here - probably at start
    when trying to autofill table, but it needs to go
    """
    colWord = []
    num = 0
    for _ in range(0, numRequiredCols):
        tpe = partialCols[num]
        if tpe == '': 
            tpe = 'STRING'
        colWord.append(tpe)
        num = num + 1
    return colWord

def load_lists(lst):
    """
    loads a sample of data for each type in lst
        l =  PEOPLE
        l =  INT
        l =  ['Carved Statue', '1984 Volvo', '2 metre Ball of string']
    
    lists_to_load = {l for l in lst}	# get unique list of types so only loading them once each
    """
    results = []	
    lists_to_load = []
    for l in lst:
        #print(' l = ', l)
        if isinstance(l, (list, tuple)):
            results.append({'name': 'LIST', 'lst': l})
        else:
            lists_to_load.append(l)
    
    
    for tpe in lists_to_load:
        if tpe == 'STRING2':
            results.append({'name': 'STRING', 'lst': get_list_string(40)})
        if tpe == 'STRING':
            results.append({'name': 'STRING', 'lst': get_list_string()})
        if tpe == 'WORD':
            results.append({'name': 'WORD', 'lst': get_list_words()})
        if tpe == 'DATE':
            results.append({'name': 'DATE', 'lst': get_list_dates()})
        if tpe == 'PLACE':
            results.append({'name': 'PLACE', 'lst': get_list_places()})
        if tpe == 'PEOPLE':
            results.append({'name': 'PEOPLE', 'lst': get_list_people()})
    return results

        
def get_list_words():
    with open(wordList) as f:
        return [line.strip().replace('_', ' ') for line in f if random.randrange(1,100) > 90]

def get_list_dates():
    return [i for i in range(1985, 2014)]

def get_list_places():
    with open(places) as f:
        return [line.split(',')[2].strip().strip('"').title() for line in f]

def get_list_people():
    with open(names) as f:
        return [line.split(',')[0].title() for line in f]
    
            
if __name__ == '__main__':
    TEST()	
    
