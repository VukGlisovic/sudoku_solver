"""
Module that makes it easy to create a sudoku field that can be used to solve the problem.
"""

import numpy as np

class SuDoKu:

    def __init__(self, field):
        self.field = np.array(field)
        self.needed_numbers = set(range(1, 10))

    def is_solved(self):
        for i in range(9):
            # check row
            row_numbers = set(self.field[i, :])
            missing_row_numbers = self.needed_numbers - row_numbers
            if len(missing_row_numbers) > 0:
                print("Row {} misses number(s) {}".format(i+1, missing_row_numbers))
                return False

            # check column
            column_numbers = set(self.field[:, i])
            missing_column_numbers = self.needed_numbers - column_numbers
            if len(missing_column_numbers) > 0:
                print("Column {} misses number(s) {}".format(i+1, missing_column_numbers))
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # check box
                box_numbers = set(np.ravel(self.field[i:i+3, j:j+3]))
                missing_box_numbers = self.needed_numbers - box_numbers
                if len(missing_box_numbers) > 0:
                    print("Box ({},{}) misses number(s) {}".format((i%3)+1, (j%3)+1, missing_box_numbers))
                    return False
        # if we get here, then we passed all checks and the sudoku is fine
        return True
