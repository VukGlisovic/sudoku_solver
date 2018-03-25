import unittest
import numpy as np

from solver.create import SuDoKu
from solver.strategies.ilp_solver import ILPsolver


class TestILPSolver(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Runs once before all tests.
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

        cls.solved_sudoku = SuDoKu(solved_field)
        cls.unsolved_sudoku = SuDoKu(unsolved_field)

    def test_is_solved(self):
        solved = self.solved_sudoku.is_solved()
        self.assertEqual(solved, True)
        solved = self.unsolved_sudoku.is_solved()
        self.assertEqual(solved, False)

    def test_create_constraints(self):
        """ Needs create variables to create constraints.
        """
        solver = ILPsolver()
        solver.create_variables()
        solver.add_constraints()
        self.assertEqual(len(solver.var_dict), 729,
                         "The ILP problem doesn't have the expected number of 729 variables. (Instead has {})".format(len(solver.var_dict)))
        self.assertEqual(len(solver.problem.constraints), 324,
                         "The ILP problem doesn't have the expected number of 324 constraints. (Instead has {})".format(len(solver.problem.constraints)))

    def test_ilp_solver(self):
        solver = ILPsolver()
        solver.create_variables()
        solver.add_constraints()
        solver.optimize()
        # A status of 1 means optimal
        self.assertEqual(solver.problem.status, 1)



if __name__ == '__main__':
    unittest.main()
