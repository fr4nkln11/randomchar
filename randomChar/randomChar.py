import random
import string
import secrets

def Letter(length = 1):
    charSequence = []
    for i in range(length):
        charSequence.append(random.choice(string.ascii_letters))
        
    return ''.join(charSequence)


def LoCase(length = 1):
    charSequence = []
    for i in range(length):
        charSequence.append(random.choice(string.ascii_lowercase))
        
    return ''.join(charSequence)


def UpCase(length = 1):
    charSequence = []
    for i in range(length):
        charSequence.append(random.choice(string.ascii_uppercase))
        
    return ''.join(charSequence)


def Digit(length = 1):
    charSequence = []
    for i in range(length):
        charSequence.append(random.choice(string.digits))
        
    return ''.join(charSequence)


def Symbol(length = 1):
    charSequence = []
    for i in range(length):
        charSequence.append(random.choice(string.punctuation))
        
    return ''.join(charSequence)


def All(length = 1):
    charSequence = []
    for i in range(length):
        charSequence.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
        
    return ''.join(charSequence)
    
def Password(length):
	charSequence = []
	for i in range(length):
	   charSequence.append(secrets.choice(string.ascii_letters + string.digits + string.punctuation))
	   
	random.shuffle(charSequence)
	return ''.join(charSequence)
    
if __name__ == "__main__":
    print(" ")
