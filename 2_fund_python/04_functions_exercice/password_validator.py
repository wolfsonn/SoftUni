password_input = input()


def password_validation(password):
    if length_validation(password) and characters_validation(password) and digits_validation(password):
        print('Password is valid')
    if not length_validation(password):
        print('Password must be between 6 and 10 characters')
    if not characters_validation(password):
        print('Password must consist only of letters and digits')
    if not digits_validation(password):
        print('Password must have at least 2 digits')


def length_validation(password):
    if 5 < len(password) < 11:
        return True


def characters_validation(password):
    if password.isalnum():
        return True


def digits_validation(password):
    digits_count = len([i for i in password if i.isnumeric()])
    if digits_count >= 2:
        return True


password_validation(password_input)
