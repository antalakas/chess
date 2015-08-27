# -*- coding: utf-8 -*-

"""
    `test_independence3` module is responsible for setting up
    and running tests related to Independence module
"""

# ///////////////////////////////////////////////////
# ---------------------------------------------------
# File: test_mailer.py
# Author: Andreas Ntalakas <antalakas>
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# independence modules
# ---------------------------------------------------
from chess import Independence
# ---------------------------------------------------

import unittest

# ///////////////////////////////////////////////////


class TestIndependence3(unittest.TestCase):
    """
        `TestIndependence3()` class is unit-testing the class
        Independence().
    """

    # ///////////////////////////////////////////////////
    def setUp(self):
        params = {}
        params["m"] = 4
        params["n"] = 4
        params["q"] = 0
        params["r"] = 2
        params["b"] = 0
        params["k"] = 0
        params["kn"] = 4
        self.game = Independence(params)

    # ///////////////////////////////////////////////////
    def two_r_4_kn(self):
        """
            two rooks, four knights
        """
        self.game.play()
        self.assertEqual(self.game.num_solutions == 8, True)
