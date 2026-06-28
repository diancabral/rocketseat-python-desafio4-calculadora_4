from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from typing import List
from src.drivers.numpy_handler import NumpyHandler
from typing import cast
from typing import Dict
from pytest import raises
from .calculator_2 import Calculator2, FlaskRequest


class MockRequest:
    def __init__(self, body: Dict):
        self.json = body

    def get_json(self):
        return self.json


class MockDriverHandler:
    def standard_derivation(self, numbers: List[float]):
        return 3


def test_calculate_integration():
    mock_request = cast(FlaskRequest, MockRequest(
        {"numbers": [2.12, 4.62, 1.32]}))

    calculator_2 = Calculator2(NumpyHandler())
    formated_response = calculator_2.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'calculator': 2, 'result': 0.08}}


def test_calculate():
    mock_request = cast(FlaskRequest, MockRequest(
        {"numbers": [2.12, 4.62, 1.32]}))

    calculator_2 = Calculator2(
        cast(DriverHandlerInterface, MockDriverHandler()))
    formated_response = calculator_2.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'calculator': 2, 'result': 0.33}}


def test_calculate_with_body_error():
    mock_request = cast(FlaskRequest, MockRequest({"foo": 1}))
    calculator_2 = Calculator2(NumpyHandler())

    with raises(Exception) as excinfo:
        calculator_2.calculate(mock_request)

    assert str(excinfo.value) == "Body mal formatado!"
