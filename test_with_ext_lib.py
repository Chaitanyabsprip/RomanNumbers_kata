import roman  # External library
from roman_numbers import RomanNumber

rn = RomanNumber()
test = True
for integer in range(1, 1001):
    if roman.toRoman(integer) == rn.toInt(integer):
        test and True
    else:
        test and False
        print(integer)
        break

if test:
    print("OK")
