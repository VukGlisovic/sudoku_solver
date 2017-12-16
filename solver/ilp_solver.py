import pulp

class ILPsolver:

    def __init__(self, name="sudoku"):
        self.problem = pulp.LpProblem(name, pulp.LpMaximize)
        self.var_dict = dict()

    def create_variables(self):
        for i in range(9):  # Indicates row
            for j in range(9):  # Indicates column
                for k in range(1, 10):  # Indicates number from 1 till 9
                    var_name = 'x{row}{col}{nr}'.format(row=1, col=j, nr=k)
                    self.var_dict[var_name] = pulp.LpVariable(var_name, lowBound=0, upBound=1, cat=pulp.LpInteger)

    def create_constraints(self):
        # positional constraints
        for i in range(9):
            for j in range(9):
                constraint_var_names = ['x{row}{col}{nr}'.format(row=i, col=j, nr=nr) for nr in range(1, 10)]
                lp_variables = [self.var_dict[name] for name in self.var_dict.keys() if name in constraint_var_names]
                c = sum(lp_variables) == 1
                # c = var_dict['x' + str(i) + str(j) + '1'] + var_dict['x' + str(i) + str(j) + '2'] + var_dict[
                #     'x' + str(i) + str(j) + '3'] \
                #     + var_dict['x' + str(i) + str(j) + '4'] + var_dict['x' + str(i) + str(j) + '5'] + var_dict[
                #         'x' + str(i) + str(j) + '6'] \
                #     + var_dict['x' + str(i) + str(j) + '7'] + var_dict['x' + str(i) + str(j) + '8'] + var_dict[
                #         'x' + str(i) + str(j) + '9'] == 1
                self.problem += c, "pos_constr_{row}{col}".format(row=i, col=j)

    def create_objective_function(self):
        pass

    def optimize(self):
        pass
