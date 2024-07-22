def sorted_list_of_numbers(numbers):
    return sorted(numbers)

list_of_strings = input().split()
list_of_numbers = []
for string in list_of_strings:
    list_of_numbers.append(int(string))
print(sorted_list_of_numbers(list_of_numbers))