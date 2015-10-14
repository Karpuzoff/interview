
__author__ = "Valery Karpuzoff"
__copyright__ = "Copyright (C) 2015 Valery Karpuzoff"

import fraction
import unittest


class FractionTest(unittest.TestCase):

    # For testing i use online calculator from http://matworld.ru/calculator/perevod-chisel.php

    def test_base_16(self):
        self.assertEqual("0.0(B851E)", fraction.to_string(45, 1000, 16))
        self.assertEqual("2D.(E147A)", fraction.to_string(4588, 100, 16))

    def test_base_11(self):
        self.assertEqual("0.(0549932771)", fraction.to_string(45, 1000, 11))
        self.assertEqual("41.9(75309)", fraction.to_string(4588, 100, 11))

    def test_base_10(self):
        self.assertEqual("123", fraction.to_string(123, 1))
        self.assertEqual("50", fraction.to_string(100, 2))
        self.assertEqual("50.5", fraction.to_string(101, 2))

        self.assertEqual("0.(3)", fraction.to_string(1, 3))
        self.assertEqual("0.43(18)",   fraction.to_string(19, 44))

        self.assertEqual("10",   fraction.to_string(10, 1))
        self.assertEqual("1",   fraction.to_string(1, 1))
        self.assertEqual("0.1",   fraction.to_string(1, 10))

        self.assertEqual("1",   fraction.to_string(10, 10))
        self.assertEqual("2",   fraction.to_string(20, 10))
        self.assertEqual("0.2",   fraction.to_string(2, 10))

        self.assertEqual("0.39",   fraction.to_string(78, 200))

        self.assertEqual("0.5",   fraction.to_string(2, 4))
        self.assertEqual("0.33", fraction.to_string(33, 100))

        self.assertEqual("0.02", fraction.to_string(1, 50))

        self.assertEqual("0.08(3)", fraction.to_string(1, 12))

        self.assertEqual("0.(02)", fraction.to_string(2, 99))
        self.assertEqual("0.43(18)", fraction.to_string(19, 44))
        self.assertEqual("0.58(3)", fraction.to_string(7, 12))
        self.assertEqual("0.(641025)", fraction.to_string(25, 39))
        self.assertEqual("0.(6)", fraction.to_string(2, 3))

        self.assertEqual("0.(142857)", fraction.to_string(1, 7))

        self.assertEqual("1.(54)", fraction.to_string(17, 11))
        self.assertEqual("3066.(6)", fraction.to_string(9200, 3))

        self.assertEqual("155.25", fraction.to_string(621, 4))
        self.assertEqual("0.02625", fraction.to_string(21, 800))

        self.assertEqual("0.0219(37)", fraction.to_string(10859, 495000))

        self.assertEqual("1.(8235294117647058)", fraction.to_string(31, 17))
        self.assertEqual("18.(2352941176470588)", fraction.to_string(310, 17))

        self.assertEqual("0.5", fraction.to_string(1, 2))
        self.assertEqual("0.5", fraction.to_string(10, 20))
        self.assertEqual("0.5", fraction.to_string(100, 200))
        self.assertEqual("0.5", fraction.to_string(500, 1000))

    def test_base_9(self):
        self.assertEqual("0.03(5721754003)", fraction.to_string(45, 1000, 9))
        self.assertEqual("50.(7824610642)", fraction.to_string(4588, 100, 9))

    def test_base_8(self):
        self.assertEqual("0.4", fraction.to_string(1, 2, 8))
        self.assertEqual("0.4", fraction.to_string(2, 4, 8))
        self.assertEqual("0.4", fraction.to_string(4, 8, 8))
        self.assertEqual("0.4", fraction.to_string(8, 16, 8))

        self.assertEqual("0.2", fraction.to_string(1, 4, 8))
        self.assertEqual("0.2", fraction.to_string(2, 8, 8))
        self.assertEqual("0.1", fraction.to_string(1, 8, 8))

        self.assertEqual("1073", fraction.to_string(571, 1, 8))
        self.assertEqual("1073.4", fraction.to_string(571*2+1, 1*2, 8))

        self.assertEqual("0.24", fraction.to_string(3125, 10000, 8))

        self.assertEqual("0.52", fraction.to_string(65625, 100000, 8))

        self.assertEqual("0.0(27024365605075341217)", fraction.to_string(45, 1000, 8))
        self.assertEqual("55.(70243656050753412172)", fraction.to_string(4588, 100, 8))

    def test_base_7(self):
        self.assertEqual("0.(0213)", fraction.to_string(45, 1000, 7))
        self.assertEqual("63.(6105)", fraction.to_string(4588, 100, 7))

    def test_base_4(self):
        self.assertEqual("0.00(2320110132)", fraction.to_string(45, 1000, 4))
        self.assertEqual("231.(3201101322)", fraction.to_string(4588, 100, 4))

    def test_base_3(self):
        self.assertEqual("0.001(01221020121121100001)", fraction.to_string(45, 1000, 3))
        self.assertEqual("1200.(21220211200100201102)", fraction.to_string(4588, 100, 3))

    def test_base_2(self):
        self.assertEqual("0.1", fraction.to_string(50, 100, 2))
        self.assertEqual("0.0(0011)", fraction.to_string(10, 100, 2))

        self.assertEqual("10111", fraction.to_string(23, 1, 2))
        self.assertEqual("0.001", fraction.to_string(125, 1000, 2))

        self.assertEqual("10111.001", fraction.to_string(23125, 1000, 2))

        self.assertEqual("0.10(1001)", fraction.to_string(65, 100, 2))

        self.assertEqual("0.000(01011100001010001111)", fraction.to_string(45, 1000, 2))
        self.assertEqual("101101.1(11000010100011110101)", fraction.to_string(4588, 100, 2))

    def test_negative(self):
        self.assertEqual("50.5", fraction.to_string(+101, +2))
        self.assertEqual("-50.5", fraction.to_string(+101, -2))
        self.assertEqual("-50.5", fraction.to_string(-101, +2))
        self.assertEqual("50.5", fraction.to_string(-101, -2))

    def test_raises(self):
        self.assertRaises(ValueError, fraction.to_string, 1, 1, 1)
        self.assertRaises(ValueError, fraction.to_string, 1, 1, 17)
        self.assertRaises(ValueError, fraction.to_string, 1, 0, 10)


###############################################################################


if __name__ == '__main__':
    unittest.main()
