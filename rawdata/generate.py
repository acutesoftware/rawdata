#!/usr/bin/python3

import os
import random
import binascii
import string

root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) )

dat_fldr = root_fldr + os.sep + 'data' 
names    = dat_fldr + os.sep + 'names.csv'  # http://www.cs.princeton.edu/introcs/data/names.csv
places   = dat_fldr + os.sep + 'countries.csv'  
wordList = dat_fldr + os.sep + 'nouns.txt'
    
class Structure(object):
    """
    core container to manager data generation
    structures
    """
    pass
  
class NumberGenerator(Structure):
    """
    Creates a random currency value based on likely
    cent values 
    """
    def __init__(self, cents='Normal'):
        """
        pass a random choice cent selection
        """
        if cents == 'Normal':
            self.cent_choices = ['00','00','00','00','10','50','95','95','95','98','99','99']
        elif cents == 'fives':
            self.cent_choices = ['{:0>2}'.format(c) for c in range(0,99,5)]
        else:
            self.cent_choices = ['{:0>2}'.format(c) for c in range(0,99)]
    
    def random_int(self, min_v=0, max_v=100):
        return random.randrange(min_v, max_v)
        
    def random_currency(self, start=9, end=499.9999979797):
        cents = random.choice(self.cent_choices)
        if end == 499.9999979797:
            end = 499
            sign = random.choice(['$','', '+$', '+'])
        else:
            sign = random.choice(['$', '+$', '-$', '-', '', '$ ', ''])
        dollars = random.randint(start,end)
        return sign + str(dollars) + '.' + cents
        
class StringGenerator(Structure):
    """
    generates random strings
    """
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
        
    def bytes_to_str(self, btes):
        return btes.decode("utf-8")
        
    def str_to_bytes(self, txt):
        return bytes(txt, encoding="UTF-8")
        
    def unicode_to_ascii(self, txt, destructive=True):
        """
        take an unknown unicode string as 'str' and convert
        to ASCII. If destructive, then ignore unknown chars
        otherwise attempt to convert via mapping.
        """
        print('TODO')
        return txt
      
        

class FunctionGenerator(object):
    """
    generates a random polynomial function
    """
    def __init__(self, mult_range, exp_range, num_terms=3):
        if num_terms is None:
            num_terms = random.randint(2, 9)
        self.num_terms = num_terms
        self.equation = ''
        self.mult = [random.randint(mult_range[0], mult_range[1] ) for _ in range(self.num_terms + 1)]
        self.expt = [random.randint(exp_range[0], exp_range[1]) for _ in range(self.num_terms + 1)]
        
        for i in range(self.num_terms):
            letter = chr(97 + i)
            sign = ''
            if self.mult[i] >= 0:
                if i > 0:
                    sign = '+'
            self.equation += sign + str(self.mult[i]) + letter + '^' + str(self.expt[i])
                
    def __str__(self):
        return 'Equation   : ' + self.equation 
        
class FunctionCalculator(object):
    """
    uses a FunctionGenerator object 'func' to
    run calculations over a set of parameters
    PARAMETERS:
        func    : FunctionGenerator() object
        params  : [3, 4, 1] # list with ONE value per term (x,y,z...) 
        test_id : optional integer for naming when logging
    USAGE:
        f = FunctionGenerator(mult_range=[-9,9], exp_range=[0,5], num_terms=3)
        print(f)
        for i in range(5):
            c = FunctionCalculator(f, [n.random_int(), n.random_int(), n.random_int()], i)
            print(c)
    RETURNS:
        Equation   : 7x^5 -1x^4 -6x^1
        Parameters : 1,4,7 => answer     : -249.000000000
        Parameters : 8,8,0 => answer     : 225280.000000000
        Parameters : 4,3,5 => answer     : 7087.000000000
        Parameters : 1,8,2 => answer     : -4089.000000000
        Parameters : 7,3,8 => answer     : 117568.000000000    
    """
    def __init__(self, func, params, test_id=1):
        self.test_id = 'math_test_' + str(test_id)
        if len(params) != func.num_terms:
            assert('Error first parameter not equal to number of terms of function')
        self.params = params
        ans = 0
        #for param_num, p in enumerate(self.params):
        for i in range(func.num_terms - 1):
            ans += func.mult[i] * params[i] ** func.expt[i]
        #self.answer = '%.9f' %ans
        self.answer = str(ans)

    def __str__(self):
        res = 'Parameters : '
        res += ','.join([chr(97 + i) + '=' + str(t) for i,t in enumerate(self.params)]) + ' => '
        res += 'answer     : ' + self.answer # + '\n'
        return res
            
        
        
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
        
        
        print('Generating columns - ', colTypes)
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

def get_list_string(num = 40):
    s = StringGenerator()
    return [s.random_letters(num) for _ in range(0,100)]
                
            
def get_rand_text_from_list(lst):
    return lst[random.randrange(0, len(lst))]
    

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
    
"""
def get_list_from_file(fname, col_name):
    col_ndx = 0
    lst = []
    with open(fname, 'r') as f:
        line = f.readline()
        hdrs = line.split(',')
        for num, c in enumerate(hdrs):
            if c == col_name:
                col_ndx = num
        
        # now read the rest
        for line in f:
            cols = line.split(',')
            lst.append(cols[col_ndx])
    return lst
"""        
def get_list_words():
    """
    reads wordnet to get a unique list of nouns
    """
    with open(wordList) as f:
        return [line.strip().replace('_', ' ') for line in f if random.randrange(1,100) > 90]

def get_list_dates(start_date=1985, end_date=2015):
    """
    picks a random year
    """
    return [i for i in range(start_date, end_date)]

def get_list_places():
    """
    picks a random country
    """
    print('get_list_places : places= ', places )
    with open(places) as f:
        return [line.split(',')[1].strip().strip('"').title() for line in f]

def get_list_people():
    """
    chooses a random name from names.csv
    """
    with open(names) as f:
        return [line.split(',')[0].title() for line in f]
    
