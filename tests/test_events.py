#!/usr/bin/python3
# test_events.py

import unittest
import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__),  '..', 'rawdata'))
test_fldr = os.path.dirname(__file__) + os.sep + 'test_results'
sys.path.insert(1, root_fldr)
import events

sample_dict = {'name' :'test_dict_by_weekday', 'scale':'day_of_week', 
               'trend':{'Mon':0.5, 'Tue':0.5, 'Wed':0.1, 'Thu':0.1, 'Fri':0.5}}

sample_data = [['2011-11-11', 20], ['2012-02-22', 50]]

class TestEvent(unittest.TestCase):
    def test_01_create_event(self):
        t = events.TrendGenerator(sample_dict)
        #print(t)
        self.assertEqual(str(t)[0:28], 'name  = test_dict_by_weekday')
        
    def test_02_time_series(self):
        t = events.TrendGenerator(sample_dict)
        
        # orig data sample
        self.assertEqual(sample_data[0],['2011-11-11', 20])  
        self.assertEqual(sample_data[1],['2012-02-22', 50]) 

        BEFORE = str(sample_data)
        t.create_time_series(sample_data, 0, 1) 
        AFTER = str(sample_data)
        self.assertEqual(BEFORE == AFTER, False)
        
        # checked modified data
        self.assertEqual(sample_data[0],['2011-11-11', 22.0])
        self.assertEqual(sample_data[1],['2012-02-22', 55.00000000000001])

    def test_03_int_keys(self):
        int_key_dict = {'name' :'test3', 'scale':'day_of_week', 
               'trend':{1:0.5, 2:0.5, 3:0.1, 4:0.1, 5:0.5}}
        t3 = events.TrendGenerator(int_key_dict)
        #print(t3)
        self.assertEqual('trend = 1=0.5, 2=0.5, 3=0.1, 4=0.1, 5=0.5,' in str(t3), True) 
        
    def test_04_str_values(self):
        str_val_dict = {'name' :'test3', 'scale':'day_of_week', 
               'trend':{1:'0.5', 2:'0.5', 3:'0.1', 4:'0.1', 5:'0.5'}}
        t4 = events.TrendGenerator(str_val_dict)
        #print(t4)
        self.assertEqual('trend = 1=0.5, 2=0.5, 3=0.1, 4=0.1, 5=0.5,' in str(t4), True)
        
#if __name__ == '__main__':
#    unittest.main()
print('to run locally - import test_errors; unittest.main();')