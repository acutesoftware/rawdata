# run_tests.py

# T:\\user\\dev\\src\\python\\rawdata\\tests>run_tests.py
# 11
# ............
# ----------------------------------------------------------------------
# Ran 12 tests in 0.211s
# OK

import os
import time
import unittest as unittest

all_tests = unittest.TestLoader().discover('.', pattern='test*.py')
unittest.TextTestRunner().run(all_tests)  




# Cleanup Files

def wipe_file(fname):
    if os.path.exists(fname):
        os.remove(fname)
        print('deleted ' + fname)
    

print ('WIPING ALL TEST RESULTS - PRESS CTRL C TO STOP')

time.sleep(5)
wipe_file('random_table.csv')

