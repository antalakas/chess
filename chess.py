#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
`chess` module collects input arguments and creates a
dictionary to be used as an input to Constraint class
"""

# ///////////////////////////////////////////////////
# ---------------------------------------------------
# File: chess.py
# Author: Andreas Ntalakas <antalakas>
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# Python packages
# ---------------------------------------------------
import argparse
import imp

# ///////////////////////////////////////////////////
# Custom modules
# ---------------------------------------------------
from constraint import Constraint
from settings import king_type
from settings import queen_type
from settings import bishop_type
from settings import rook_type
from settings import knight_type

# ///////////////////////////////////////////////////
# Checks if the required modules have been installed.
def dependencies():
    """checks for module project's dependencies"""
    try:
        imp.find_module('recordtype')
        return True
    except ImportError:
        return False


# ///////////////////////////////////////////////////
#  Chess - command line interface


def chess():
    """
    `chess` function collects input arguments and creates a
    dictionary to be used as an input to Constraint class
    """

    # ///////////////////////////////////////////////////
    parser = argparse.ArgumentParser(description="chess - A lightweight command-line interface.")

    # ///////////////////////////////////////////////////
    parser.add_argument('--m', action='store', dest='x_dim',
                        help='Board dimension in the x direction')
    parser.add_argument('--n', action='store', dest='y_dim',
                        help='Board dimension in the y direction')
    parser.add_argument('--k', action='store', dest='k_num', help='Number of kings')
    parser.add_argument('--q', action='store', dest='q_num', help='Number of queens')
    parser.add_argument('--r', action='store', dest='r_num', help='Number of rooks')
    parser.add_argument('--b', action='store', dest='b_num', help='Number of bishops')
    parser.add_argument('--kn', action='store', dest='kn_num', help='Number of knights')

    # ///////////////////////////////////////////////////
    args = parser.parse_args()

    # ///////////////////////////////////////////////////
    params = {}
    pieces = []

    if args.x_dim:
        params["m"] = int(args.x_dim)
    else:
        return False

    if args.y_dim:
        params["n"] = int(args.y_dim)
    else:
        return False

    if args.k_num:
        for _ in range(int(args.k_num)):
            pieces.append(king_type)

    if args.q_num:
        for _ in range(int(args.q_num)):
            pieces.append(queen_type)

    if args.b_num:
        for _ in range(int(args.b_num)):
            pieces.append(bishop_type)

    if args.r_num:
        for _ in range(int(args.r_num)):
            pieces.append(rook_type)

    if args.kn_num:
        for _ in range(int(args.kn_num)):
            pieces.append(knight_type)

    params["pieces"] = pieces
    return params

# ///////////////////////////////////////////////////
# Execute
if __name__ == "__main__":

    try:
        if dependencies():
            Constraint(chess()).play()
        else:
            raise Exception("Packages required: recordtype")
    except KeyboardInterrupt:
        print "\n"
