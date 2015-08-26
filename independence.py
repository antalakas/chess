# -*- coding: utf-8 -*-

"""
    `independence` module is responsible for providing a basic
    interface for playing the chess independence game.

    The problem
    -----------
    Find all unique configurations of a set of normal chess
    pieces on a chess board with dimensions M×N where none of
    the pieces is in a position to take any of the others.
    Assume the colour of the piece does not matter, and that
    there are no pawns among the pieces.

    Write a program which takes as input:
    The dimensions of the board: M, N
    The number of pieces of each type (King, Queen, Bishop,
    Rook and Knight) to try and place on the board.
    As output, the program should list all the unique
    configurations to the console for which all of the pieces
    can be placed on the board without threatening each other.
    -------------------------------------------------------------

    Solution path
    -------------
    The algorithm, keeps placing pieces on the board until there
    is no longer a safe square, modelling the human reaction to
    the problem.

    If the last piece has been placed, the solution is noted. If
    fewer pieces than the total number of pieces have been placed,
    then this is a dead end.  In either case, backtracking occurs.
    The last piece placed on the board gets pulled, then it gets
    moved to the next safe square. Backtrack occurs even after a
    "good" attempt in order to get to a new solution. Backtracking
    may repeat itself several times until the original misplaced
    piece finally is proven to be a dead end.

    The "attack graph"  for each piece is precomputed up front,
    and then we essentially ignore the geometry of the problem.
    -------------------------------------------------------------
"""

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
                r_1 = x_coord + y_coord - i
                r_2 = x_coord + i - y_coord
                if 0 <= r_1 and r_1 < self.rows:
                    bit_board[r_1*self.cols + i] = 1
                if 0 <= r_2 and r_2 < self.rows:
                    bit_board[r_2*self.cols + i] = 1

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
                r_1 = x_coord + y_coord - i
                r_2 = x_coord + i - y_coord
                if 0 <= r_1 and r_1 < self.rows:
                    bit_board[r_1*self.cols + i] = 1
                if 0 <= r_2 and r_2 < self.rows:
                    bit_board[r_2*self.cols + i] = 1

        return bit_board

    # ///////////////////////////////////////////////////
    def play(self):
        """
            `play()` is a public method of class Independence.
            It is used to play the independence game.
        """
        print self.knight_attacks(0, 0)
