def lenght_check(some_username):
    if 3 < len(some_username) < 16:
        return some_username


def letters_check(username1):
    if username1.isalnum() or "-" in username1 or "_" in username1:
        return username1


def username_check(username2):
    if lenght_check(username2) and letters_check(username2):
        return username2


username_list = input().split(", ")
for username in username_list:
    if username_check(username):
        print(username)