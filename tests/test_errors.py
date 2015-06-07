# test_errors.py

import unittest
import rawdata.generate
import rawdata.errors

class TestCreate(unittest.TestCase):
    
    def test_01_create_error(self):
        e = rawdata.errors.DataError('Random Text')
        self.assertEqual(str(e),'Random Text')
        #print(e)

    def test_02_error_fixed_val(self):
        e = rawdata.errors.DataError('BAD STRING')
        self.assertEqual(e._fixed_val(),'BAD STRING')

    def test_03_error_blank_out(self):
        e = rawdata.errors.DataError('Originally Valid Text')
        self.assertEqual(e._blank_out(),'')

    def test_03_error_add_spaces(self):
        e = rawdata.errors.DataError('')
        self.assertEqual(e._add_spaces('AAA'),' AAA     ')

    def test_03_error_add_random(self):
        # not sure what error will occur, but ensure input string is different
        e = rawdata.errors.DataError('BAD STRING')
        self.assertEqual(e.random_error('Orig') != 'Orig', True)
        
        
    def test_10_table_swap_columns(self):
        colLabel = ['DATE', 'name',   'Born']
        colTypes = ['DATE', 'PEOPLE', 'PLACE']
        good_table = rawdata.generate.TableGenerator(40, colTypes, colLabel)
        t = rawdata.errors.TableWithErrors(good_table, 'BLAH')
        self.assertEqual(t.tbl[0],['DATE', 'name', 'Born'])
        t.swap_columns(0,1)
        self.assertEqual(t.tbl[0],['name', 'DATE', 'Born'])
        t.swap_columns(1,2)
        self.assertEqual(t.tbl[0],['name', 'Born', 'DATE'])
        t.swap_columns(2,0)
        self.assertEqual(t.tbl[0],['DATE', 'Born', 'name'])
        self.assertEqual(len(t.tbl[0]),3)  # confirm 3 columns in header
    
    
    
    
if __name__ == '__main__':
    unittest.main()
