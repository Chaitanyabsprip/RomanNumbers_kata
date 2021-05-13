#! /usr/bin/python3.9
"""Convert to and from Roman numerals"""

__author__ = "Chaitanya Sharma (chaitanyasanjeevsharma@gmail.com)"
__version__ = "1.0"
__date__ = "20 April 2021"

import sys

from romannum.roman_numbers import RomanNumbers

from .subtractive_recursion import SubtractiveRecursion

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments")
        sys.exit(1)
    input_int: int = int(sys.argv[1])
    rn: RomanNumbers = SubtractiveRecursion()
    print(rn.fromInt(input_int))
