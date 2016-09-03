#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_content.py

import unittest
import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep + 'rawdata'
test_fldr = os.path.dirname(__file__) + os.sep + 'test_results'
sys.path.insert(1, root_fldr)
root_path = root_fldr + os.sep + 'samples'
import generate
import content

class TestContent(unittest.TestCase):
    def test_01_check_sample_datafiles(self):
        s = content.DataFiles()
        all_files = s.get_list()
        self.assertEqual(len(all_files) > 12, True)  # check for at least 12 data files
        #self.assertEqual(all_files[0][2],'countries.csv')
        #print(all_files)

    def test_02_get_collist(self):
        s = content.DataFiles()
        data_file = content.data_fldr + os.sep + 'games' + os.sep + 'skills.csv'
        col1 = s.get_collist_by_name(data_file, 'type' )
        self.assertEqual(col1, [{'buff', 'change', 'build', 'info', 'gather', 'attack', 'heal'}])
        
    def test_03_read_list(self):
        s = content.DataFiles()
        fname = content.data_fldr + os.sep + 'food' + os.sep + 'food_desc.csv'
        food_list = s.get_collist_by_name(fname, 'Long_Desc')
        self.assertEqual(len(food_list[0]), 1113)
    
    def test_04_read_data_copper(self):
        # get list of countries from copper production
        s = content.DataFiles()
        fname = content.data_fldr + os.sep + 'finance' + os.sep + 'mining_copper_rent.csv'
        country_names_copper = s.get_collist_by_name(fname, 'Country Name')  # country code, Country Name
        self.assertEqual(len(country_names_copper[0]), 67)  # 68 countries mine copper
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
        self.assertEqual(len(d.columns) > 1, True)
        
        self.assertEqual('finance.mining_copper_rent.2002' in d.lookup, True)
        self.assertEqual('food.food_desc.Ref_Desc' in d.lookup, True)
        self.assertEqual('games.materials.name' in d.lookup, True)
        self.assertEqual('.countries.country_code' in d.lookup, True)  # this should be moved
        #print('d.columns = ', d.columns)
        

    
    
    def test_09_datafile__str__(self):
        d = content.DataFiles()
        self.assertTrue(len(str(d)) > 5000)
        self.assertEqual(str(d)[0:22], 'Data files read from :')
        
    def test_10_datafile_get_list(self):
        d = content.DataFiles()
        list_1 = d.get_list()
        list_2 = d.get_list(True)
        
        #print('list1 = ', list_1)
        #print('list2 = ', list_2)
        
    
    def test_11_datafile_get_list_fullname(self):
        d = content.DataFiles()
        full_list = d.get_list_fullname()
        if full_list:
            self.assertEqual(len(full_list) > 22, True)
    
    def test_12_datafile_get_sample(self):
        fname = content.data_fldr + os.sep + 'food' + os.sep + 'food_desc.csv'
        d = content.DataFiles()
        mysample = d.get_sample(fname, 'Long Desc')
        self.assertTrue(len(mysample) > 3)
    
    def test_13_datafile_get_all_columns(self):
        fname = content.data_fldr + os.sep + 'food' + os.sep + 'food_desc.csv'
        d = content.DataFiles()
        #print(d.get_all_columns(fname))
        self.assertEqual(len(d.get_all_columns(fname)), 14)
        self.assertEqual(d.get_all_columns(fname)[0], 'NDB_No')
        
        # check for dud file
        self.assertEqual(d.get_all_columns('FILE_NOT_FOUND.txt'), None)


     
    def test_14_samples__str__(self):
        tst1 = content.Samples(root_path)
        self.assertEqual(str(tst1)[0:36], 'List of available sample definitions')
    
    def test_15_samples_get_sample_by_name(self):
        tst1 = content.Samples(root_path)
        s2 = tst1.get_sample_by_name('FAKE_WILL_FAIL')
        self.assertEqual(s2, None)
        
        s3 = tst1.get_sample_by_name('finance_transaction')
        self.assertEqual(len(str(s3)) > 50, True)
        
        
    def test_16_samples_list(self):
        tst1 = content.Samples(root_path)
        full_list = tst1.list()
        #print('full_list = ', full_list)
        self.assertEqual(len(full_list) > 1, True)

    def test_17_data_building(self):
        s = content.DataFiles()
        fname = content.data_fldr + os.sep + 'building' + os.sep + 'tools.csv'
        tool_list = s.get_collist_by_name(fname, 'name')
        self.assertTrue(len(tool_list[0]) > 10)
        self.assertTrue('welder' in tool_list[0])
        self.assertFalse('purple' in tool_list[0])
        
        tool_types = s.get_collist_by_name(fname, 'type')
        self.assertEqual(set(tool_types[0]),{'measuring', 'cutting', 'fastening', 'chemical', 'shaping', 'simple', 'moving'})

    def test_18_get_list_columns(self):
        s = content.DataFiles()
        cols_world = s.get_list_columns('world')
        print('cols_world = ', cols_world)
        self.assertTrue('world.country.CountryCode' in cols_world)
        self.assertTrue('world.country.Latest agricultural census' in cols_world)
        
        cols_building = s.get_list_columns('building')
        self.assertTrue('building.tools.name' in cols_building)
        self.assertTrue('building.materials_specific_strength.Tensile strength_Mpa' in cols_building)
        self.assertTrue('building.actions.cost_time' in cols_building)
        
        cols_multiple = s.get_list_columns('material')
        self.assertTrue('games.materials.drop_rate' in cols_multiple)
        self.assertTrue('building.materials_specific_strength.Material_name' in cols_multiple)
        
        cols_multiple2 = s.get_list_columns('desc')
        self.assertTrue('.countries.country_desc' in cols_multiple2)
        self.assertTrue('games.materials.description' in cols_multiple2)
        self.assertTrue('games.monsters.desc' in cols_multiple2)
        self.assertTrue('games.skills.description' in cols_multiple2)
        self.assertTrue('food.food_desc.NDB_No' in cols_multiple2)
        
   
    def test_20_samples_person_consumer(self):
        tst20 = content.Samples(root_path)
        s20 = tst20.get_sample_by_name('person_consumer')
        self.assertEqual(len(str(s20)) > 50, True)
        self.assertEqual(len(s20.lists), 4)
        self.assertEqual(s20.lists[0], {'date_range':[2015, 2017]})
        
        self.assertEqual(s20.lists[1], {'amount_range':[2.50, 123.30]})
        self.assertEqual(s20.lists[2], {'spending_type':['saves','spends']})
        
        self.assertEqual(len(s20.cols), 4)
        self.assertEqual(s20.cols[0], 'Name, NAME, !random!')
        self.assertEqual(s20.cols[1], 'Spend_type,WORD,spending_type')
        self.assertEqual(s20.cols[2], 'Fav_hobby, WORD, !random!')
        self.assertEqual(s20.cols[3], 'Location, PLACE, !random!')
        


        
    def test_21_random_person(self):
        tst21 = content.Samples(root_path)
        import random
        import pprint
        s21 = tst21.get_sample_by_name('person_consumer')
        person = {}
        for l in s21.lists:
            for k,v in l.items():
                person[k] = random.choice(v)
        
        pprint.pprint(person)
        
    
    
if __name__ == '__main__':
    unittest.main()
        
        
        
        