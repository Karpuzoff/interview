
__author__ = "Valery Karpuzoff"
__copyright__ = "Copyright (C) 2015 Valery Karpuzoff"

import polynom
import unittest


class PolynomTest(unittest.TestCase):

    def test(self):
        self.assertEqual("", polynom.simplify(""))

        self.assertEqual("1", polynom.simplify("1"))
        self.assertEqual("0", polynom.simplify("0"))
        self.assertEqual("0", polynom.simplify("00"))

        self.assertEqual("4x^2+4x+1", polynom.simplify("(2x+1)(2x+1)"))
        self.assertEqual("4x^2+4x+1", polynom.simplify("(2x+1)*(2x+1)"))
        self.assertEqual("4x^2+4x+1", polynom.simplify("(2x+1)^2"))
        self.assertEqual("4x^2+4x+1", polynom.simplify("(2x+1)^(1+1)"))
        self.assertEqual("4x^2", polynom.simplify("(2x)^(1+1)"))

        self.assertEqual("x^8+8x^7+28x^6+56x^5+70x^4+56x^3+28x^2+8x+1", polynom.simplify("(x+1)*(x+1)*(x+1)*(x+1)*(x+1)*(x+1)*(x+1)*(x+1)"))
        self.assertEqual("x^8+8x^7+28x^6+56x^5+70x^4+56x^3+28x^2+8x+1", polynom.simplify("(x+1)^(4+4)"))

        self.assertEqual("x^2+x", polynom.simplify("+x(x+1)"))
        self.assertEqual("-x^2-x", polynom.simplify("-x(x+1)"))
        self.assertEqual("x^2+x", polynom.simplify("x(x+1)"))

        self.assertEqual("27", polynom.simplify("-(-27)"))
        self.assertEqual("-27", polynom.simplify("-(+27)"))
        self.assertEqual("-27", polynom.simplify("+(-27)"))

        self.assertEqual("x^3+3x^2+2x", polynom.simplify("x(x+1)(x+2)"))
        self.assertEqual("x^2+x", polynom.simplify("x(x+1)"))
        self.assertEqual("x^2+x", polynom.simplify("(x(x+1))"))
        self.assertEqual("x^2+x+1", polynom.simplify("x+1+x^2"))
        self.assertEqual("3x^3-9x", polynom.simplify("2x^3+x(x^2-9)"))
        self.assertEqual("3x^3-9x", polynom.simplify("(2x^3+x(x^2-9))"))
        self.assertEqual("3x^4-15x^3-9x^2+45x", polynom.simplify("(x-5)(2x^3+x(x^2-9))"))

        self.assertEqual("x^2+3x+2", polynom.simplify("(x+1)(x+2)"))

        self.assertEqual("-345", polynom.simplify("23(4-5)(7+8)"))

        self.assertEqual("6x", polynom.simplify("3x*2"))
        self.assertEqual("6x", polynom.simplify("3x*(2)"))
        self.assertEqual("12x", polynom.simplify("3x*(2+2)"))
        self.assertEqual("x^2-4", polynom.simplify("(x-2)*(x+2)"))
        self.assertEqual("x^2-4", polynom.simplify("(x-2)(x+2)"))
        self.assertEqual("1", polynom.simplify("0x+1"))

        self.assertEqual("162x-1", polynom.simplify("-1+(5+4)(18x)"))
        self.assertEqual("-18x^2", polynom.simplify("(-18x)x"))
        self.assertEqual("-162x^2-x", polynom.simplify("-1x+(5+4)(-18x)x"))

        self.assertEqual("30", polynom.simplify("5*6"))
        self.assertEqual("30", polynom.simplify("(5)*(6)"))
        self.assertEqual("30x^4", polynom.simplify("x(5)x*x(6)x"))
        self.assertEqual("256", polynom.simplify("2^8"))
        self.assertEqual("65610", polynom.simplify("3^8*10"))
        self.assertEqual("120", polynom.simplify("1*2*3*4*5"))

        self.assertEqual("x^7-3x^6-2x^4+6x^3+x-3", polynom.simplify("(x-3)*(x^6-2x^3+1)"))

    def test_exponentiation(self):
        self.assertEqual("20x^8", polynom.simplify("2x^8*10"))
        self.assertEqual("8x^3", polynom.simplify("(2x)^3"))
        self.assertEqual("8x^3", polynom.simplify("(2x)^(3)"))
        self.assertEqual("16x^4", polynom.simplify("(2x)^((3)+(1))"))
        self.assertEqual("16x^4", polynom.simplify("((1+1)(x+0))^((3)+(1))"))
        self.assertEqual("65610", polynom.simplify("(2+1)^8*10"))

        self.assertEqual("16", polynom.simplify("2^2^2"))
        self.assertEqual("16", polynom.simplify("(1+1)^(2+0)^(2)"))

        self.assertEqual("0", polynom.simplify("0^2"))
        self.assertEqual("1", polynom.simplify("2^0"))
        self.assertEqual("1", polynom.simplify("x^0"))
        self.assertEqual("x", polynom.simplify("x^1"))

    def test_with_spaces(self):
        self.assertEqual("3x^3-9x", polynom.simplify("   2 x ^ 3  +    x  \t     (x^2-9)   "))

    def test_other_letters(self):
        self.assertEqual("y^2-1", polynom.simplify("(y+1)(y-1)"))
        self.assertRaises(ValueError, polynom.simplify, "(x+1)(X-1)")
        self.assertRaises(ValueError, polynom.simplify, "xy")
        self.assertRaises(ValueError, polynom.simplify, "x+y")

    def test_invalid_polynoms(self):
        self.assertRaises(ValueError, polynom.simplify, "!x(x+1)")
        self.assertRaises(ValueError, polynom.simplify, "x!(x+1)")
        self.assertRaises(ValueError, polynom.simplify, "x(x+1)!")
        self.assertRaises(ValueError, polynom.simplify, "x(x+1)-")
        self.assertRaises(ValueError, polynom.simplify, "-")
        self.assertRaises(ValueError, polynom.simplify, ")x")
        self.assertRaises(ValueError, polynom.simplify, "x(")

        self.assertRaises(ValueError, polynom.simplify, "1+()")
        self.assertRaises(ValueError, polynom.simplify, "x()+5")
        self.assertRaises(ValueError, polynom.simplify, "()()+5")

        self.assertRaises(ValueError, polynom.simplify, "1+)(+4")
        self.assertRaises(ValueError, polynom.simplify, ")()(")
        self.assertRaises(ValueError, polynom.simplify, "(1*)")
        self.assertRaises(ValueError, polynom.simplify, "1*2*3*")

        self.assertRaises(ValueError, polynom.simplify, "9(x)((x+2x)))")

        self.assertRaises(ValueError, polynom.simplify, "1+5++4")
        self.assertRaises(ValueError, polynom.simplify, "-1+(5+-4)")
        self.assertRaises(ValueError, polynom.simplify, "1+5+*4")
        self.assertRaises(ValueError, polynom.simplify, "1^^4")
        self.assertRaises(ValueError, polynom.simplify, "(1^)")

        self.assertRaises(ValueError, polynom.simplify, "xx")


###############################################################################


if __name__ == '__main__':
    unittest.main()
