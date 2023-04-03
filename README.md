# Random Password Generator in Python
This is a small Python project that allows you to generate random passwords with customizable options.

## Features
* Generates random passwords of custom length (default 12 characters).
* Includes special characters in the passwords (default yes).
* Customize password generation options via command-line arguments.
* Uses Python's argparse library to parse command-line arguments.

## Usage
To use this random password generator, simply run the generate_password.py file with the following optional arguments:

~~~ 
usage: generate_password.py [-h] [--no-special] [length]

Generate a random password.

positional arguments:
  length         Length of the password (default: 12)

optional arguments:
  -h, --help     show this help message and exit
  --no-special   Exclude special characters from the password
For example, to generate a 16-character password without including special characters, you can run:
~~~ 
css
~~~ 
python generate_password.py 16 --no-special
~~~ 
This will generate a random 16-character password without including special characters.

## Contributing
If you would like to contribute to this project, you can submit a pull request to the master branch. We are open to improvements and new features.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.



