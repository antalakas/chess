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

        self.params = params
        self.chess_board = self.create_bit_board(params["m"], params["n"])
        self.chess_board_size = len(self.chess_board)

    @classmethod
    def create_bit_board(cls, num_rows, num_cols):
        """
            creates a one-dimension representation
            of a clear mxn chess board
        """
        bit_board = [0] * num_rows * num_cols
        return bit_board

    @classmethod
    def coords_to_index(cls, coords, num_cols):
        """
            converts a set of cartesian
            coordinates to array index
        """
        return (coords[0] * num_cols) + coords[1]

    # ///////////////////////////////////////////////////
    def play(self):
        """
            `play()` is a public method of class Independence.
            It is used to play the independence game.
        """
