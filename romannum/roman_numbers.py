class RomanNumbers:
    def __init__(self, cls):
        self.cls = cls

    def fromInt(self, integer):
        return self.cls.fromInt(integer)

    def toInt(self, romanNumber):
        self.cls.toInt(romanNumber)
