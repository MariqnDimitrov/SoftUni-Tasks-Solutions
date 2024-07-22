def palindrome_check(some_numbers):
    is_palindrome = False
    if some_numbers == some_numbers[::-1]:
        is_palindrome = True
        return is_palindrome
    return is_palindrome

list_of_numbers = input().split(", ")
for number in list_of_numbers:
    print(palindrome_check(number))