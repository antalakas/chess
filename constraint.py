# -*- coding: utf-8 -*-

"""
`constraint` module is responsible for providing a basic
interface for playing the chess constraint game.
"""

# ///////////////////////////////////////////////////
# ---------------------------------------------------
# File: constraint.py
# Author: Andreas Ntalakas <antalakas>
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# Python packages
import time
from recordtype import recordtype
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# My modules
from settings import king_type
from settings import queen_type
from settings import bishop_type
from settings import rook_type
from settings import knight_type
from settings import number_of_types
from settings import symbols
# ---------------------------------------------------

# ///////////////////////////////////////////////////


class Constraint(object):
    """
    `Constraint()` class is responsible for providing a basic interface for
    playing the chess constraint game.
    """

    # ///////////////////////////////////////////////////
    def __init__(self, params):
        """
        `__init__()` initializes the necessary objects for using the
        Constraint.

        Attributes:
        `height`                         --     Board heigh.
        `widt`                           --    Board width.
        `count`         int              --     Number of solutions found.
        `board`         []position       --     List of currently allocated pieces.
        `board_index`   int              --     Index in the list of allocated pieces.
        `pieces`        []int            --     List of given pieces to allocate.
        `last_xy`       [][]coordinate   --     List of last used position
                                         --     per every type of piece.
        `last_index`    []int            --     Index in the list of last positions.
        `used_cols`     []int            --     Attacked columns.
        `used_rows`     []int            --     Attacked rows.
        `used_diag_l`   []int            --     Attacked diagonals (left)
        `used_diag_r`   []int            --     Attacked diagonals (right)
        `used_cells`    []int            --     Map of cells "under attack".
        `king_rules`    [8]coordinate    --     Permitted moves for king
        `knight_rules`  [8]coordinate    --     Permitted moves for knight
        """
        position = recordtype("position", ["x", "y", "kind"])
        coordinate = recordtype("coordinate", ["x", "y"])

        self.width = params["m"]
        self.height = params["n"]
        self.count = 0
        self.pieces = params["pieces"]

        self.board = []
        for _ in self.pieces:
            self.board.append(position(0, 0, 0))

        self.board_index = 0
        self.last_xy = []
        self.last_index = [0] * number_of_types

        for _ in range(number_of_types):
            coord_list = []
            for _ in range(len(self.pieces) + 1):
                coord_list.append(coordinate(0, 0))
            self.last_xy.append(coord_list)

        self.attacked_cols = [0] * self.width
        self.attacked_rows = [0] * self.height
        self.attacked_diag_l = [0] * (self.width + self.height)
        self.attacked_diag_r = [0] * (self.width + self.height)
        self.attacked_cells = [0] * ((self.width+4) * (self.height+4))

        self.king_rules = [
            coordinate(-1, 0), coordinate(1, 0), coordinate(0, -1), coordinate(0, 1),
            coordinate(-1, -1), coordinate(1, 1), coordinate(1, -1), coordinate(-1, 1)
        ]

        self.knight_rules = [
            coordinate(-2, -1), coordinate(-2, 1), coordinate(2, -1), coordinate(2, 1),
            coordinate(-1, -2), coordinate(-1, 2), coordinate(1, -2), coordinate(1, 2)
        ]

    def print_board(self):
        """prints board"""
        board_print = ['.'] * self.width * self.height

        for j in range(self.board_index):
            current_board = self.board[j]
            board_print[current_board.y * self.width + current_board.x] = \
                symbols[current_board.kind]

        print board_print

    def is_attacking(self, y_dim, x_dim, kind):
        """
        checks whether the piece is attacking other
        units from this position
        """
        i = 0
        while i < self.board_index:
            c_y = self.board[i].y
            c_x = self.board[i].x

            if kind == queen_type or kind == rook_type:
                if c_y == y_dim or c_x == x_dim:
                    return True

            if kind == queen_type or kind == bishop_type:
                if ((c_y + c_x) == (y_dim + x_dim)) or ((c_y - c_x) == (y_dim - x_dim)):
                    return True

            if (kind == king_type) or (kind == knight_type):
                delta = self.king_rules
                if kind == knight_type:
                    delta = self.knight_rules
                for item in delta:
                    if (c_y == (y_dim + item.y)) and (c_x == (x_dim + item.x)):
                        return True
            i += 1

        return False

    def place_piece(self, y_dim, x_dim, kind, direction):
        """marks the board when we are placing next piece"""
        # Mark rows and columns.
        if (kind == rook_type) or (kind == queen_type):
            self.attacked_rows[y_dim] += direction
            self.attacked_cols[x_dim] += direction

        # Mark diagonals.
        if (kind == queen_type) or (kind == bishop_type):
            self.attacked_diag_l[y_dim + x_dim] += direction
            self.attacked_diag_r[y_dim - x_dim + self.width] += direction

        # Mark King's and Knight's attacks.
        if (kind == king_type) or (kind == knight_type):
            delta = self.king_rules
            if kind == knight_type:
                delta = self.knight_rules
            for item in delta:
                # print "kind: " + str(kind)
                myindex = (y_dim + item.y + 2) * (self.width + 4) + (x_dim + item.x + 2)
                # print "index to place: " + str(myindex)
                self.attacked_cells[myindex] += direction

        # Mark the cell itself.
        self.attacked_cells[(y_dim + 2) * (self.width + 4) + (x_dim + 2)] += direction

        # Put a piece to the list of already placed units.
        if direction == 1:
            self.board[self.board_index].y = y_dim
            self.board[self.board_index].x = x_dim
            self.board[self.board_index].kind = kind

        self.board_index += direction

        # Save this position as the last used for this type of pieces.
        self.last_index[kind] += direction
        if direction == 1:
            self.last_xy[kind][self.last_index[kind]].y = y_dim
            self.last_xy[kind][self.last_index[kind]].x = x_dim

    def search(self, piece_number):
        """recursive function implementing depth-first search"""
        # Recursive search function.
        if piece_number == len(self.pieces):
            # Found!
            self.count += 1
            if self.height <= 4 and self.width <= 4:
                self.print_board()
            return

        kind = self.pieces[piece_number]

        # Load the last used position for this type of pieces to avoid generating
        # duplicated positions.
        last_index = self.last_index[kind]
        f_y = self.last_xy[kind][last_index].y
        f_x = self.last_xy[kind][last_index].x

        j = f_y
        while j < self.height:
            # Skip if row is occupied.
            if self.attacked_rows[j] == 0:
                i = f_x
                while i < self.width:
                    # Skip if cell is occupied.
                    if self.attacked_cells[(j + 2) * (self.width + 4) + (i + 2)] > 0:
                        i += 1
                        continue

                    # Skip if column is occupied.
                    if self.attacked_cols[i] > 0:
                        i += 1
                        continue

                    # Skip if diagonals are occupied.
                    if (self.attacked_diag_l[j + i] > 0) or \
                            (self.attacked_diag_r[j - i + self.width] > 0):
                        i += 1
                        continue

                    # Skip if the current piece attacks already placed units.
                    if self.is_attacking(j, i, kind):
                        i += 1
                        continue

                    # Mark the board.
                    self.place_piece(j, i, kind, 1)

                    self.search(piece_number + 1)

                    # Un-mark the board.
                    self.place_piece(j, i, kind, -1)
                    i += 1
            j += 1
            f_x = 0

    # ///////////////////////////////////////////////////
    def play(self):
        """
        `play()` is a public method of class Constraint.
        It is used to play the constraint game.
        """
        start = time.time()
        self.search(0)
        end = time.time()

        print "number of solutions: " + str(self.count) + "\n"
        print "calculation time (sec): " + str(end - start)
