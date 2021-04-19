class RomanNumber:
    def __init__(self):
        self.rn = {1: "I", 5: "V", 10: "X",
                   50: "L", 100: "C", 500: "D", 1000: "M"}

    def fromInt(self, integer):
        print(f'integer {integer}')
        rn = self.__prefix(integer) + self.__major(integer) + \
            self.__suffix(integer)
        print(f'roman number {rn}')
        return rn

    def toInt(self, romanNumber):
        pass

    def __prefix(self, integer):
        prefix = self.rn[1] if ((integer + 1) % 5) == 0 and integer < 5 else ""
        prefix = self.rn[1] if ((integer + 1) %
                                10) == 0 and integer < 10 else prefix
        prefix = self.rn[10] if ((integer + 1) %
                                 50) == 0 and integer < 50 else prefix
        prefix = self.rn[10] if ((integer + 1) %
                                 100) == 0 and integer < 100 else prefix
        prefix = self.rn[100] if ((integer + 1) %
                                  500) == 0 and integer < 500 else prefix
        prefix = self.rn[100] if ((integer + 1) %
                                  1000) == 0 and integer < 1000 else prefix
        assert len(prefix) <= 1
        print(f'prefix {prefix}')
        return prefix

    def __major(self, integer):
        mN = self.__conversionNumber(integer + 10 ** (len(str(integer)) - 2))
        mRn = self.rn[mN]
        major = mRn
        if mN == 1:
            major = integer * mRn
        print(f'major {major}')
        return major

    def __suffix(self, integer):
        mN = self.__conversionNumber(integer)
        mN = self.__conversionNumber(integer + 10 ** (len(str(integer)) - 2))
        suffix = ""

        if integer >= 5 and (integer + 1) % mN != 0 or integer >= 10:
            suffix = self.fromInt(integer - mN)
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
