def char_range(first_number, second_number):
    list_of_strings = []
    for character in range(first_number + 1, second_number):
        list_of_strings.append(chr(character))
    return list_of_strings
first_string = input()
second_string = input()
first_string_number = ord(first_string)
second_string_number = ord(second_string)
print(" ".join(char_range(first_string_number,second_string_number)))