from typing import List
from abc import ABC, abstractmethod


class DriverHandlerInterface(ABC):
    @abstractmethod
    def standard_derivation(self, numbers: List[float]) -> float: pass

    @abstractmethod
    def variance(self, numbers: List[float]) -> float: pass

    @abstractmethod
    def mean(self, numbers: List[float]) -> float: pass
