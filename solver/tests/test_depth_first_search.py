import unittest
import numpy as np

from solver.strategies.depth_first_search import DepthFirstSearch


class TestDepthFirstSearch(unittest.TestCase):

    def setUp(self):
        """ Runs before every test.
        """
        solved_field = np.array([[1,2,3,4,5,6,7,8,9],
                                 [4,5,6,7,8,9,1,2,3],
                                 [7,8,9,1,2,3,4,5,6],
                                 [2,3,1,5,6,4,8,9,7],
                                 [5,6,4,8,9,7,2,3,1],
                                 [8,9,7,2,3,1,5,6,4],
                                 [3,1,2,6,4,5,9,7,8],
                                 [6,4,5,9,7,8,3,1,2],
                                 [9,7,8,3,1,2,6,4,5]])

        unsolved_field = np.array([[1,2,3,4,5,6,7,8,9],
                                   [4,5,6,7,8,9,1,2,3],
                                   [7,8,9,1,2,3,4,5,6],
                                   [2,3,1,5,6,4,8,9,7],
                                   [5,6,4,8,9,7,2,3,1],
                                   [8,9,7,2,3,1,5,6,4],
                                   [3,1,2,6,4,5,9,7,8],
                                   [6,4,5,9,7,8,3,1,2],
                                   [9,7,8,3,1,2,6,4,np.nan]])

        self.solved_sudoku = DepthFirstSearch(solved_field)
        self.unsolved_sudoku = DepthFirstSearch(unsolved_field)

    def test_solve(self):
        field = [list(range(1, 10))]
        for i in range(8):
            field.append([0 for j in range(9)])
        field = np.array(field)
        DepthFirstSearch(field).solve()


if __name__ == '__main__':
    unittest.main()
