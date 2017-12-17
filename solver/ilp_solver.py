import pulp

class ILPsolver:

    def __init__(self, name="sudoku"):
        self.problem = pulp.LpProblem(name, pulp.LpMaximize)
        self.var_dict = dict()

    def create_variables(self):
        for i in range(9):  # Indicates row
            for j in range(9):  # Indicates column
                for k in range(1, 10):  # Indicates number from 1 till 9
                    var_name = 'x{row}{col}{nr}'.format(row=i, col=j, nr=k)
                    self.var_dict[var_name] = pulp.LpVariable(var_name, lowBound=0, upBound=1, cat=pulp.LpInteger)

    def add_constraints(self):
        # positional constraints
        for i in range(9):
            for j in range(9):
                constraint_var_names = ['x{row}{col}{nr}'.format(row=i, col=j, nr=nr) for nr in range(1, 10)]
                lp_variables = [self.var_dict[name] for name in constraint_var_names]
                c = sum(lp_variables) == 1
                self.problem += c, "pos_constr_{row}{col}".format(row=i, col=j)  # give the constraint a name

    def create_objective_function(self):
        pass

    def optimize(self):
        pass
