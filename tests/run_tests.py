# run_tests.py

import unittest as unittest
 
if __name__ == "__main__":
    """
    T:\\user\\dev\\src\\python\\rawdata\\tests>run_tests.py
    11
    ............
    ----------------------------------------------------------------------
    Ran 12 tests in 0.211s

    OK
    """
    all_tests = unittest.TestLoader().discover('.', pattern='test*.py')
    unittest.TextTestRunner().run(all_tests)  
    