import unittest
import numpy as np

from solver.strategies.ilp_solver import ILPsolver


class TestILPSolver(unittest.TestCase):

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

        self.solved_sudoku = ILPsolver(solved_field)
        self.unsolved_sudoku = ILPsolver(unsolved_field)

    def test_is_solved(self):
        solved = self.solved_sudoku.is_solved()
        self.assertEqual(solved, True)
        solved = self.unsolved_sudoku.is_solved()
        self.assertEqual(solved, False)

    def test_create_constraints(self):
        """ Needs create variables to create constraints.
        """
        self.unsolved_sudoku.create_variables()
        self.unsolved_sudoku.add_constraints()
        self.assertEqual(len(self.unsolved_sudoku.var_dict), 729,
                         "The ILP problem doesn't have the expected number of 729 variables. (Instead has {})".format(
                             len(self.unsolved_sudoku.var_dict)))
        self.assertEqual(len(self.unsolved_sudoku.problem.constraints), 404,
                         "The ILP problem doesn't have the expected number of 404 constraints. (Instead has {})".format(
                             len(self.unsolved_sudoku.problem.constraints)))

    def test_ilp_solver(self):
        """ This is more of a regression test.
        """
        self.unsolved_sudoku.create_variables()
        self.unsolved_sudoku.add_constraints()
        self.unsolved_sudoku.optimize()
        solved_field = self.unsolved_sudoku.get_solution()
        # A status of 1 means optimal
        self.assertEqual(self.unsolved_sudoku.problem.status, 1)
        self.assertEqual(solved_field[8, 8], 5)


if __name__ == '__main__':
    unittest.main()
