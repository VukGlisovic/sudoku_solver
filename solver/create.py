"""
Module that makes it easy to create a sudoku field that can be used to solve the problem.
"""

import numpy as np

class SuDoKu:

    def __init__(self, field):
        self.field = field
        self.needed_numbers = set(range(1, 10))

    def is_solved(self):
        # check rows
        self.field