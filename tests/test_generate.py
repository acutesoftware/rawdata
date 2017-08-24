#!/usr/bin/python3
# test_generate.py

import unittest
import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep + 'rawdata'
test_fldr = os.path.dirname(__file__) + os.sep + 'test_results'
sys.path.insert(1, root_fldr)

import random
import generate as generate

class TestGenerate(unittest.TestCase):
    
    def test_01_random_int(self):
        n = generate.NumberGenerator()
        self.assertEqual(n.random_int(1,100) > 100, False)
        self.assertEqual(n.random_int(1,100) > 0, True)
        self.assertEqual(n.random_int(0,1), 0)
        self.assertEqual(n.random_int(50,51), 50)
        self.assertEqual(n.random_int(999,5555) > 999, True)

    def test_02_random_currency(self):
        n2 = generate.NumberGenerator()
        self.assertEqual(len(n2.random_currency(1,100)) > 2, True)
        n3 = generate.NumberGenerator(cents='Normal')
        
        # random_currency(self, start=9, end=499.9999979797)
        self.assertEqual(len(n2.random_currency(2,499.9999979797)) > 4, True)
        
    def test_03_currency_cents(self):
        n4 = generate.NumberGenerator(cents='Normal')
        self.assertEqual(n4.cent_choices, ['00', '00', '00', '00', '10', '50', '95', '95', '95', '98', '99', '99'])

        n5 = generate.NumberGenerator()   # uses cents=Normal as default
        self.assertEqual(n5.cent_choices, ['00', '00', '00', '00', '10', '50', '95', '95', '95', '98', '99', '99'])
        
        n6 = generate.NumberGenerator('fives')
        self.assertEqual(n6.cent_choices[0:5], ['00', '05', '10', '15', '20'])
        self.assertEqual(n6.cent_choices[18:20], ['90', '95'])
        

        n7 = generate.NumberGenerator('all')
        self.assertEqual(len(n7.cent_choices), 99)
        self.assertEqual(n7.cent_choices[0:5], ['00', '01', '02', '03', '04'])
        self.assertEqual(n7.cent_choices[97:99], ['97', '98'])
        

    def test_04_random_letters(self):
        s = generate.StringGenerator()
        self.assertEqual(len(s.random_letters(1)), 1)
        self.assertEqual(len(s.random_letters(5)), 5)
        self.assertEqual(len(s.random_letters(500)), 500)
    
    
    def test_04_random_hexstring(self):
        s = generate.StringGenerator()
        self.assertEqual(len(s.random_hex_string()), 60)

    def test_04_random_block(self):
        s = generate.StringGenerator()
        self.assertEqual(len(s.random_block()), 205)
        print(s.random_block())
    
    def test_04_unicode_to_ascii(self):
        s = generate.StringGenerator()
        self.assertEqual(len(s.unicode_to_ascii('ABCDEF')), 6)

    def test_05_generate_password(self):
        s = generate.StringGenerator()
        self.assertEqual(len(s.generate_password(6)), 8)  # 8 char min enforced
        self.assertEqual(len(s.generate_password(8)), 8) 
        self.assertEqual(len(s.generate_password(10)), 10) 
        self.assertEqual(len(s.generate_password()), 18)  # default 18 char
        self.assertEqual(len(s.generate_password(22)), 22) 
    
    def test_06_random_table(self):
        colLabel = ['DATE', 'name', 'password', 'Born',  'Quote', 'Score',  'Balance']
        colTypes = ['DATE', 'PEOPLE', 'STRING', 'PLACE', 'WORD',  'INT', 'CURRENCY']
        t = generate.TableGenerator(500, colTypes, colLabel)
        self.assertEqual(len(t.tbl), 501)       # 500 rows plus header
        self.assertEqual(len(t.tbl[0]), 7)      # check for all columns
        self.assertEqual(t.tbl[0][0], 'DATE') 
        self.assertEqual(t.tbl[0][1], 'name') 
        self.assertEqual(t.tbl[0][2], 'password') 
        self.assertEqual(t.tbl[0][3], 'Born') 
        self.assertEqual(t.tbl[0][4], 'Quote') 
        self.assertEqual(t.tbl[0][5], 'Score') 
        self.assertEqual(t.tbl[0][6], 'Balance') 
        t.save_table('random_table.csv')
        self.assertEqual(os.path.exists('random_table.csv'), True)
        
    def test_07_table_with_custom_list(self):
        my_colours = ['Blue', 'Green', 'Orange']
        tbl = generate.TableGenerator(99, ['PEOPLE', my_colours], ['Name', 'MyCols'])
        self.assertEqual('Blue' in tbl.get_column(1), True) 
        self.assertEqual('Green' in tbl.get_column(1), True) 
        self.assertEqual('Orange' in tbl.get_column(1), True) 
        self.assertEqual(str(tbl)[0:11], 'Name,MyCols')


    def test_08_function_generator(self):
        rng_mult = [-9999,9999]
        rng_expt = [0,999]
        f1 = generate.FunctionGenerator(rng_mult, rng_expt, num_terms=3)
        f2 = generate.FunctionGenerator(rng_mult, rng_expt)
        self.assertEqual(len(str(f2)) > 5, True) 
        self.assertEqual('a' in f1.equation, True) 
        self.assertEqual('b' in f1.equation, True) 
        self.assertEqual('c' in f1.equation, True) 
        
        self.assertEqual(f1.mult[0] >= rng_mult[0], True) 
        self.assertEqual(f1.mult[0] < rng_mult[1]+1, True) 
        
        self.assertEqual(f1.expt[0] >= rng_expt[0], True) 
        self.assertEqual(f1.expt[0] < rng_expt[1]+1, True) 
        
    def test_09_function_answer(self):
        """
        Set the max and min ranges for randomisation the same
        to generate a fixed equation to test against known answers
        Equation   : 2a^2+2b^2+2c^2
        Parameters : a=1,b=2,c=3
        answer     : 10        
        """
        rng_mult = [2,2]
        rng_expt = [2,2]
        f3 = generate.FunctionGenerator(rng_mult, rng_expt, num_terms=3)
        self.assertEqual(f3.equation, '2a^2+2b^2+2c^2')
        c1 = generate.FunctionCalculator(f3, [1,2,3])
        self.assertEqual(c1.answer, '10')
        self.assertEqual(len(str(c1)) > 5, True)
        c2 = generate.FunctionCalculator(f3, [5,-4,33])
        self.assertEqual(c2.answer, '82')
        c3 = generate.FunctionCalculator(f3, [1.72,2.32,5.115])
        self.assertEqual(c3.answer, '16.6816')
        c4 = generate.FunctionCalculator(f3, [-2,-66,4543.1118])
        self.assertEqual(c4.answer, '8720')
        
        
    def test_10_function_calculator(self):
        rng_mult = [-9,99]
        rng_expt = [0,9]
        f2 = generate.FunctionGenerator(rng_mult, rng_expt, num_terms=3)
        
        for i in range(5):
            n = generate.NumberGenerator()
            params = [n.random_int(i,i+5), n.random_int(i,i+5), n.random_int(i,i+5)]
            c = generate.FunctionCalculator(f2, params, i)
            print(c)
  
    def test_11_convert_str_and_bytes(self):
        txt = 'abcde'
        self.assertEqual(txt, 'abcde')
        s = generate.StringGenerator()
        b = s.str_to_bytes(txt)
        self.assertEqual(b, b'abcde')
        s2 = s.bytes_to_str(b)
        self.assertEqual(txt, s2)
        
    def test_12_get_dates(self):
        t = generate.TableGenerator(9, ['DATE','YEAR'], ['Date of Birth','Year First Purchased'])
        self.assertEqual(t.tot_rows, 9)
        self.assertEqual(t.col_label, ['Date of Birth','Year First Purchased'])
        self.assertEqual(t.col_types, ['DATE','YEAR'])
        self.assertEqual(len(t.tbl[1][0]), 10)   # 10 character date in yyyy-mm-dd format
        self.assertEqual(len(str(t.tbl[1][1])), 4)   # 4 character year in yyyy format
        self.assertTrue(str(t.tbl[1][1])[0:2] > '18')  # default year starts from 1900ish
        
        
    
    def test_13_more_dates(self):
        d = generate.get_list_dates(start_year=2013, end_year=2016, num_dates=10000)
        self.assertEqual(len(d), 10000)
        self.assertEqual(len(d[23]), 10)
        self.assertEqual(d[0][4:5], '-')
        self.assertEqual(d[0][7:8], '-')
        self.assertTrue(min(d) > '2013-01-00')
        self.assertTrue(max(d) < '2016-12-31')
        
        
    
if __name__ == '__main__':
    unittest.main()        
