#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_config.py

import unittest
import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep + 'rawdata'
test_fldr = os.path.dirname(__file__) + os.sep + 'test_results'
sys.path.insert(1, root_fldr)

import config


class TestConfig(unittest.TestCase):
    def test_01_config(self):
        self.assertEqual(config.params['rawdata_version'] >= '0.0.9', True) 

    def test_02_fldrs(self):
        self.assertEqual(len(config.fldrs) > 6, True)
        
   
if __name__ == '__main__':
    unittest.main()
