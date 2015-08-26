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
from itertools import product
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
        # self.kings = params["k"]
        # self.queens = params["q"]
        # self.rooks = params["r"]
        # self.bishops = params["b"]
        # self.knights = params["kn"]
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
    def king_attacks(self, x_coord, y_coord):
        """
            for given coordinates,calculates king's attack
            sparse bitboard, where biboard[index] = 1
            denotes an index (coordinate) under attack
        """
        bit_board = self.create_bit_board()
        moves = list(product([x_coord-1, x_coord+1], [y_coord-1, y_coord+1])) + \
                list(product([x_coord], [y_coord-1, y_coord+1])) + \
                list(product([x_coord-1, x_coord+1], [y_coord]))
        moves = [(x_coord, y_coord) for x_coord, y_coord in moves
                 if x_coord >= 0 and y_coord >= 0 and x_coord < self.rows and y_coord < self.cols]
        for pos in moves:
            index = self.coords_to_index(pos)
            bit_board[index] = 1

        return bit_board

    # ///////////////////////////////////////////////////
    def knight_attacks(self, x_coord, y_coord):
        """
            for given coordinates,calculates knight's attack
            sparse bitboard, where biboard[index] = 1
            denotes an index (coordinate) under attack
        """
        bit_board = self.create_bit_board()
        moves = list(product([x_coord-1, x_coord+1], [y_coord-2, y_coord+2])) + \
                list(product([x_coord-2, x_coord+2], [y_coord-1, y_coord+1]))
        moves = [(x_coord, y_coord) for x_coord, y_coord in moves
                 if x_coord >= 0 and y_coord >= 0 and x_coord < self.rows and y_coord < self.cols]
        for pos in moves:
            index = self.coords_to_index(pos)
            bit_board[index] = 1

        return bit_board

    # ///////////////////////////////////////////////////
    def queen_attacks(self, x_coord, y_coord):
        """
            for given coordinates,calculates queen's attack
            sparse bitboard, where biboard[index] = 1
            denotes an index (coordinate) under attack
        """
        bit_board = self.create_bit_board()

        for i in range(self.cols):
            if i != y_coord:
                bit_board[x_coord*self.cols + i] = 1
                r1 = x_coord + y_coord - i
                r2 = x_coord + i - y_coord
                if 0 <= r1 and r1 < self.rows:
                  bit_board[r1*self.cols + i] = 1
                if 0 <= r2 and r2 < self.rows:
                  bit_board[r2*self.cols + i] = 1

        for i in range(self.rows):
            if i != x_coord:
                bit_board[i*self.cols + y_coord] = 1

        return bit_board

    # ///////////////////////////////////////////////////
    def rook_attacks(self, x_coord, y_coord):
        """
            for given coordinates,calculates rook's attack
            sparse bitboard, where biboard[index] = 1
            denotes an index (coordinate) under attack
        """
        bit_board = self.create_bit_board()

        for i in range(self.cols):
            if i != y_coord:
                bit_board[x_coord*self.cols + i] = 1

        for i in range(self.rows):
            if i != x_coord:
                bit_board[i*self.cols + y_coord] = 1

        return bit_board

    # ///////////////////////////////////////////////////
    def bishop_attacks(self, x_coord, y_coord):
        """
            for given coordinates,calculates bishop's attack
            sparse bitboard, where biboard[index] = 1
            denotes an index (coordinate) under attack
        """
        bit_board = self.create_bit_board()

        for i in range(self.cols):
            if i != y_coord:
                r1 = x_coord + y_coord - i
                r2 = x_coord + i - y_coord
                if 0 <= r1 and r1 < self.rows:
                    bit_board[r1*self.cols + i] = 1
                if 0 <= r2 and r2 < self.rows:
                    bit_board[r2*self.cols + i] = 1

        return bit_board

    # ///////////////////////////////////////////////////
    def play(self):
        """
            `play()` is a public method of class Independence.
            It is used to play the independence game.
        """
        print self.knight_attacks(0, 0)
