# -*- coding: utf-8 -*-

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


class TestIndependence(unittest.TestCase):
    """
        `TestIndependence()` class is unit-testing the class
        Independence().
    """
    
    # ///////////////////////////////////////////////////
    def setUp(self):
        params = {}
        params["m"] = 8
        params["n"] = 8
        params["q"] = 8
        self.game = Independence(params)

    # ///////////////////////////////////////////////////
    # Tests x dimension exists and is valid
    def x_dim_is_valid(self):
        self.assertEqual(self.game.params["m"] > 0, True)

    # ///////////////////////////////////////////////////
    # Tests y dimension exists and is valid
    def y_dim_is_valid(self):
        self.assertEqual(self.game.params["n"] > 0, True)
