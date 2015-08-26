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
    def compare_bit_boards(self, first, second):
        if set(first) == set(second):
            return True
        else:
            return False

    # ///////////////////////////////////////////////////
    def x_dim_is_valid(self):
        """
            Tests x dimension exists and is valid
        """
        self.assertEqual(self.game.rows > 0, True)

    # ///////////////////////////////////////////////////
    def y_dim_is_valid(self):
        """
            Tests y dimension exists and is valid
        """
        self.assertEqual(self.game.cols > 0, True)

    # ///////////////////////////////////////////////////
    def board_is_valid(self):
        """
            Tests chess board creation
        """
        self.assertEqual(self.game.chess_board_size == 64, True)

    # ///////////////////////////////////////////////////
    def coord_tranformations(self):
        """
            Checks coordinate transformation
        """
        self.assertEqual(self.game.coords_to_index((5, 5)) == 45, True)

    # ///////////////////////////////////////////////////
    def king_attacks(self):
        """
            Checks knight attacks
        """
        bitboard =  [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.compare_bit_boards(self.game.king_attacks(0, 0), bitboard), True)

    # ///////////////////////////////////////////////////
    def knight_attacks(self):
        """
            Checks knight attacks
        """
        bitboard = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.compare_bit_boards(self.game.knight_attacks(0, 0), bitboard), True)


