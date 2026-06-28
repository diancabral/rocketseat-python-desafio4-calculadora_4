from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_2 import Calculator2


def calculator2_factory():
    return Calculator2(NumpyHandler())
