import random
import string
import secrets


def letter():
    return random.choice(string.ascii_letters)


def loCase():
    return random.choice(string.ascii_lowercase)


def upCase():
    return random.choice(string.ascii_uppercase)


def digit():
    return random.choice(string.digits)


def symbol():
    return random.choice(string.punctuation)


def all():
    randomCharList = [letter(), digit(), symbol()]
    return random.choice(randomCharList)
    
def password(length):
	charList = []
	
	for i in range(length):
	   charList.append(secrets.choice(string.ascii_letters + string.digits + string.punctuation))
	   
	random.shuffle(charList)
	return ''.join(charList)
    
if __name__ == "__main__":
    print("\nThis module was created by fr4nkl1n-1k3h\n")
    print(f"password(9): {password(9)}")
