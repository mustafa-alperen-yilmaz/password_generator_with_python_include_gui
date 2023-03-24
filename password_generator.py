import random
import string

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

def generate_password_with_option(option, length):
    if length < 8 or length > 25:
        return "Invalid password length. Please enter a number between 8 and 25."

    if option == 1:
        chars = string.ascii_lowercase
    elif option == 2:
        chars = string.ascii_uppercase
    elif option == 3:
        chars = string.ascii_letters + string.punctuation
    elif option == 4:
        chars = string.ascii_lowercase + string.digits
    elif option == 5:
        chars = string.ascii_uppercase + string.digits
    elif option == 6:
        chars = string.ascii_letters + string.digits
    elif option == 7:
        chars = string.ascii_lowercase + string.digits + string.punctuation
    elif option == 8:
        chars = string.ascii_uppercase + string.digits + string.punctuation
    elif option == 9:
        chars = string.ascii_letters + string.digits + string.punctuation

    password = generate_password(length, chars)
    return password