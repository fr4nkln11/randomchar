# randomchar
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


[![GitHub license](https://img.shields.io/github/license/fr4nkl1n-1k3h/randomchar)](https://github.com/fr4nkl1n-1k3h/randomchar/blob/master/LICENSE.txt)
[![Build Status](https://travis-ci.com/fr4nkl1n-1k3h/randomchar.svg?branch=master)](https://travis-ci.com/fr4nkl1n-1k3h/randomchar)
## What is `randomchar` ?
`randomchar` is a very simple solution to a very simple and common task, with the `randomchar` module you generate passwords, pseudo-emails or phone numbers for testing, unique id numbers, url tokens and other random strings by just calling a function and adding a parameter.

here is an example of why you might need randomchar:

```python
# without randomchar

import random
import string

# random password with 8 characters
password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8))

#with randomchar

import randomchar

# random password with 8 characters
password = randomchar.printable(8)
```

As you can now see the difference, you would notice that the same long code for generating random string passwords has been reduced to just a single function

The method used in the example is actually a one line representation of a much longer way to generate random strings
`randomchar` saves the python developer a lot of time from writing long patterns every time they wish to generate random strings

`randomchar` also has a `Digit()` class that helps in generating random digits in four number systems (Binary, Decimal, Octal, Hexadecimal).
There are two ways the `Digit()` class can be called after importing `randomchar`

*** Examples ***
By calling the class normally
* `randomchar.digit.decimal()`

By importing the class from the module
* `from randomchar import digit` and using as `digit.decimal()`


# Installation
This package has not been released to the Python Package Index (yet).


To install on Linux:
```bash
git clone https://github.com/fr4nkl1n-1k3h/randomchar
cd randomchar
pip install .
```
## Usage
```python
import randomchar
from randomchar import digit

randomchar.letter(5)
#returns a sequence of 5 random characters

randomchar.symbol(3)
#returns a sequence of 3 random symbolsa

digit.binary(7)
#returns a sequence of 7 random binary digits

digit.decimal(4)
#returns a seqduence of 4 random decimal digits

```

## Functions in `randomchar` and their parameters
***parameters
len: length of the required string, len = 1 by default
set: user defined character set

* letter(len)
* lowerCase(len)
* upperCase(len)
* symbol(len)
* printable(len)
* user_set(set, len)

**`Digit` class methods
* decimal(len)
* octal(len)
* binary(len)
* hexadecimal(len)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licences/mit/)
