#!/usr/bin/python3
# test_errors.py

import unittest
import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
test_fldr = os.path.dirname(__file__) + os.sep + 'test_results'
sys.path.insert(1, root_fldr + os.sep + 'rawdata')

import generate
import errors

class TestCreate(unittest.TestCase):
    
    def test_01_create_error(self):
        e = errors.DataError('Random Text')
        self.assertEqual(str(e),'Random Text')

    def test_02_error_fixed_val(self):
        e = errors.DataError('BAD STRING')
        self.assertEqual(e._fixed_val(),'BAD STRING')

    def test_03_error_blank_out(self):
        e = errors.DataError('Originally Valid Text')
        self.assertEqual(e._blank_out(),'')

    def test_03_error_add_spaces(self):
        e = errors.DataError('')
        self.assertEqual(e._add_spaces('AAA'),' AAA     ')
        
        self.assertEqual(e._add_spaces(3.111),' 3.111     ')
        self.assertNotEqual(e._add_spaces(3),'3')
        

    def test_03_error_add_random(self):
        # not sure what error will occur, but ensure input string is different
        e = errors.DataError('BAD STRING')
        self.assertEqual(e.random_error('Orig') != 'Orig', True)
        
    def test_10_table_swap_columns(self):
        colLabel = ['DATE', 'name',   'Born']
        colTypes = ['DATE', 'PEOPLE', 'PLACE']
        good_table = generate.TableGenerator(40, colTypes, colLabel)
        t = errors.TableWithErrors(good_table, 'BLAH')
        self.assertEqual(t.tbl[0],['DATE', 'name', 'Born'])
        t.swap_columns(0,1)
        self.assertEqual(t.tbl[0],['name', 'DATE', 'Born'])
        t.swap_columns(1,2)
        self.assertEqual(t.tbl[0],['name', 'Born', 'DATE'])
        t.swap_columns(2,0)
        self.assertEqual(t.tbl[0],['DATE', 'Born', 'name'])
        self.assertEqual(len(t.tbl[0]),3)  # confirm 3 columns in header
        
    def test_11_table_bad_data(self):
        colLabel = ['Year',  'Born', 'Fav number']
        colTypes = ['DATE', 'PLACE', 'INT']
        good_table = generate.TableGenerator(10, colTypes, colLabel)
        t11 = errors.TableWithErrors(good_table, 'WRONG_STRING')
        self.assertEqual(str(t11)[0:20], 'Year,Born,Fav number')
        self.assertEqual(t11.header, ['Year', 'Born', 'Fav number'])
        t11.add_errors(150)  # make sure all error types get called

        
    def test_12_load_from_file(self):
        cntry_tbl = generate.TableGenerator(1, ['Code', 'Country'], ['STRING', 'STRING'])
        t12 = errors.TableWithErrors(cntry_tbl, '')
        t12.load_from_file(errors.data_fldr + os.sep + 'countries.csv')
