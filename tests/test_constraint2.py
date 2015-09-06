# -*- coding: utf-8 -*-

"""
    `test_constraint` module is responsible for setting up
    and running tests related to Constraint module
"""

# ///////////////////////////////////////////////////
# ---------------------------------------------------
# File: test_constraint.py
# Author: Andreas Ntalakas <antalakas>
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# constraint modules
# ---------------------------------------------------
from chess import Constraint
# ---------------------------------------------------

import unittest

# ///////////////////////////////////////////////////


class TestConstraint2(unittest.TestCase):
    """
    `TestConstraint2()` class is unit-testing the class
    Constraint().
    """

    # ///////////////////////////////////////////////////
    def setUp(self):
        params = {}
        params["m"] = 4
        params["n"] = 4
        params["pieces"] = [3, 3, 4, 4, 4, 4]
        self.game = Constraint(params)

    # ///////////////////////////////////////////////////
    def solve(self):
        """Tests validity of solution"""
        self.game.search(0)
        self.assertEqual(self.game.count == 8, True)