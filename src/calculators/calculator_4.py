from typing import cast
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from typing import List
from typing import Dict
from flask import Request as FlaskRequest


class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface):
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.get_json()
        input_data = self.__validate_body(body)
        mean: float = self.__calculate_mean(input_data)

        formated_response = self.__format_response(mean)

        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        numbers = cast(List[float], body.get("numbers"))
        if not numbers or not all(isinstance(num, (int, float)) for num in numbers):
            raise HttpUnprocessableEntityError("Body mal formatado!")

        return numbers

    def __calculate_mean(self, numbers: List[float]) -> float:
        mean = self.__driver_handler.mean(
            numbers)
        return mean

    def __format_response(self, mean: float) -> Dict:
        return {
            "data": {
                "calculator": 4,
                "result": round(mean, 2)
            }
        }
