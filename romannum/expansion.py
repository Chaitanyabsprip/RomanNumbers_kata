from .roman_numbers import RomanNumbers


class Expansion(RomanNumbers):
    def __init__(self):
        self.rn: dict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

    def fromInt(self, integer: int) -> str:
        pass

    def toInt(self, roman_number: str) -> int:
        pass

    # def __face_value(self, number: int, integer: int) -> int:
    #     pass

    # def __place_value(self, number: int, position: int) -> int:
    #     pass
