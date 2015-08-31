# -*- coding: utf-8 -*-

"""
    `coordinate` module is responsible for providing
    two dimensional coordinates
"""

# ///////////////////////////////////////////////////
# ---------------------------------------------------
# File: coordinate.py
# Author: Andreas Ntalakas <antalakas>
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# Python packages
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# My modules
# ---------------------------------------------------

# ///////////////////////////////////////////////////


class Coordinate(object):
    """
        `Coordinate` class is responsible for providing
        two dimensional coordinates
    """

    # ///////////////////////////////////////////////////
    def __init__(self, x, y):
        """
            `__init__()` initializes the necessary objects for using the
            Coordinate class.

            Attributes:
                * `self.x`           : x coordinate
                * `self.y`           : y coordinate
        """
        self.x = x
        self.y = y
