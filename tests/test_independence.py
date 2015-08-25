# -*- coding: utf-8 -*-

"""
    `test_independence` module is responsible for setting up
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
    def x_dim_is_valid(self):
        """
            Tests x dimension exists and is valid
        """
        self.assertEqual(self.game.params["m"] > 0, True)

    # ///////////////////////////////////////////////////
    def y_dim_is_valid(self):
        """
            Tests y dimension exists and is valid
        """
        self.assertEqual(self.game.params["n"] > 0, True)

    # ///////////////////////////////////////////////////
    def chess_board_is_valid(self):
        """
            Tests chess board creation
        """
        self.assertEqual(self.game.chess_board_size == 64, True)

    # ///////////////////////////////////////////////////
    def check_coord_tranformations(self):
        """
            Checks coordinate transformation
        """
        self.assertEqual(self.game.coords_to_index((5, 5)) == 45, True)
