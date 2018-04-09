# Sudoku Solver

To solve your sudoku, run the solver.py module with two flags added:<br/>
`--field-location`
`--strategy`

`field-location` should point to a file where the sudoku is that needs to be solved. The sudoku is expected to be in a comma seperated format.
For `strategy` there currently are two options: ilp_solver.ILPsolver and depth_first_search.DepthFirstSearch.

Good luck solving sudokus ;)
