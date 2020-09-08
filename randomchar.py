#!/usr/bin/env python3

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
# SOFTWARE

""" Easier way to generate random strings"""

from random import choice, shuffle
from string import (
    ascii_letters as letters,
    ascii_lowercase as lowercase,
    ascii_uppercase as uppercase,
    octdigits,
    hexdigits,
    digits,
    punctuation,
)


def letter(length: int = 1) -> str:
    """
    returns random letter strings

    :parameters:
    length: defines the length of the character sequence
    if length is not given, the function returns only a single character
    """

    return "".join(choice(letters) for i in range(length))


def lowerCase(length: int = 1) -> str:
    """
    returns random lowercase letter strings

    :parameters:
    length: defines the length of the character sequence
    if length is not given, the function returns only a single character
    """

    return "".join(choice(lowercase) for i in range(length))


def upperCase(length: int = 1) -> str:
    """
    returns random uppercase letter strings

    :parameters:
    length: defines the length of the character sequence
    if length is not given, the function returns only a single character
    """

    return "".join(choice(uppercase) for i in range(length))


def symbol(length: int = 1) -> str:
    """
    returns random punctuation strings

    :parameters:
    length: defines the length of the character sequence
    if length is not given, the function returns only a single character
    """

    return "".join(choice(punctuation) for i in range(length))


def printable(length: int = 1) -> str:
    """
    returns random printable strings except newlines, spaces and tabs

    :parameters:
    length: defines the length of the character sequence
    if length is not given, the function returns only a single character
    """

    return "".join(choice(letters + digits + punctuation) for i in range(length))


class Digit:
    """
    The purpose of this class is to generate
    random digits in four number systems,
    """

    binary_numbers = digits[0:2]

    def binary(self, length: int = 1) -> str:
        """
        returns binary numbers as strings

        :parameters:
        length: defines the length of the number sequence
        if length is not given, the function will return only a single binary number
        """
        if length == 1:
            return choice(self.binary_numbers)
        elif length > 1:
            return "1" + "".join(choice(self.binary_numbers) for _ in range(length - 1))
        elif length < 1:
            return ""

    def octal(self, length: int = 1) -> str:
        """
        returns octal numbers as strings

        :parameters:
        length: defines the length of the number sequence
        if length is not given, the function will return only a single octal number
        """
        if length == 1:
            return choice(octdigits)
        elif length > 1:
            return choice(octdigits[1:]) + "".join(
                choice(octdigits) for i in range(length - 1)
            )
        elif length < 1:
            return ""

    def decimal(self, length: int = 1) -> str:
        """
        returns decimal numbers as strings

        :parameters:
        length: defines the length of the number sequence
        if length is not given, the function will return only a single decimal number
        """
        if length == 1:
            return choice(digits)
        elif length > 1:
            return choice(digits[1:]) + "".join(
                choice(digits) for i in range(length - 1)
            )
        elif length < 1:
            return ""

    def hexadecimal(self, length: int = 1) -> str:
        """
        returns hexadecimal numbers as strings

        :parameters:
        length: defines the length of the character sequence
        if length is not given, the function will return only a single hexadecimal number
        """
        if length == 1:
            return choice(hexdigits)
        elif length > 1:
            return choice(hexdigits[1:]) + "".join(
                choice(hexdigits) for i in range(length - 1)
            )
        elif length < 1:
            return ""


digit = Digit()
"""an instance of the digit() class"""

def user_set(chars = "", length: int = 1) -> str:
    """
    returns a random string from a set of user_defined characters.
    :parameters:
     chars: defines the user_defined set of charcters
     e.g '12345', 'abcdefgls', ['a', 'n', 'l']
     
     length: defines the length of the character sequence
        if length is not given, the function will return only a single character from the set
    """
    if chars != "":
        return ''.join(choice(chars) for i in range(length))
    if chars == "":
        return ""
