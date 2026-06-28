from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from typing import List
from src.drivers.numpy_handler import NumpyHandler
from typing import cast
from typing import Dict
from pytest import raises
from .calculator_4 import Calculator4, FlaskRequest


class MockRequest:
    def __init__(self, body: Dict):
        self.json = body

    def get_json(self):
        return self.json


class MockDriverHandler:
    def mean(self, numbers: List[float]):
        return 10.5


def test_calculate_integration():
    mock_request = cast(FlaskRequest, MockRequest(
        {"numbers": [1, 2, 3, 4, 5]}))

    calculator_4 = Calculator4(NumpyHandler())
    formated_response = calculator_4.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'calculator': 4, 'result': 3.0}}


def test_calculate():
    mock_request = cast(FlaskRequest, MockRequest(
        {"numbers": [9, 10, 11, 12]}))

    calculator_4 = Calculator4(
        cast(DriverHandlerInterface, MockDriverHandler()))
    formated_response = calculator_4.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'calculator': 4, 'result': 10.5}}


def test_calculate_with_body_error():
    mock_request = cast(FlaskRequest, MockRequest({"foo": 1}))
    calculator_4 = Calculator4(NumpyHandler())

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "Body mal formatado!"
