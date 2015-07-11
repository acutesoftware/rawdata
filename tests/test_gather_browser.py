#!/usr/bin/python3
# test_gather_browser.py

import unittest
import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__),  '..', 'rawdata'))
imp_folder = root_fldr + os.sep + 'gather'
print(imp_folder)
sys.path.insert(1, imp_folder)
import browser_usage


class TestGatherBrowser(unittest.TestCase):
    def test_01_browser(self):
        browser = browser_usage.Browser(browser_usage.browser_data_path, browser_usage.op_folder, 'Chrome')
        browser.get_passwords()
        browser.get_browser_history_chrome()
        browser.get_browser_bookmarks_chrome()
        print(browser)
        
        bookmarks_file = browser_usage.op_folder + os.sep + 'chrome_bookmarks.csv'
        history_file = browser_usage.op_folder + os.sep + 'chrome_history.csv'
        password_op = browser_usage.op_folder + os.sep + 'PASSWORDS.csv' 
        
        self.assertEqual(os.path.exists(bookmarks_file), True)
        self.assertEqual(os.path.exists(history_file), True)
        self.assertEqual(os.path.exists(password_op), True)
 

if __name__ == '__main__':
    unittest.main()
