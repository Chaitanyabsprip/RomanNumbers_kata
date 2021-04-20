#! /usr/bin/python3.9

from roman_numbers import RomanNumber
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid arguments")
        sys.exit(1)
    input_int = int(sys.argv[1])
    rn = RomanNumber()
    print(rn.fromInt(input_int))
