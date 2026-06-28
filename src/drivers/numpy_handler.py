from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from numpy import floating
from typing import List
import numpy


class NumpyHandler(DriverHandlerInterface):
    def __init__(self):
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return float(self.__np.std(numbers))

    def variance(self, numbers: List[float]) -> float:
        return float(self.__np.var(numbers))

    def mean(self, numbers: List[float]) -> float:
        return float(self.__np.mean(numbers))
