def even_numbers(some_numbers):
    list_of_even_numbers = []
    if some_numbers % 2 == 0:
        list_of_even_numbers.append(some_numbers)
        return list_of_even_numbers


list_of_strings = input().split()
list_of_numbers = []
for strings in list_of_strings:
    list_of_numbers.append(int(strings))
print(list(filter(even_numbers, list_of_numbers)))