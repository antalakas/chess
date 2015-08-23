#!/usr/bin/env python

# -*- coding: utf-8 -*-

# ///////////////////////////////////////////////////////////
# -----------------------------------------------------------
# File: run_tests.py
# Author: Andreas Ntalakas  <antalakas>
# -----------------------------------------------------------

# ///////////////////////////////////////////////////
# Python packages
# ---------------------------------------------------
import unittest
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# independence - Import Test Suite
from tests.suite import test_suite

# ///////////////////////////////////////////////////
# Execute 
if __name__ == "__main__":
    
    try:
        unittest.TextTestRunner(verbosity=2).run(test_suite())
    except KeyboardInterrupt:
        print "\n"
