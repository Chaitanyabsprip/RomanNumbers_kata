import unittest
from roman_numbers import RomanNumber


class TestRomanNumber(unittest.TestCase):

    def test_frominteger(self):
        rn = RomanNumber()

        # self.assertEqual(rn.fromInt(1), "I",
        #                  "should return 'I' for 1 as input")
        # self.assertEqual(rn.fromInt(2), "II",
        #                  "should return 'II' for 2 as input")
        # self.assertEqual(rn.fromInt(3), "III",
        #                  "should return 'III' for 3 as input")
        # self.assertEqual(rn.fromInt(4), "IV",
        #                  "should return 'IV' for 4 as input")
        # self.assertEqual(rn.fromInt(5), "V",
        #                  "should return 'V' for 5 as input")
        # self.assertEqual(rn.fromInt(6), "VI",
        #                  "should return 'VI' for 6 as input")
        # self.assertEqual(rn.fromInt(7), "VII",
        #                  "should return 'VII' for 7 as input")
        # self.assertEqual(rn.fromInt(8), "VIII",
        #                  "should return 'VIII' for 8 as input")
        # self.assertEqual(rn.fromInt(9), "IX",
        #                  "should return 'IX ' for 9 as input")
        # self.assertEqual(rn.fromInt(10), "X",
        #                  "should return 'X' for 10 as input")
        # self.assertEqual(rn.fromInt(11), "XI",
        #                  "should return 'XI' for 11 as input")
        # self.assertEqual(rn.fromInt(12), "XII",
        #                  "should return 'XII' for 12 as input")
        # self.assertEqual(rn.fromInt(13), "XIII",
        #                  "should return 'XIII' for 13 as input")
        # self.assertEqual(rn.fromInt(14), "XIV",
        #                  "should return 'XIV' for 14 as input")
        # self.assertEqual(rn.fromInt(15), "XV",
        #                  "should return 'XV' for 15 as input")
        # self.assertEqual(rn.fromInt(16), "XVI",
        #                  "should return 'XVI' for 16 as input")
        # self.assertEqual(rn.fromInt(17), "XVII",
        #                  "should return 'XVII' for 17 as input")
        # self.assertEqual(rn.fromInt(18), "XVIII",
        #                  "should return 'XVIII' for 18 as input")
        # self.assertEqual(rn.fromInt(19), "XIX",
        #                  "should return 'XIX' for 19 as input")
        # self.assertEqual(rn.fromInt(20), "XX",
        #                  "should return 'XX' for 20 as input")
        # self.assertEqual(rn.fromInt(40), "XL",
        #                  "should return 'XL' for 40 as input")
        # self.assertEqual(rn.fromInt(49), "XLIX",
        #                  "should return 'XLIX' for 49 as input")
        self.assertEqual(rn.fromInt(90), "XC",
                         "should return 'XC' for 90 as input")
        self.assertEqual(rn.fromInt(99), "XCIX",
                         "should return 'XCIX' for 99 as input")


if __name__ == "__main__":
    unittest.main()
