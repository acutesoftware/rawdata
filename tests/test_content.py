# test_content.py

import os
import unittest
import rawdata.generate
import rawdata.content

class TestContent(unittest.TestCase):
    def test_01_check_sample_datafiles(self):
        s = rawdata.content.Samples()
        all_files = s.get_list()
        print(len(all_files))
        self.assertEqual(len(all_files),12)  # check for 11 data files
        
        #for f in all_files:
            #print(f[2])
        self.assertEqual(all_files[0][2],'countries.csv')
        self.assertEqual(all_files[1][2],'finance_categories.txt')
        self.assertEqual(all_files[2][2],'names.csv')

    def test_02_get_collist(self):
        s = rawdata.content.Samples()
        data_file = rawdata.content.data_fldr + os.sep + 'games' + os.sep + 'skills.csv'
        col1 = s.get_collist_by_name(data_file, 'type' )
        self.assertEqual(col1, [{'buff', 'change', 'build', 'type', 'info', 'gather', 'attack', 'heal'}])
        
    def test_03_read_list(self):
        s = rawdata.content.Samples()
        fname = rawdata.content.data_fldr + os.sep + 'food' + os.sep + 'food_desc.csv'
        food_list = s.get_collist_by_name(fname, 'Long_Desc')
        #print(food_list[0])
        self.assertEqual(len(food_list[0]), 1114)
        for f in food_list[0]:
            #print(f)
            pass
        #self.assertEqual(food_list[0], 'Cheese')
        
    
if __name__ == '__main__':
    unittest.main()
