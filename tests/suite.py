# -*- coding: utf-8 -*-

# ///////////////////////////////////////////////////
# ---------------------------------------------------
# File: suite.py
# Author: Andreas Ntalakas <antalakas>
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# Python
# ---------------------------------------------------
# ---------------------------------------------------

import unittest

# ///////////////////////////////////////////////////
# independence Tests
# ---------------------------------------------------
from test_independence import TestIndependence
# ---------------------------------------------------

# ///////////////////////////////////////////////////


def test_suite():
    """
        `test_suite()` method creates a test suite 
        for the unit-tests of independence package.
    """
 
    all_tests = unittest.TestSuite()
    
    # Adding TestIndependence tests
    all_tests.addTest(TestIndependence('x_dim_is_valid'))
    all_tests.addTest(TestIndependence('y_dim_is_valid'))

    return all_tests
