# -*- coding: utf-8 -*-

"""
    `position` module is responsible for providing
    position for a single piece
"""

# ///////////////////////////////////////////////////
# ---------------------------------------------------
# File: position.py
# Author: Andreas Ntalakas <antalakas>
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# Python packages
# ---------------------------------------------------

# ///////////////////////////////////////////////////
# My modules
# ---------------------------------------------------

# ///////////////////////////////////////////////////


class Position(object):
    """
        `Position` class is responsible for providing
    position for a single piece
    """

    # ///////////////////////////////////////////////////
    def __init__(self, x, y, kind):
        """
            `__init__()` initializes the necessary objects for using the
            Position class.

            Attributes:
                * `self.x`          : x coordinate
                * `self.y`          : y coordinate
                * `self.kind`       : kind of piece
        """
        self.x = x
        self.y = y
        self.kind = kind
