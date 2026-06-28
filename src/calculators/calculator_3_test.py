from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from pytest import raises
from typing import List
from typing import cast
from typing import Dict
from .calculator_3 import Calculator3, FlaskRequest


class MockRequest:
    def __init__(self, body: Dict):
        self.json = body

    def get_json(self):
        return self.json


class MockDriverHandlerError:
    def variance(self, numbers: List[float]):
        return 3


class MockDriverHandler:
    def variance(self, numbers: List[float]):
        return 1000000


def test_calculate_with_variance_error():
    mock_request = cast(FlaskRequest, MockRequest(
        {"numbers": [1, 2, 3, 4, 5]}))

    calculator_3 = Calculator3(
        cast(DriverHandlerInterface, MockDriverHandlerError()))
    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(
        excinfo.value) == 'Falha no processo: Variância menor que multiplicação'


def test_calculate():
    mock_request = cast(FlaskRequest, MockRequest(
        {"numbers": [1, 1, 1, 1, 100]}))

    calculator_3 = Calculator3(
        cast(DriverHandlerInterface, MockDriverHandler()))
    response = calculator_3.calculate(mock_request)

    assert response == {'data': {'calculator': 3,
                                 'result': 1000000, 'success': True}}
