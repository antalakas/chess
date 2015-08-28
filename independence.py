# -*- coding: utf-8 -*-

"""
    `independence` module is responsible for providing a basic
    interface for playing the chess independence game.
"""

# ///////////////////////////////////////////////////
# ---------------------------------------------------
# File: independence.py
# Author: Andreas Ntalakas <antalakas>
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# Python packages
from itertools import product
from itertools import permutations
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
                * `self.num_of_pieces`  : number of pieces
                * `self.under_attack`   : dictionary of attack bit boards for a queen placed on
                                          every square on a given board
                * `self.problem_list`   : array of pieces to be checked against each other, having
                                          order according to problem (unique input combination)
                                          description
                * `self.solution_list`  : array of pieces' positions (evolving in algorithm)
                * `self.board_status`   : a dictionary of board statuses that is populated every
                                          time we put a queen "on board"
                * `self.pos`            : position under examination (in algorithm)
                * `self.num_solutions`  : after algorithm convergence
                * `self.num_backtracks` : after algorithm convergence
        """

        self.rows = params["m"]
        self.cols = params["n"]

        self.board = self.create_bit_board()
        self.chess_board_size = len(self.board)

        self.problem_list = []
        for _ in range(params["kn"]):
            self.problem_list.append('n')
        for _ in range(params["k"]):
            self.problem_list.append('k')
        for _ in range(params["b"]):
            self.problem_list.append('b')
        for _ in range(params["r"]):
            self.problem_list.append('r')
        for _ in range(params["q"]):
            self.problem_list.append('q')

        self.num_of_pieces = len(self.problem_list)

        self.under_attack = {}

        self.num_solutions = 0
        self.num_backtracks = 0

        self.pos = 0
        self.solution_list = []
        self.board_status = {}

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
    def print_solution_board(self):
        """
            prints a solution  bit board, noting the
            placement of current piece, taking into
            account the fact that it has to calculate
            rows and print them in reverse order
        """
        board_rows_dict = {}

        for i in range(self.rows):
            board_rows_dict[i] = [None] * self.cols
            for j in range(self.cols):
                index = self.coords_to_index((i, j))
                board_rows_dict[i][j] = str(self.board[index])

        for piece in self.solution_list:
            row = int(math.floor(piece[0] / self.cols))
            col = piece[0] % self.cols
            board_rows_dict[row][col] = piece[1]

        for i in reversed(range(self.rows)):
            print board_rows_dict[i]

        print '\n'

    # ///////////////////////////////////////////////////
    def print_solution_board_with_args(self, bit_board, piece):
        """
            prints a solution  bit board, noting the
            placement of current piece, taking into
            account the fact that it has to calculate
            rows and print them in reverse order
        """
        board_rows_dict = {}

        for i in range(self.rows):
            board_rows_dict[i] = [None] * self.cols
            for j in range(self.cols):
                index = self.coords_to_index((i, j))
                board_rows_dict[i][j] = str(bit_board[index])

        row = int(math.floor(piece[0] / self.cols))
        col = piece[0] % self.cols
        board_rows_dict[row][col] = piece[1]

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

        index = self.coords_to_index((x_coord, y_coord))
        bit_board[index] = 1

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

        index = self.coords_to_index((x_coord, y_coord))
        bit_board[index] = 1

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

        index = self.coords_to_index((x_coord, y_coord))
        bit_board[index] = 1

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
    def pre_compute(self):
        """
            `pre_compute()` is a public method of class Independence.
            It is used to precompute all possible attacks for all
            possible pieces.
        """
        start = time.time()

        self.under_attack['q'] = {}
        self.under_attack['r'] = {}
        self.under_attack['b'] = {}
        self.under_attack['k'] = {}
        self.under_attack['n'] = {}
        for i in range(self.rows * self.cols):
            row = int(math.floor(i / self.cols))
            col = i % self.cols
            self.under_attack['q'][i] = self.queen_attacks(row, col)
            self.under_attack['r'][i] = self.rook_attacks(row, col)
            self.under_attack['b'][i] = self.bishop_attacks(row, col)
            self.under_attack['k'][i] = self.king_attacks(row, col)
            self.under_attack['n'][i] = self.knight_attacks(row, col)
            # self.print_solution_board_with_args(self.under_attack['n'][i], (i, 'n'))
            # self.print_board(self.under_attack['r'][i])

        end = time.time()

        print "precomputation time (sec): "
        print end - start

    # ///////////////////////////////////////////////////
    def attack(self, position):
        """
            calculates the board state after setting a
            piece "on board"
        """
        # retrieve a piece from problem specification
        piece = self.problem_list.pop()

        # check if it attacks existing pieces
        for existing_piece in self.solution_list:
            pos_ex = existing_piece[0]
            if self.under_attack[piece][position][pos_ex] == 1:
                # put piece back to pending
                self.problem_list.append(piece)
                return None

        for i in range(self.rows * self.cols):
            # calculate new board based on attacks of specific piece
            self.board[i] = self.board[i] or self.under_attack[piece][position][i]

        return piece

    # ///////////////////////////////////////////////////
    def backtrack(self):
        """
            recalls a board state after removing
            a piece from the board
        """
        (self.pos, piece) = self.solution_list.pop()
        self.problem_list.append(piece)
        self.board = self.board_status[self.pos]
        del self.board_status[self.pos]
        self.pos += 1
        self.num_backtracks += 1
        # print "backtrack"
        # self.print_solution_board()
        # self.print_board(self.board)

    # ///////////////////////////////////////////////////
    def algorithm(self):
        """
            finds solutions in mxn board for arbitrary pieces
        """
        while True:
            if self.pos >= self.rows * self.cols:
                if len(self.solution_list) == 0:
                    break
                self.backtrack()
                continue

            # If a square is empty
            if self.board[self.pos] == 0:
                # Save board status to remember in case of backtrack
                self.board_status[self.pos] = list(self.board)

                piece = self.attack(self.pos)

                if piece:
                    self.solution_list.append((self.pos, piece))
                    # self.print_solution_board()

                if len(self.solution_list) == self.num_of_pieces:
                    self.num_solutions += 1
                    # print self.solution_list
                    # print '\n'
                    # self.print_solution_board()
                    self.backtrack()
                    # print '\n'
            self.pos += 1

    # ///////////////////////////////////////////////////
    def play(self):
        """
            `play()` is a public method of class Independence.
            It is used to play the independence game.
        """
        list_of_combinations = set(permutations(self.problem_list, self.num_of_pieces))
        num_of_combinations = len(list_of_combinations)
        print "\n"

        self.pre_compute()

        start = time.time()

        print "\n"
        print "# of combinations: " + str(num_of_combinations)
        print "List of input combinations: "

        combination_index = 1
        for combination in list_of_combinations:
            print str(combination_index) + "/" + str(num_of_combinations) + ":"
            print combination

            del self.problem_list[:]

            for i in combination:
                self.problem_list.append(i)

            self.pos = 0
            self.solution_list = []
            self.board_status = {}

            self.algorithm()

            combination_index += 1

        end = time.time()

        print "\n"
        print "calculation time (sec): "
        print end - start
        print "num of solutions: " + str(self.num_solutions)
        print "num of backtracks: " + str(self.num_backtracks)
