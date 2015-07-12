#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_content.py

import unittest
import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep + 'rawdata'
test_fldr = os.path.dirname(__file__) + os.sep + 'test_results'
sys.path.insert(1, root_fldr)

import generate
import content

class TestContent(unittest.TestCase):
    def test_01_check_sample_datafiles(self):
        s = content.DataFiles()
        all_files = s.get_list()
        #print(len(all_files))
        self.assertEqual(len(all_files) > 12, True)  # check for at least 12 data files
        #self.assertEqual(all_files[0][2],'countries.csv')

    def test_02_get_collist(self):
        s = content.DataFiles()
        data_file = content.data_fldr + os.sep + 'games' + os.sep + 'skills.csv'
        col1 = s.get_collist_by_name(data_file, 'type' )
        self.assertEqual(col1, [{'buff', 'change', 'build', 'type', 'info', 'gather', 'attack', 'heal'}])
        
    def test_03_read_list(self):
        s = content.DataFiles()
        fname = content.data_fldr + os.sep + 'food' + os.sep + 'food_desc.csv'
        food_list = s.get_collist_by_name(fname, 'Long_Desc')
        self.assertEqual(len(food_list[0]), 1114)
    
    def test_04_read_data_copper(self):
        # get list of countries from copper production
        s = content.DataFiles()
        fname = content.data_fldr + os.sep + 'finance' + os.sep + 'mining_copper_rent.csv'
        country_names_copper = s.get_collist_by_name(fname, 'Country Name')  # country code, Country Name
        self.assertEqual(len(country_names_copper[0]), 68)  # 68 countries mine copper
        # print(country_names_copper)
        # [{'CHILE', 'AUSTRALIA', 'UNITED KINGDOM', 'Cuba', 'SOUTH AFRICA', 'INDONESIA', 
        #   'GUATEMALA', 'PHILIPPINES', 'NORWAY', 'ZIMBABWE', 'AUSTRIA', 'CYPRUS', 'CHINA', ...
    
    def test_05_list_data_file_columns(self):
        """
        d = DataFiles()
        print('Datafiles', d)
        print('columns')
        for c in d.columns:
            print(c[0][len(data_fldr) + 1:] + '.' + c[2] + '.' + c[3])
        for r in d.columns:
            print(r[4])
            print(len(r[4]))
        """
        d = content.DataFiles()
        try:
            self.assertEqual(len(d.columns) > 1, True)
            
            print(d.lookup[0:5])
            self.assertEqual('finance.mining_copper_rent.2002' in d.lookup, True)
            self.assertEqual('food.food_desc.Ref_Desc' in d.lookup, True)
            self.assertEqual('games.materials.name' in d.lookup, True)
            self.assertEqual('.countries.country_code' in d.lookup, True)  # this should be moved
        except Exception:
            print('Error running test_05_list_data_file_columns')
    
    def test_06_get_unique_list(self):
        s = content.get_unique_list('food.food_desc.Ref_Desc')
        print(s)
    
    def test_07_choose_value(self):
        s = content.choose_value('food.food_desc.Ref_Desc')
        print(s)
    
    def test_08_choose_weighted_value(self):
        s = content.choose_weighted_value('food.food_desc.Ref_Desc')
        print(s)
    
    
if __name__ == '__main__':
    unittest.main()
