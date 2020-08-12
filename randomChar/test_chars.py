import string
import randomChar

def test_Letter_char():
    test_result = string.ascii_letters
    result = randomChar.Letter()
    assert result in test_result
    
def test_LoCase_char():
    test_result = string.ascii_lowercase
    result = randomChar.LoCase()
    assert result in test_result
    
def test_UpCase_char():
    test_result = string.ascii_uppercase
    result = randomChar.UpCase()
    assert result in test_result
    
def test_Digit():
    test_result = string.digits
    result = randomChar.Digit()
    assert result in test_result
    
def test_Symbol():
    test_result = string.punctuation
    result = randomChar.Symbol()
    assert result in test_result
    
if __name__ == '__main__':
    print("randomChar v0.1.0-beta")