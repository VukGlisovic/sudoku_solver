from . import AbstractStrategy
import numpy as np
import logging

logger = logging.getLogger()


class DepthFirstSearch(AbstractStrategy):

    def __init__(self, field, name="sudoku"):
        super(DepthFirstSearch, self).__init__(field=field)

    @staticmethod
    def cell_is_valid(cell_index, flattenedfield):
        proposed_value = flattenedfield[cell_index]
        # temporary reduce by one
        flattenedfield[cell_index] -= 1
        #     print("Cell value {}".format(proposed_value))
        if proposed_value == 0:
            flattenedfield[cell_index] += 1
            return False
        # check row
        row_start = cell_index // 9 * 9
        row_values = flattenedfield[row_start: row_start + 9]
        #     print("Row values {}".format(row_values))
        if proposed_value in row_values:
            flattenedfield[cell_index] += 1
            return False
        # check column
        column_nr = cell_index % 9
        column_values = flattenedfield[range(column_nr, 81, 9)]
        #     print("Column values {}".format(column_values))
        if proposed_value in column_values:
            flattenedfield[cell_index] += 1
            return False
        # check box
        box_start = cell_index // 3 * 3 - ((cell_index // 9) % 3) * 9
        box_indices = list(range(box_start, box_start + 3)) + \
                      list(range(box_start + 9, box_start + 12)) + \
                      list(range(box_start + 18, box_start + 21))
        box_values = flattenedfield[box_indices]
        #     print("Box values {}".format(box_values))
        if proposed_value in box_values:
            flattenedfield[cell_index] += 1
            return False
        # If we've reached this point, it's a valid value
        flattenedfield[cell_index] += 1
        return True

    def depth_search(self, flattenedfield):
        empty_cell_indices = np.where(flattenedfield == 0)[0]
        i = 0
        while i != len(empty_cell_indices):
            current_cell_index = empty_cell_indices[i]
            if i < 0:
                print(flattenedfield)
            if not self.cell_is_valid(current_cell_index, flattenedfield):
                # The cell is not correct, let's increment by one and check its validity
                flattenedfield[current_cell_index] += 1
                while flattenedfield[current_cell_index] == 9:
                    flattenedfield[current_cell_index] = 0
                    i -= 1
                    current_cell_index = empty_cell_indices[i]
                    flattenedfield[current_cell_index] += 1
            else:
                # The cell is valid (for now), let's continue to the next cell
                i += 1
        return flattenedfield

    def solve(self):
        flattenedfield = self.field.reshape(-1)
        return self.depth_search(flattenedfield)
