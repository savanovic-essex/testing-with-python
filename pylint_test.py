
# SOURCE OF CODE: https://docs.pylint.org/en/1.6.0/tutorial.html
""" docstring """
import string

SHIFT = 3
CHOICE = raw_input("would you like to encode or decode?")
WORD = (raw_input("Please enter text"))
LETTERS = string.ascii_letters + string.punctuation + string.digits
ENCODED = ''
if CHOICE == "encode":
    for _letter in WORD:
        if _letter == ' ':
            ENCODED = ENCODED + ' '
        else:
            x = LETTERS.index(_letter) + SHIFT
            ENCODED = ENCODED + LETTERS[x]
        if CHOICE == "decode":
            for _letter in WORD:
                if _letter == ' ':
                    ENCODED = ENCODED + ' '
                else:
                    x = LETTERS.index(_letter) - SHIFT
                    ENCODED = ENCODED + LETTERS[x]

print ENCODED
