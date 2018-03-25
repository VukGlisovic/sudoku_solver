from solver.strategies import AbstractStrategy
import pulp
import numpy as np
import logging

logger = logging.getLogger()


class ILPsolver(AbstractStrategy):

    def __init__(self, field, name="sudoku"):
        super(ILPsolver, self).__init__(field=field)
        self.problem = pulp.LpProblem(name, pulp.LpMaximize)
        self.var_dict = dict()
        self.n_variables = 9*9*9

    def create_variables(self):
        logger.info("Creating ILP variables.")
        for i in range(9):  # Indicates row
            for j in range(9):  # Indicates column
                for k in range(1, 10):  # Indicates number from 1 till 9
                    var_name = 'x{row}{col}{nr}'.format(row=i, col=j, nr=k)
                    self.var_dict[var_name] = pulp.LpVariable(var_name, lowBound=0, upBound=1, cat=pulp.LpInteger)

    def add_constraints(self):
        if len(self.var_dict) != self.n_variables:
            raise ValueError("Expected {} variables. Got {} variables as input.".format(self.n_variables, len(self.var_dict)))
        # positional constraints (every position can have only one number)
        for i in range(9):
            for j in range(9):
                constraint_var_names = ['x{row}{col}{nr}'.format(row=i, col=j, nr=nr) for nr in range(1, 10)]
                lp_variables = [self.var_dict[name] for name in constraint_var_names]
                c = sum(lp_variables) == 1
                self.problem += c, "positional_constraint_{row}{col}".format(row=i, col=j)  # give the constraint a name
        # rowwise constraints (every number can occur only once in a row)
        for i in range(9):
            for k in range(1, 10):
                constraint_var_names = ['x{row}{col}{nr}'.format(row=i, col=j, nr=k) for j in range(9)]
                lp_variables = [self.var_dict[name] for name in constraint_var_names]
                c = sum(lp_variables) == 1
                self.problem += c, "row_constraint_{row}{nr}".format(row=i, nr=k)
        # columnwise constraints (every number can occur only once in a column)
        for j in range(9):
            for k in range(1, 10):
                constraint_var_names = ['x{row}{col}{nr}'.format(row=i, col=j, nr=k) for i in range(9)]
                lp_variables = [self.var_dict[name] for name in constraint_var_names]
                c = sum(lp_variables) == 1
                self.problem += c, "column_constraint_{col}{nr}".format(col=j, nr=k)
        # boxwise constraints (every number can occur only once in a box)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(1, 10):
                    constraint_var_names = ['x{row}{col}{nr}'.format(row=i+p, col=j+q, nr=k) for p in range(3) for q in range(3)]
                    lp_variables = [self.var_dict[name] for name in constraint_var_names]
                    c = sum(lp_variables) == 1
                    self.problem += c, "box_constraint_{row}{col}{nr}".format(row=i, col=j, nr=k)

    def fill_known_numbers(self, sudoku):
        pass

    def create_objective_function(self):
        objective = sum(self.var_dict.values())
        self.problem += objective, "If optimized, the value should be 81."

    def optimize(self):
        self.problem.solve()
        logger.info("ILP solver status: {}".format(pulp.LpStatus[self.problem.status]))

    def get_solution(self):
        if self.problem.status != 1:
            raise ValueError("SuDoKu is not solved yet! Use the optimize method to solve the sudoku.")
        solved_field = np.zeros((9, 9), dtype="int32")
        for x___ in self.var_dict.keys():  # Gets the keys (x___ stands for e.g. x001)
            if self.var_dict[x___].varValue == 1:
                # If the ILP variable equals 1, this means the number corresponding to this variable is part of the solution
                solved_field[int(x___[1]), int(x___[2])] = int(x___[3])
        return solved_field

    def solve(self):
        return
