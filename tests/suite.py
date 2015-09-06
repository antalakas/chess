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
from .test_constraint1 import TestConstraint1
from .test_constraint2 import TestConstraint2
from .test_constraint3 import TestConstraint3
# ---------------------------------------------------

# ///////////////////////////////////////////////////


def test_suite():
    """
    `test_suite()` method creates a test suite
    for the unit-tests of independence package.
    """

    all_tests = unittest.TestSuite()

    # Adding TestIndependence tests
    all_tests.addTest(TestConstraint1('solve'))
    all_tests.addTest(TestConstraint2('solve'))
    all_tests.addTest(TestConstraint3('solve'))

    return all_tests
