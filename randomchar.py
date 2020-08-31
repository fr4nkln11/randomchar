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
    
    return ''.join(choice(letters) for i in range(length))
    
def lowerCase(length: int = 1) -> str:
    """
    returns random lowercase letter strings
    
    :parameters:
    length: defines the length of the character sequence
    if length is not given, the function returns only a single character
    """
    
    return ''.join(choice(lowercase) for i in range(length))

def upperCase(length: int = 1) -> str:
    """
    returns random uppercase letter strings
    
    :parameters:
    length: defines the length of the character sequence
    if length is not given, the function returns only a single character
    """
    
    return ''.join(choice(uppercase) for i in range(length))

def symbol(length: int = 1) -> str:
    """
    returns random punctuation strings
    
    :parameters:
    length: defines the length of the character sequence
    if length is not given, the function returns only a single character
    """
    
    return ''.join(choice(punctuation) for i in range(length))

def printable(length: int = 1) -> str:
    """
    returns random printable strings except newlines, spaces and tabs
    
    :parameters:
    length: defines the length of the character sequence
    if length is not given, the function returns only a single character
    """
    
    return ''.join(choice(letters + digits + punctuation) for i in range(length))
    
def password(length: int) -> str:
	"""
    returns password string which consists of letters,
    digits and symbols
    
    :parameters:
    length: defines the length of the character sequence
    if length is not given, an error will occur
    """
    
	password = shuffle(list(printable(length)))
	return ''.join(password)
	
class digit:
    """
    The purpose of this class is to generate
    random digits in four number systems,
    decimal() and octal() returns integers,
    binary() and hexadecimal() returns strings.
    """
    binary_numbers = digits[0:2]
    
    def binary(self, length: int = 1) -> str:
        """
        returns binary numbers as strings
        
        :parameters:
        length: defines the length of the number sequence
        if length is not given, the function will return only a single binary number
        """
        
        return ''.join(choice(self.binary_numbers) for i in range(length))
        
    def octal(self, length: int = 1) -> int:
        """
        returns octal numbers as integers
        
        :parameters:
        length: defines the length of the number sequence
        if length is not given, the function will return only a single octal number
        """
        
        return int(''.join(choice(octdigits) for i in range(length)))
         
    def decimal(self, length: int = 1) -> int:
        """
        returns decimal numbers as integers
        
        :parameters:
        length: defines the length of the number sequence
        if length is not given, the function will return only a single decimal number
        """
        
        return int(''.join(choice(digits) for i in range(length)))
        
    def hexadecimal(self, length: int = 1) -> str:
        """
        returns hexadecimal numbers as strings
        
        :parameters:
        length: defines the length of the character sequence
        if length is not given, the function will return only a single hexadecimal number
        """
        
        return ''.join(choice(hexdigits) for i in range(length))
        
digit = digit()
"""an instance of the digit() class"""
    
if __name__ == "__main__":
    print(letter())
    print(digit.binary(6))
    print(digit.decimal(6))
    print(digit.hexadecimal(6))
    print(digit.octal(6))