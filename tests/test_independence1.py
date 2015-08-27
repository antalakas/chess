# -*- coding: utf-8 -*-

"""
    `test_independence1` module is responsible for setting up
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


class TestIndependence1(unittest.TestCase):
    """
        `TestIndependence1()` class is unit-testing the class
        Independence().
    """

    # ///////////////////////////////////////////////////
    def setUp(self):
        params = {}
        params["m"] = 8
        params["n"] = 8
        params["q"] = 8
        params["r"] = 0
        params["b"] = 0
        params["k"] = 0
        params["kn"] = 0
        self.game = Independence(params)

    # ///////////////////////////////////////////////////
    @classmethod
    def compare_bit_boards(cls, first, second):
        """
            Compares two bit boards (arrays)
        """
        return first == second

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
        attacks = self.game.king_attacks(0, 0)
        bit_board = [1, 1, 0, 0, 0, 0, 0, 0,
                     1, 1, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.compare_bit_boards(attacks, bit_board), True)

    # ///////////////////////////////////////////////////
    def knight_attacks(self):
        """
            Checks knight attacks
        """
        attacks = self.game.knight_attacks(0, 0)
        bit_board = [1, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 1, 0, 0, 0, 0, 0,
                     0, 1, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.compare_bit_boards(attacks, bit_board), True)

    # ///////////////////////////////////////////////////
    def queen_attacks(self):
        """
            Checks queen attacks
        """
        attacks = self.game.queen_attacks(0, 3)
        bit_board = [1, 1, 1, 1, 1, 1, 1, 1,
                     0, 0, 1, 1, 1, 0, 0, 0,
                     0, 1, 0, 1, 0, 1, 0, 0,
                     1, 0, 0, 1, 0, 0, 1, 0,
                     0, 0, 0, 1, 0, 0, 0, 1,
                     0, 0, 0, 1, 0, 0, 0, 0,
                     0, 0, 0, 1, 0, 0, 0, 0,
                     0, 0, 0, 1, 0, 0, 0, 0]
        self.assertEqual(self.compare_bit_boards(attacks, bit_board), True)

    # ///////////////////////////////////////////////////
    def rook_attacks(self):
        """
            Checks rook attacks
        """
        attacks = self.game.rook_attacks(3, 7)
        bit_board = [0, 0, 0, 0, 0, 0, 0, 1,
                     0, 0, 0, 0, 0, 0, 0, 1,
                     0, 0, 0, 0, 0, 0, 0, 1,
                     1, 1, 1, 1, 1, 1, 1, 1,
                     0, 0, 0, 0, 0, 0, 0, 1,
                     0, 0, 0, 0, 0, 0, 0, 1,
                     0, 0, 0, 0, 0, 0, 0, 1,
                     0, 0, 0, 0, 0, 0, 0, 1]
        self.assertEqual(self.compare_bit_boards(attacks, bit_board), True)

    # ///////////////////////////////////////////////////
    def bishop_attacks(self):
        """
            Checks bishop attacks
        """
        attacks = self.game.bishop_attacks(0, 3)
        bit_board = [0, 0, 0, 1, 0, 0, 0, 0,
                     0, 0, 1, 0, 1, 0, 0, 0,
                     0, 1, 0, 0, 0, 1, 0, 0,
                     1, 0, 0, 0, 0, 0, 1, 0,
                     0, 0, 0, 0, 0, 0, 0, 1,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.compare_bit_boards(attacks, bit_board), True)

    # ///////////////////////////////////////////////////
    def eight_queens(self):
        """
            8 queens
        """
        self.game.play()
        self.assertEqual(self.game.num_solutions == 92, True)
