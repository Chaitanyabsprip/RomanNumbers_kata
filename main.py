#! /usr/bin/python3.9

from roman_numbers import RomanNumber
import sys

if __name__ == '__main__':
    input_int = int(sys.argv[1])
    rn = RomanNumber()
    print(rn.fromInt(input_int))
