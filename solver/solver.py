"""
Run this script with the the wanted input and get your output
"""
import importlib
import logging

logger = logging.getLogger()
log_format = '%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s - %(funcName)s | %(message)s'
logging.basicConfig(format=log_format, level=logging.INFO)


def load_strategy_class(name):
    split_result = name.split('.')
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


def main():
    module = load_strategy_class('ilp_solver.ILPsolvers')
    return


if __name__ == '__main__':
    main()
