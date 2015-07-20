# run_tests.py

# T:\\user\\dev\\src\\python\\rawdata\\tests>run_tests.py
# 11
# ............
# ----------------------------------------------------------------------
# Ran 12 tests in 0.211s
# OK

import unittest as unittest

all_tests = unittest.TestLoader().discover('.', pattern='test*.py')
unittest.TextTestRunner().run(all_tests)  
