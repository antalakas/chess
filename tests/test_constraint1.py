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


class TestConstraint1(unittest.TestCase):
    """
        `TestConstraint1()` class is unit-testing the class
        Constraint().
    """

    # ///////////////////////////////////////////////////
    def setUp(self):
        params = {}
        params["m"] = 3
        params["n"] = 3
        params["pieces"] = [0, 0, 3]
        self.game = Constraint(params)

    # ///////////////////////////////////////////////////
    def solve(self):
        """
            Tests x dimension exists and is valid
        """
        self.game.search(0)
        self.assertEqual(self.game.count == 4, True)