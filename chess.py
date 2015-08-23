#!/usr/bin/env python

"""
    `chess` module collects input arguments and creates a
    dictionary to be used as an input to Independence class
"""

# -*- coding: utf-8 -*-

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
from .independence import Independence

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
        params["m"] = args.x_dim
    else:
        return False

    if args.y_dim:
        params["n"] = args.y_dim
    else:
        return False

    if args.k_num:
        params["k"] = args.k_num

    if args.q_num:
        params["q"] = args.q_num

    if args.r_num:
        args.params["r"] = args.r_num

    if args.b_num:
        params["b"] = args.b_num

    if args.kn_num:
        params["kn"] = args.kn_num

    return params

# ///////////////////////////////////////////////////
# Execute
if __name__ == "__main__":

    try:
        Independence(chess()).play()

    except KeyboardInterrupt:
        print "\n"
