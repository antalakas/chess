# -*- coding: utf-8 -*-

"""
    `test_independence2` module is responsible for setting up
    and running tests related to Independence module
"""

# ///////////////////////////////////////////////////
# ---------------------------------------------------
# File: test_independence2.py
# Author: Andreas Ntalakas <antalakas>
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# independence modules
# ---------------------------------------------------
from chess import Independence
# ---------------------------------------------------

import unittest

# ///////////////////////////////////////////////////


class TestIndependence2(unittest.TestCase):
    """
        `TestIndependence2()` class is unit-testing the class
        Independence().
    """

    # ///////////////////////////////////////////////////
    def setUp(self):
        params = {}
        params["m"] = 3
        params["n"] = 3
        params["q"] = 0
        params["r"] = 1
        params["b"] = 0
        params["k"] = 2
        params["kn"] = 0
        self.game = Independence(params)

    # ///////////////////////////////////////////////////
    def one_r_2_k(self):
        """
            one rook, two kings
        """
        self.game.play()
        self.assertEqual(self.game.num_solutions == 4, True)
