# -*- coding: utf-8 -*-

"""
    `suite` module collects all tests and adds them
    to the test suite
"""

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
from .test_independence1 import TestIndependence1
from .test_independence2 import TestIndependence2
from .test_independence3 import TestIndependence3
# ---------------------------------------------------

# ///////////////////////////////////////////////////


def test_suite():
    """
        `test_suite()` method creates a test suite
        for the unit-tests of independence package.
    """

    all_tests = unittest.TestSuite()

    # Adding TestIndependence tests
    all_tests.addTest(TestIndependence1('x_dim_is_valid'))
    all_tests.addTest(TestIndependence1('y_dim_is_valid'))
    all_tests.addTest(TestIndependence1('board_is_valid'))
    all_tests.addTest(TestIndependence1('coord_tranformations'))
    all_tests.addTest(TestIndependence1('king_attacks'))
    all_tests.addTest(TestIndependence1('knight_attacks'))
    all_tests.addTest(TestIndependence1('queen_attacks'))
    all_tests.addTest(TestIndependence1('rook_attacks'))
    all_tests.addTest(TestIndependence1('bishop_attacks'))
    all_tests.addTest(TestIndependence1('eight_queens'))
    all_tests.addTest(TestIndependence2('one_r_2_k'))
    all_tests.addTest(TestIndependence3('two_r_4_kn'))

    return all_tests
