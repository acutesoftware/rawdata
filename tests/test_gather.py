#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_gather.py

import unittest
import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep + 'rawdata'
test_fldr = os.path.dirname(__file__) + os.sep + 'test_results'
sys.path.insert(1, root_fldr)

import gather


class TestGather(unittest.TestCase):
    def test_01_gather(self):
        self.assertEqual(len(gather.lookup_terms) > 2, True) 

 
   
if __name__ == '__main__':
    unittest.main()
