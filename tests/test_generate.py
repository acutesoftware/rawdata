# test_generate.py

import unittest
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
    
if __name__ == '__main__':
    unittest.main()
