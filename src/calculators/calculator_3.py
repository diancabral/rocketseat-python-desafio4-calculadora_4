from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from typing import List
from typing import Dict
from flask import Request as FlaskRequest


class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface):
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.get_json()
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)

        self.__verify_results(variance, multiplication)

        formated_response = self.__format_response(variance)

        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado!")

        input_data = body["numbers"]
        return input_data

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(
            numbers)
        return variance

    def __verify_results(self, variance: float, multiplication: float):
        if variance < multiplication:
            raise HttpBadRequestError(
                'Falha no processo: Variância menor que multiplicação')

    def __calculate_multiplication(self, numbers: List[float]):
        multiplication = 1
        for num in numbers:
            multiplication *= num
        return multiplication

    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "calculator": 3,
                "result": round(variance, 2),
                "success": True
            }
        }
