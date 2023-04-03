import argparse
import random
import string

def generate_password(length=12, special_characters=True):
    """
    Generate a random password of given length.
    If special_characters is True, include special characters in the password.
    """
    characters = string.ascii_letters + string.digits
    if special_characters:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description='Generate a random password.')
    parser.add_argument('length', type=int, default=12, nargs='?',
                        help='Length of the password (default: 12)')
    parser.add_argument('--no-special', dest='special', action='store_false',
                        help='Exclude special characters from the password')
    args = parser.parse_args()

    password = generate_password(length=args.length, special_characters=args.special)
    print(password)

if __name__ == '__main__':
    main()
