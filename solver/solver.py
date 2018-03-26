"""
Run this script with the the wanted input and get your output
"""
import argparse
import numpy as np
import importlib
import logging

logger = logging.getLogger()
log_format = '%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s - %(funcName)s | %(message)s'
logging.basicConfig(format=log_format, level=logging.INFO)


def load_strategy_class(strategy):
    """ Loads the class that will be used to solve the sudoku with.

    :param strategy: string, format <module_name>.<class_name>
    :return: class object
    """
    split_result = strategy.split('.')
    if len(split_result) != 2:
        raise ValueError("Expected following format for input: <module_name>.<class_name>")
    module_name, class_name = split_result
    logger.info("Loading module strategies.{}.".format(module_name))
    module = importlib.import_module("strategies.{}".format(module_name))
    logger.info("Loading solver class from retrieved module.")
    solver_class = getattr(module, class_name, None)
    if not solver_class:
        raise ValueError("Could not find class {} in module strategies.{}.".format(class_name, module_name))
    return solver_class


def get_field(field_location):
    with open(field_location, 'r') as f:
        field = []
        for line in f.readlines():
            numbers = line.strip('\n').split(',')
            numbers = list(map(lambda nr: int(nr) if nr else 0, numbers))
            field.append(numbers)
    return field


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--field_location',
                        type=str,
                        help="Path to the file with the SuDoKu.")
    parser.add_argument('--strategy',
                        type=str,
                        help="Combination of module name and class name with dot notation (module_name.class_name)")
    args = parser.parse_args()
    kwargs = args.__dict__
    # Using input to get and prepare the solver
    field = get_field(field_location=kwargs['field_location'])
    solver_class = load_strategy_class(strategy=kwargs['strategy'])
    solver = solver_class(field=field)
    solution = solver.solve()
    logger.info("Solution:\n" + str(solution))
    return solution


if __name__ == '__main__':
    main()
