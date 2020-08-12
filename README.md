# randomchar

## What is `randomchar` ?

## Installation
This package has not been released to the Python Package Index (yet).

## Usage
```python
import randomchar

randomchar.Letter(5)
#returns a sequence of 5 random characters
randomchar.Digit(9)
#returns a sequence of 9 random digits
randomchar.Symbol(3)
#returns a sequence of 3 random symbols
randomchar.Password(8)
#returns a secure sequence of 8 characters

randomchar.Letter()
#returns a single random letter
randomchar.Digit()
#returns a single random number
randomchar.Symbol()
#returns a single random symbol
randomchar.All()
#returns a single random character

```

## `randomchar` functions
* `Letter()` - This function returns a sequence of ramdom **letters**, if its called with out any arguments it returns just one random **letter**
* `LoCase()` - This function returns a sequence of ramdom **lowercase letters**, if its called with out any arguments it returns just one random **lowercase letter**
* `UpCase()` - This function returns a sequence of ramdom **uppercase letters**, if its called with out any arguments it returns just one random **uppercase letter**
* `Digit()` - This function returns a sequence of ramdom **digits**, if its called with out any arguments it returns just one random **digit**
* `Symbol()` - This function returns a sequence of ramdom **symbols**, if its called with out any arguments it returns just one random **symbol**
* `All()` - This function returns a sequence of ramdom **character**, if its called with out any arguments it returns just one random **character**
* `Password()`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licences/mit/)
