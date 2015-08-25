"""
    `independence` module is responsible for providing a basic interface for
    playing the chess independence game.
"""

# -*- coding: utf-8 -*-

# ///////////////////////////////////////////////////
# ---------------------------------------------------
# File: setter.py
# Author: Andreas Ntalakas <antalakas>
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# ---------------------------------------------------
# Module: independence.py
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# Python packages
# from itertools import product
# import math
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# My modules
# ---------------------------------------------------

# ///////////////////////////////////////////////////


class Independence(object):
    """
        `Independence()` class is responsible for providing a basic interface for
        playing the chess independence game.
    """

    # ///////////////////////////////////////////////////
    def __init__(self, params):
        """
            `__init__()` initializes the necessary objects for using the
            Independence.

            Attributes:
                * `self.params`         : A dictionary with the problem parameters.
        """

        self.rows = params["m"]
        self.cols = params["n"]
        self.kings = params["k"]
        self.queens = params["q"]
        self.rooks = params["r"]
        self.bishops = params["b"]
        self.knights = params["kn"]
        self.chess_board = self.create_bit_board()
        self.chess_board_size = len(self.chess_board)

    # ///////////////////////////////////////////////////
    def create_bit_board(self):
        """
            creates a one-dimension representation
            of a clear mxn chess board
        """
        bit_board = [0] * self.rows * self.cols
        return bit_board

    # ///////////////////////////////////////////////////
    def coords_to_index(self, coords):
        """
            converts a set of cartesian
            coordinates to array index
        """
        return (coords[0] * self.cols) + coords[1]

    # ///////////////////////////////////////////////////
    def play(self):
        """
            `play()` is a public method of class Independence.
            It is used to play the independence game.
        """
