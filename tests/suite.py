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
from .test_independence import TestIndependence
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
    all_tests.addTest(TestIndependence('board_is_valid'))
    all_tests.addTest(TestIndependence('coord_tranformations'))
    all_tests.addTest(TestIndependence('king_attacks'))
    all_tests.addTest(TestIndependence('knight_attacks'))
    all_tests.addTest(TestIndependence('queen_attacks'))
    all_tests.addTest(TestIndependence('rook_attacks'))
    all_tests.addTest(TestIndependence('bishop_attacks'))

    return all_tests
