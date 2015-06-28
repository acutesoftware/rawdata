#!/usr/bin/python3
# test_samples.py

import unittest
import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
test_fldr = os.path.dirname(__file__) + os.sep + 'test_results'
sys.path.insert(1, root_fldr)

import rawdata.generate
import rawdata.content

class TestSamples(unittest.TestCase):
    def test_01_check_sample_datafiles(self):
        s = rawdata.content.Samples()
        all_files = s.get_list()
        self.assertEqual(len(all_files) > 12, True)  # check for at least 12 data files

if __name__ == '__main__':
    unittest.main()
