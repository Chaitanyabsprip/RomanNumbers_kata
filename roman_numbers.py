class RomanNumber:
    def __init__(self):
        self.rn = {1: "I", 5: "V", 10: "X",
                   50: "L", 100: "C", 500: "D", 1000: "M"}

    def fromInt(self, integer):
        print(f'integer {integer}')
        converted_roman_number = self.__prefix(integer) + self.__major(integer) + \
            self.__suffix(integer)
        print(f'roman number {converted_roman_number}')
        return converted_roman_number

    def toInt(self, romanNumber):
        pass

    def __prefix(self, integer):
        no_of_digits = len(str(integer))
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
        print(f'prefix {prefix}')
        return prefix

    def __major(self, integer):
        no_of_digits = len(str(integer))
        adjustment = 10 ** (no_of_digits - 1) if no_of_digits > 1 else 1
        mN = self.__conversionNumber(integer + adjustment)
        mRn = self.rn[mN]
        major = mRn
        if mN == 1:
            major = integer * mRn
            print(f'major {major}')
        return major

    def __suffix(self, integer):
        no_of_digits = len(str(integer))
        # mN = self.__conversionNumber(integer + 10 ** (no_of_digits - 2))
        adjustment = 10 ** (no_of_digits - 1) if no_of_digits > 1 else 0
        mN = self.__conversionNumber(integer + adjustment)
        aN_list = list(self.rn.keys())
        suffix = ""

        if integer >= 5 and (integer + 1) % mN != 0 or integer >= 10:
            if integer >= mN:
                suffix = self.fromInt(integer - mN)
            else:
                pN = aN_list[aN_list.index(mN) - 1]
                suffix = self.fromInt(integer - (mN - pN))
        print(f'suffix {suffix}')
        return suffix

    def __conversionNumber(self, integer):
        mN = 5 if (integer / 5) >= 1 else 1
        mN = 10 if (integer / 10) >= 1 else mN
        mN = 50 if (integer / 50) >= 1 else mN
        mN = 100 if (integer / 100) >= 1 else mN
        mN = 500 if (integer / 500) >= 1 else mN
        mN = 1000 if (integer / 1000) >= 1 else mN
        return mN
