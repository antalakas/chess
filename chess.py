#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
    `chess` module collects input arguments and creates a
    dictionary to be used as an input to Independence class
"""

# ///////////////////////////////////////////////////
# ---------------------------------------------------
# File: setter.py
# Author: Andreas Ntalakas <antalakas>
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# Python packages
# ---------------------------------------------------
import argparse

# ///////////////////////////////////////////////////
# Custom modules
# ---------------------------------------------------
from independence import Independence

# ///////////////////////////////////////////////////
#  Chess - command line interface


def chess():
    """
        `chess` function collects input arguments and creates a
        dictionary to be used as an input to Independence class
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

    if args.x_dim:
        params["m"] = int(args.x_dim)
    else:
        return False

    if args.y_dim:
        params["n"] = int(args.y_dim)
    else:
        return False

    if args.k_num:
        params["k"] = int(args.k_num)
    else:
        params["k"] = 0

    if args.q_num:
        params["q"] = int(args.q_num)
    else:
        params["q"] = 0

    if args.r_num:
        args.params["r"] = int(args.r_num)
    else:
        params["r"] = 0

    if args.b_num:
        params["b"] = int(args.b_num)
    else:
        params["b"] = 0

    if args.kn_num:
        params["kn"] = int(args.kn_num)
    else:
        params["kn"] = 0

    return params

# ///////////////////////////////////////////////////
# Execute
if __name__ == "__main__":

    try:
        Independence(chess()).play()

    except KeyboardInterrupt:
        print "\n"
