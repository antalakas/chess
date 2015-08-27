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
    the problem. The order of placement will be based on the
    number of attacks a piece can provide in descending order,
    which means Queen (q) -> Rook (r) -> Bishop (b) -> King (k)
    -> Knight (n).

    If the last piece has been placed, the solution is noted. If
    fewer pieces than the total number of pieces have been placed,
    then this is a dead end.  In either case, backtracking occurs.
    The last piece placed on the board gets pulled, then it gets
    moved to the next safe square. Backtrack occurs even after a
    "good" attempt in order to get to a new solution. Backtracking
    may repeat itself several times until the original misplaced
    piece finally is proven to be a dead end.

    The "attack graph" for each piece is precomputed up front,
    and then we essentially ignore the geometry of the problem.
    The "attack graph" is presented as a bit board, a one
    dimensional array transformation of the rectangular board
    (according to the problem). Coordinate (0, 0) represents
    the lower-left board square.
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
import math
import time
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
                * `self.rows`           : number of board's rows
                * `self.cols`           : number of board's columns
                * `self.num_queens`     : number of queens
                * `self.under_attack`   : dictionary of attack bit boards for a queen placed on
                                          every square on a given board
                * `self.queens`         : array of queen positions (in algorithm)
                * `self.board_status`   : a dictionary of board statuses that is populated every
                                          time we put a queen "on board"
                * `self.pos`            : position under examination (in algorithm)
                * `self.num_solutions`  : after algorithm convergence
                * `self.num_backtracks` : after algorithm convergence
        """

        self.rows = params["m"]
        self.cols = params["n"]
        # self.num_kings = params["k"]
        self.num_queens = params["q"]
        # self.num_rooks = params["r"]
        # self.num_bishops = params["b"]
        # self.num_knights = params["kn"]
        self.board = self.create_bit_board()
        self.chess_board_size = len(self.board)

        self.under_attack = {}
        self.queens = []
        self.board_status = {}
        self.pos = 0
        self.num_solutions = 0
        self.num_backtracks = 0

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
    def print_board(self, bit_board):
        """
            prints a bit board, taking into account
            the fact that it has to calculate rows
            and print them in reverse order
        """
        board_rows_dict = {}

        for i in range(self.rows):
            board_rows_dict[i] = [None] * self.cols
            for j in range(self.cols):
                index = self.coords_to_index((i, j))
                board_rows_dict[i][j] = bit_board[index]

        for i in reversed(range(self.rows)):
            print board_rows_dict[i]

        print '\n'

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

        index = self.coords_to_index((x_coord, y_coord))
        bit_board[index] = 1

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

        index = self.coords_to_index((x_coord, y_coord))
        bit_board[index] = 1

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
    def attack(self, position):
        """
            calculates the board state after setting a
            piece "on board"
        """
        for i in range(self.rows * self.cols):
            self.board[i] = self.board[i] or self.under_attack[position][i]
        # self.print_board(self.board)

    # ///////////////////////////////////////////////////
    def backtrack(self):
        """
            recalls a board state after removing
            a piece from the board
        """
        self.pos = self.queens.pop()
        self.board = self.board_status[self.pos]
        del self.board_status[self.pos]
        self.pos += 1
        self.num_backtracks += 1
        # self.print_board(self.board)

    # ///////////////////////////////////////////////////
    def play(self):
        """
            `play()` is a public method of class Independence.
            It is used to play the independence game.
        """

        # attacks = self.queen_attacks(4, 5)
        # self.print_board(attacks)
        #
        # attacks = self.rook_attacks(4, 5)
        # self.print_board(attacks)
        #
        # attacks = self.bishop_attacks(4, 5)
        # self.print_board(attacks)
        #
        # attacks = self.king_attacks(4, 5)
        # self.print_board(attacks)
        #
        # attacks = self.knight_attacks(4, 5)
        # self.print_board(attacks)

        start = time.time()
        # precomputation
        for i in range(self.rows * self.cols):
            row = int(math.floor(i / self.cols))
            col = i % self.cols
            self.under_attack[i] = self.queen_attacks(row, col)
            # self.print_board(self.under_attack[i])
        end = time.time()

        print "precomputation time (sec): "
        print end - start

        start = time.time()

        # Find solutions in mxn board for x queens
        while True:
            if self.pos >= self.rows * self.cols:
                if len(self.queens) == 0:
                    break
                self.backtrack()
                continue

            # If a square is empty
            if self.board[self.pos] == 0:
                self.board_status[self.pos] = list(self.board)
                self.attack(self.pos)
                self.queens.append(self.pos)
                if len(self.queens) == self.num_queens:
                    self.num_solutions += 1
                    # print self.queens
                    # print '\n'
                    # show_queens queens, n
                    self.backtrack()
            self.pos += 1

        end = time.time()

        print "calculation time (sec): "
        print end - start
        print "num of solutions: " + str(self.num_solutions)
        print "num of backtracks: " + str(self.num_backtracks)
