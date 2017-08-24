"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED == True:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(
        len(password)) + " character password is valid: " + password)

def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0

    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        count_lower = char.islower()
        if count_lower is True:
            number_of_lower = number_of_lower + 1
        count_upper = char.isupper()
        if count_upper is True:
            number_of_upper = number_of_upper + 1
        count_digit = char.isdigit()
        if count_digit is True:
            number_of_digit = number_of_digit + 1
        count_special = char in SPECIAL_CHARACTERS
        if count_special is True:
            number_of_special = number_of_special + 1

    # TODO: if any of the 'normal' counts are zero, return False
    if number_of_lower == 0:
        return False
    if number_of_upper == 0:
        return False
    if number_of_digit == 0:
        return False
    if number_of_special == 0:
        return False

    return True
main()
