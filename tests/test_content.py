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
        self.assertEqual(len(all_files),11)  # check for 11 data files
        
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
        
    
if __name__ == '__main__':
    unittest.main()
