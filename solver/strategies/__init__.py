from abc import ABCMeta, abstractmethod
import numpy as np
import logging

logger = logging.getLogger()


class AbstractStrategy:
    __metaclass__ = ABCMeta

    def __init__(self, field):
        self.field = np.array(field, dtype='int32')
        if field.shape != (9, 9):
            raise ValueError("Sudoku has field needs to be of shape (9,9)!")
        self.needed_numbers = set(range(1, 10))

    @abstractmethod
    def solve(self):
        return

    def is_solved(self):
        for i in range(9):
            # check row
            row_numbers = set(self.field[i, :])
            missing_row_numbers = self.needed_numbers - row_numbers
            if len(missing_row_numbers) > 0:
                logger.info("Row {} misses number(s) {}".format(i+1, missing_row_numbers))
                return False

            # check column
            column_numbers = set(self.field[:, i])
            missing_column_numbers = self.needed_numbers - column_numbers
            if len(missing_column_numbers) > 0:
                logger.info("Column {} misses number(s) {}".format(i+1, missing_column_numbers))
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # check box
                box_numbers = set(np.ravel(self.field[i:i+3, j:j+3]))
                missing_box_numbers = self.needed_numbers - box_numbers
                if len(missing_box_numbers) > 0:
                    logger.info("Box ({},{}) misses number(s) {}".format((i%3)+1, (j%3)+1, missing_box_numbers))
                    return False
        # if we get here, then we passed all checks and the sudoku is solved
        return True
