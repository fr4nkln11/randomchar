import unittest
from string import (
    ascii_letters as letters,
    ascii_lowercase as lowercase,
    ascii_uppercase as uppercase,
    octdigits,
    hexdigits,
    digits,
    punctuation,
)
import randomchar


class Letter_test(unittest.TestCase):
    def test_no_parameter(self):
        self.assertIn(randomchar.letter(), letters)

    def test_length(self):
        self.assertEqual(len(randomchar.letter(6)), 6)
    def test_negative_parameter(self):
    	self.assertEqual(randomchar.letter(-2), "")

    def test_string(self):
        string = randomchar.letter(5)
        for letter in string:
            self.assertIn(letter, letters)

class LowerCase_test(unittest.TestCase):
    def test_no_parameter(self):
        self.assertIn(randomchar.lowerCase(), lowercase)

    def test_length(self):
        self.assertEqual(len(randomchar.lowerCase(6)), 6)
    def test_negative_parameter(self):
    	self.assertEqual(randomchar.lowerCase(-2), "")

    def test_string(self):
        string = randomchar.lowerCase(5)
        for letter in string:
            self.assertIn(letter, lowercase)

if __name__ == "__main__":
    unittest.main()
