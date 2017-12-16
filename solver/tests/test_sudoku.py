import unittest
import numpy as np

from solver.create import SuDoKu


class TestSuDoKu(unittest.TestCase):

    def setUp(self):
        solved_field = np.array([[1,2,3,4,5,6,7,8,9],
                                 [4,5,6,7,8,9,1,2,3],
                                 [7,8,9,1,2,3,4,5,6],
                                 [2,3,1,5,6,4,8,9,7],
                                 [5,6,4,8,9,7,2,3,1],
                                 [8,9,7,2,3,1,5,6,4],
                                 [3,1,2,6,4,5,9,7,8],
                                 [6,4,5,9,7,8,3,1,2],
                                 [9,7,8,3,1,2,6,4,5]])
        self.sudoku = SuDoKu(solved_field)

    def test_is_solved(self):
        print(self.sudoku)
        return

if __name__ == '__main__':
    unittest.main()
