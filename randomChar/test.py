import unittest
import string
import randomChar

class TestSingleChar(unittest.TestCase):
    def test_Letter(self):
        """
        Test if the Letter() function returns a letter
        """
        test_result = string.ascii_letters
        result = randomChar.Letter()
        self.assertIn(result, test_result)
        
    def test_Digit(self):
        """
        Test if the Letter() function returns a letter
        """
        test_result = string.digits
        result = randomChar.Digit()
        self.assertIn(result, test_result)
        
    def test_Symbol(self):
        """
        Test if the Letter() function returns a letter
        """
        test_result = string.punctuation
        result = randomChar.Symbol()
        self.assertIn(result, test_result)
        
        
if __name__ == '__main__':
    print("randomChar v0.1.0-beta")
    unittest.main()