from math import floor


"""Convert to and from Roman numerals"""

__author__ = "Chaitanya Sharma (chaitanyasanjeevsharma@gmail.com)"
__version__ = "1.0"
__date__ = "20 April 2021"

# Define exceptions


class RomanError(Exception):
    pass


class OutOfRangeError(RomanError):
    pass


class NotIntegerError(RomanError):
    pass


class RomanNumber:
    def __init__(self):
        self.rn = {1: "I", 5: "V", 10: "X",
                   50: "L", 100: "C", 500: "D", 1000: "M"}

    def fromInt(self, integer):
        """convert integer to Roman numeral"""
        if not isinstance(integer, int):
            raise NotIntegerError("decimals can not be converted")
        if not (-1 < integer < 5000):
            raise OutOfRangeError("number out of range (must be 0..4999)")

        converted_roman_number = self.__prefix(integer) + self.__major(integer) + \
            self.__suffix(integer)
        return converted_roman_number

    def toInt(self, romanNumber):
        pass

    def __prefix(self, integer):
        no_of_digits = len(str(integer))
        integer = int(str(integer)[0]) * 10 ** (len(str(integer)) - 1)
        adjustment = 10 ** (no_of_digits - 1) if no_of_digits > 1 else 1
        prefix = self.rn[1] if ((integer + adjustment) %
                                5) == 0 and integer < 5 else ""
        prefix = self.rn[1] if ((integer + adjustment) %
                                10) == 0 and integer < 10 else prefix
        prefix = self.rn[10] if ((integer + adjustment) %
                                 50) == 0 and integer < 50 else prefix
        prefix = self.rn[10] if ((integer + adjustment) %
                                 100) == 0 and integer < 100 else prefix
        prefix = self.rn[100] if ((integer + adjustment) %
                                  500) == 0 and integer < 500 else prefix
        prefix = self.rn[100] if ((integer + adjustment) %
                                  1000) == 0 and integer < 1000 else prefix
        assert len(prefix) <= 1
        return prefix

    def __major(self, integer):
        no_of_digits = len(str(integer))
        adjustment = 10 ** (no_of_digits - 1) if no_of_digits > 1 else 1
        numeric_equivalent = self.__conversionNumber(integer + adjustment)
        roman_digit = self.rn[numeric_equivalent]
        major = roman_digit
        if numeric_equivalent == 1:
            major = integer * roman_digit
        return major

    def __suffix(self, integer):
        no_of_digits = len(str(integer))
        adjustment = 10 ** (no_of_digits - 1) if no_of_digits > 1 else 0
        mN = self.__conversionNumber(integer + adjustment)
        aN_list = list(self.rn.keys())
        suffix = ""

        if integer >= 5 and (integer + 1) % mN != 0 or integer >= 10 and (
                integer + 10) % mN != 0 or integer >= 100:
            if integer >= mN:
                suffix = self.fromInt(integer - mN)
            else:
                pN = aN_list[2 * floor((aN_list.index(mN) - 1) / 2)]
                suffix = self.fromInt(integer - (mN - pN))
        return suffix

    def __conversionNumber(self, integer):
        mN = 5 if (integer / 5) >= 1 else 1
        mN = 10 if (integer / 10) >= 1 else mN
        mN = 50 if (integer / 50) >= 1 else mN
        mN = 100 if (integer / 100) >= 1 else mN
        mN = 500 if (integer / 500) >= 1 else mN
        mN = 1000 if (integer / 1000) >= 1 else mN
        return mN
