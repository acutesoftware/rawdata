# test_generate.py

import unittest
import random
import rawdata.generate

class TestGenerate(unittest.TestCase):
    
    def test_01_random_int(self):
        n = rawdata.generate.NumberGenerator()
        self.assertEqual(n.random_int(1,100) > 100, False)
        self.assertEqual(n.random_int(1,100) > 0, True)
        self.assertEqual(n.random_int(0,1), 0)
        self.assertEqual(n.random_int(50,51), 50)
        self.assertEqual(n.random_int(999,5555) > 999, True)

    def test_02_random_letters(self):
        s = rawdata.generate.StringGenerator()
        self.assertEqual(len(s.random_letters(1)), 1)
        self.assertEqual(len(s.random_letters(5)), 5)
        self.assertEqual(len(s.random_letters(500)), 500)
        
    def test_03_generate_password(self):
        s = rawdata.generate.StringGenerator()
        self.assertEqual(len(s.generate_password(6)), 8)  # 8 char min enforced
        self.assertEqual(len(s.generate_password(8)), 8) 
        self.assertEqual(len(s.generate_password(10)), 10) 
        self.assertEqual(len(s.generate_password()), 18)  # default 18 char
        self.assertEqual(len(s.generate_password(22)), 22) 
    
    def test_04_random_table(self):
        colLabel = ['DATE', 'name', 'password', 'Born',  'Quote', 'Score']
        colTypes = ['DATE', 'PEOPLE', 'STRING', 'PLACE', 'WORD',  'INT']
        t = rawdata.generate.TableGenerator(500, colTypes, colLabel)
        #print(tbl)
        self.assertEqual(len(t.tbl), 501)       # 500 rows plus header
        self.assertEqual(len(t.tbl[0]), 6)      # check for 6 columns
        self.assertEqual(t.tbl[0][0], 'DATE') 
        self.assertEqual(t.tbl[0][1], 'name') 
        self.assertEqual(t.tbl[0][2], 'password') 
        self.assertEqual(t.tbl[0][3], 'Born') 
        self.assertEqual(t.tbl[0][4], 'Quote') 
        self.assertEqual(t.tbl[0][5], 'Score') 
    
    def test_05_table_with_custom_list(self):
        my_colours = ['Blue', 'Green', 'Orange']
        tbl = rawdata.generate.TableGenerator(99, ['PEOPLE', my_colours], ['Name', 'MyCols'])
        #print(tbl)
        #print(tbl.get_column(1))
        self.assertEqual('Blue' in tbl.get_column(1), True) 
        self.assertEqual('Green' in tbl.get_column(1), True) 
        self.assertEqual('Orange' in tbl.get_column(1), True) 


    def test_06_function_generator(self):
        rng_mult = [-9999,9999]
        rng_expt = [0,999]
        #rng = [-2,9]
        f1 = rawdata.generate.FunctionGenerator(rng_mult, rng_expt, num_terms=3)
        self.assertEqual('a' in f1.equation, True) 
        self.assertEqual('b' in f1.equation, True) 
        self.assertEqual('c' in f1.equation, True) 
        
        self.assertEqual(f1.mult[0] >= rng_mult[0], True) 
        self.assertEqual(f1.mult[0] < rng_mult[1]+1, True) 
        
        self.assertEqual(f1.expt[0] >= rng_expt[0], True) 
        self.assertEqual(f1.expt[0] < rng_expt[1]+1, True) 
        
        #print(f1)
    def test_07_function_answer(self):
        """
        Set the max and min ranges for randomisation the same
        to generate a fixed equation to test against known answers
        Equation   : 2a^2+2b^2+2c^2
        Parameters : a=1,b=2,c=3
        answer     : 10        
        """
        rng_mult = [2,2]
        rng_expt = [2,2]
        f3 = rawdata.generate.FunctionGenerator(rng_mult, rng_expt, num_terms=3)
        self.assertEqual(f3.equation, '2a^2+2b^2+2c^2')
        c1 = rawdata.generate.FunctionCalculator(f3, [1,2,3])
        self.assertEqual(c1.answer, '10')
        c2 = rawdata.generate.FunctionCalculator(f3, [5,-4,33])
        self.assertEqual(c2.answer, '82')
        c3 = rawdata.generate.FunctionCalculator(f3, [1.72,2.32,5.115])
        self.assertEqual(c3.answer, '16.6816')
        c4 = rawdata.generate.FunctionCalculator(f3, [-2,-66,4543.1118])
        self.assertEqual(c4.answer, '8720')
        #print(c3)
        
        
    def test_08_function_calculator(self):
        rng_mult = [-9,99]
        rng_expt = [0,9]
        f2 = rawdata.generate.FunctionGenerator(rng_mult, rng_expt, num_terms=3)
        
        
        
        for i in range(5):
            n = rawdata.generate.NumberGenerator()
            params = [n.random_int(i,i+5), n.random_int(i,i+5), n.random_int(i,i+5)]
            c = rawdata.generate.FunctionCalculator(f2, params, i)
            #print(c)
 
        
if __name__ == '__main__':
    unittest.main()
