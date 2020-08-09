import random
import string
import secrets

def letter(length = 1):
    charSequence = []
    for i in range(length):
        charSequence.append(random.choice(string.ascii_letters))
        
    return ''.join(charSequence)


def loCase(length = 1):
    charSequence = []
    for i in range(length):
        charSequence.append(random.choice(string.ascii_lowercase))
        
    return ''.join(charSequence)


def upCase(length = 1):
    charSequence = []
    for i in range(length):
        charSequence.append(random.choice(string.ascii_uppercase))
        
    return ''.join(charSequence)


def digit(length = 1):
    charSequence = []
    for i in range(length):
        charSequence.append(random.choice(string.digits))
        
    return ''.join(charSequence)


def symbol(length = 1):
    charSequence = []
    for i in range(length):
        charSequence.append(random.choice(string.punctuation))
        
    return ''.join(charSequence)


def all(length = 1):
    charSequence = []
    for i in range(length):
        charSequence.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
        
    return ''.join(charSequence)
    
def password(length):
	charSequence = []
	
	for i in range(length):
	   charSequence.append(secrets.choice(string.ascii_letters + string.digits + string.punctuation))
	   
	random.shuffle(charSequence)
	return ''.join(charSequence)
    
if __name__ == "__main__":
    print(" ")
