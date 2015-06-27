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

        _ = t.create_time_series(sample_data, 0, 1) 
 
        # checked modified data
        self.assertEqual(sample_data[0],['2011-11-11', 22.0])
        self.assertEqual(sample_data[1],['2012-02-22', 55.00000000000001])

if __name__ == '__main__':
    unittest.main()
