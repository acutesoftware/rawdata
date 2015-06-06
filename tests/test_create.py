# test_create.py

import unittest
import rawdata.create
import rawdata.generate

colLabel = ['DATE', 'name',   'Born']
colTypes = ['DATE', 'PEOPLE', 'PLACE']
tbl = rawdata.generate.random_table(40, colTypes, colLabel)


class TestCreate(unittest.TestCase):
    
    def test_01_create_error(self):
        e = rawdata.create.DataError('Random Text')
        self.assertEqual(str(e),'Random Text')
        #print(e)

    def test_02_error_fixed_val(self):
        e = rawdata.create.DataError('BAD STRING')
        self.assertEqual(e._fixed_val(),'BAD STRING')

    def test_03_error_blank_out(self):
        e = rawdata.create.DataError('Originally Valid Text')
        self.assertEqual(e._blank_out(),'')

    def test_03_error_add_spaces(self):
        e = rawdata.create.DataError('')
        self.assertEqual(e._add_spaces('AAA'),' AAA     ')

    def test_03_error_add_random(self):
        # not sure what error will occur, but ensure input string is different
        e = rawdata.create.DataError('BAD STRING')
        self.assertEqual(e.random_error('Orig') != 'Orig', True)
        
    def test_09_create_table(self):
        t = rawdata.create.Table(tbl, '')
        self.assertEqual(len(tbl),41)  # confirm 40 rows + header
        self.assertEqual(len(tbl[0]),3)  # confirm 40 rows
        
    def test_10_table_swap_columns(self):
        t = rawdata.create.Table(tbl, '')
        self.assertEqual(tbl[0],['DATE', 'name', 'Born'])
        t.swap_columns(0,1)
        self.assertEqual(tbl[0],['name', 'DATE', 'Born'])
        t.swap_columns(1,2)
        self.assertEqual(tbl[0],['name', 'Born', 'DATE'])
        t.swap_columns(2,0)
        self.assertEqual(tbl[0],['DATE', 'Born', 'name'])
        self.assertEqual(len(tbl[0]),3)  # confirm 3 columns in header
    
    
    
    
if __name__ == '__main__':
    unittest.main()
