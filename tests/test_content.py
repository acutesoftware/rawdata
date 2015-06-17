#!/usr/bin/python3
# test_content.py

import unittest
import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
test_fldr = os.path.dirname(__file__) + os.sep + 'test_results'
sys.path.insert(1, root_fldr)

import rawdata.generate
import rawdata.content

class TestContent(unittest.TestCase):
    def test_01_check_sample_datafiles(self):
        s = rawdata.content.Samples()
        all_files = s.get_list()
        #print(len(all_files))
        self.assertEqual(len(all_files) > 12, True)  # check for at least 12 data files
        self.assertEqual(all_files[0][2],'countries.csv')

    def test_02_get_collist(self):
        s = rawdata.content.Samples()
        data_file = rawdata.content.data_fldr + os.sep + 'games' + os.sep + 'skills.csv'
        col1 = s.get_collist_by_name(data_file, 'type' )
        self.assertEqual(col1, [{'buff', 'change', 'build', 'type', 'info', 'gather', 'attack', 'heal'}])
        
    def test_03_read_list(self):
        s = rawdata.content.Samples()
        fname = rawdata.content.data_fldr + os.sep + 'food' + os.sep + 'food_desc.csv'
        food_list = s.get_collist_by_name(fname, 'Long_Desc')
        self.assertEqual(len(food_list[0]), 1114)
    
if __name__ == '__main__':
    unittest.main()
