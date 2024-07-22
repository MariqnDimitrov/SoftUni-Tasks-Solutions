def password_validation(password_check):
    length_of_the_password = len(password_check)
    password_is_valid = True
    if length_of_the_password < 6 or length_of_the_password > 10:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False
    if not password_check.isalnum():
        print("Password must consist only of letters and digits")
        password_is_valid = False
    digit_count = 0
    for character in password_check:
        if character.isdigit():
            digit_count += 1
    if digit_count < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False
    if password_is_valid:
        print("Password is valid")

password = input()
password_validation(password)