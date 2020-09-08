# Copyright (c) 2020 Franklin Ikeh

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import unittest
from string import (
    ascii_letters as letters,
    ascii_lowercase as lowercase,
    ascii_uppercase as uppercase,
    octdigits,
    hexdigits,
    digits,
    punctuation,
    printable,
)
import randomchar
from randomchar import digit

conv_prefixes = ["0b", "0o", "0x"]


class Letter_test(unittest.TestCase):
    def test_no_parameter(self):
        self.assertIn(randomchar.letter(), letters)

    def test_param_zero(self):
        self.assertEqual(randomchar.letter(0), "")

    def test_length(self):
        self.assertEqual(len(randomchar.letter(6)), 6)

    def test_string(self):
        string = randomchar.letter(10)
        for letter in string:
            self.assertIn(letter, letters)


class LowerCase_test(unittest.TestCase):
    def test_no_parameter(self):
        self.assertIn(randomchar.lowerCase(), lowercase)

    def test_param_zero(self):
        self.assertEqual(randomchar.lowerCase(0), "")

    def test_length(self):
        self.assertEqual(len(randomchar.lowerCase(6)), 6)

    def test_string(self):
        string = randomchar.lowerCase(10)
        for letter in string:
            self.assertIn(letter, lowercase)


class UpperCase_test(unittest.TestCase):
    def test_no_parameter(self):
        self.assertIn(randomchar.upperCase(), uppercase)

    def test_param_zero(self):
        self.assertEqual(randomchar.upperCase(0), "")

    def test_length(self):
        self.assertEqual(len(randomchar.upperCase(6)), 6)

    def test_string(self):
        string = randomchar.upperCase(10)
        for letter in string:
            self.assertIn(letter, uppercase)


class Symbol_test(unittest.TestCase):
    def test_no_parameter(self):
        self.assertIn(randomchar.symbol(), punctuation)

    def test_param_zero(self):
        self.assertEqual(randomchar.symbol(0), "")

    def test_length(self):
        self.assertEqual(len(randomchar.symbol(6)), 6)

    def test_string(self):
        string = randomchar.symbol(10)
        for symbol in string:
            self.assertIn(symbol, punctuation)


class Printable_test(unittest.TestCase):
    def test_no_parameter(self):
        self.assertIn(randomchar.printable(), printable)

    def test_param_zero(self):
        self.assertEqual(randomchar.printable(0), "")

    def test_length(self):
        self.assertEqual(len(randomchar.printable(6)), 6)

    def test_string(self):
        string = randomchar.printable(10)
        for character in string:
            self.assertIn(character, printable)


class Octal_digit_test(unittest.TestCase):
    def test_no_parameter(self):
        self.assertIn(digit.octal(), octdigits)

    def test_param_zero(self):
        self.assertEqual(digit.octal(0), "")

    def test_length(self):
        self.assertEqual(len(digit.octal(6)), 6)

    def test_nozero(self):
        self.assertNotEqual(digit.octal(4)[0], 0)

    def test_string(self):
        numbers = digit.octal(10)
        for number in numbers:
            self.assertIn(number, octdigits)

    def test_arithmetic(self):
        x = int(digit.octal(4), 8)
        y = int(digit.octal(3), 8)
        sum = oct(x + y)
        for octd in str(sum)[2:]:
            self.assertIn(octd, octdigits)

    def test_conversion_prefix(self):
        num = oct(int(digit.octal(5), 8))
        self.assertIn(num[:2], conv_prefixes)


class Decimal_digit_test(unittest.TestCase):
    def test_no_parameter(self):
        self.assertIn(digit.decimal(), digits)

    def test_param_zero(self):
        self.assertEqual(digit.decimal(0), "")

    def test_length(self):
        self.assertEqual(len(digit.decimal(6)), 6)

    def test_nozero(self):
        self.assertNotEqual(digit.decimal(4)[0], 0)

    def test_string(self):
        numbers = digit.decimal(10)
        for number in numbers:
            self.assertIn(number, digits)

    def test_arithmetic(self):
        x = int(digit.decimal(4))
        y = int(digit.decimal(3))
        sum = x + y
        for decd in str(sum):
            self.assertIn(decd, digits)

    def test_conversion_prefix(self):
        num = str(int(digit.decimal(5)))
        self.assertNotIn(num[:2], conv_prefixes)


class Binary_digit_test(unittest.TestCase):
    def test_no_parameter(self):
        self.assertIn(digit.binary(), digit.binary_numbers)

    def test_param_zero(self):
        self.assertEqual(digit.binary(0), "")

    def test_length(self):
        self.assertEqual(len(digit.binary(6)), 6)

    def test_nozero(self):
        self.assertNotEqual(digit.binary(4)[0], 0)

    def test_string(self):
        numbers = digit.binary(10)
        for number in numbers:
            self.assertIn(number, digit.binary_numbers)

    def test_arithmetic(self):
        x = int(digit.binary(4), 2)
        y = int(digit.binary(3), 2)
        sum = bin(x + y)
        for bind in str(sum)[2:]:
            self.assertIn(bind, digit.binary_numbers)

    def test_conversion_prefix(self):
        num = bin(int(digit.binary(5), 2))
        self.assertIn(num[:2], conv_prefixes)


class Hexadecimal_digit_test(unittest.TestCase):
    def test_no_parameter(self):
        self.assertIn(digit.hexadecimal(), hexdigits)

    def test_param_zero(self):
        self.assertEqual(digit.hexadecimal(0), "")

    def test_length(self):
        self.assertEqual(len(digit.hexadecimal(6)), 6)

    def test_nozero(self):
        self.assertNotEqual(digit.hexadecimal(4)[0], 0)

    def test_string(self):
        numbers = digit.hexadecimal(10)
        for number in numbers:
            self.assertIn(number, hexdigits)

    def test_arithmetic(self):
        x = int(digit.hexadecimal(4), 16)
        y = int(digit.hexadecimal(3), 16)
        sum = hex(x + y)
        for hexd in str(sum)[2:]:
            self.assertIn(hexd, hexdigits)

    def test_conversion_prefix(self):
        num = hex(int(digit.hexadecimal(5), 16))
        self.assertIn(num[:2], conv_prefixes)
        
class User_set_test(unittest.TestCase):
    userDefined = "Good123($):"
    def test_no_length_parameter(self):
        self.assertIn(randomchar.user_set(self.userDefined), self.userDefined)
    
    def test_no_parameter(self):
        self.assertEqual(randomchar.user_set(),"")
    
    def test_length_param_zero(self):
        self.assertEqual(randomchar.user_set(self.userDefined, 0), "")

    def test_length(self):
        self.assertEqual(len(randomchar.user_set(self.userDefined, 6)), 6)

    def test_string(self):
        string = randomchar.user_set(self.userDefined, 10)
        for letter in string:
            self.assertIn(letter, self.userDefined)


if __name__ == "__main__":
    unittest.main()
