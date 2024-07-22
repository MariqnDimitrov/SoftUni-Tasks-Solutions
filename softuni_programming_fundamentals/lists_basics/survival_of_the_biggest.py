list_of_strings = input().split(" ")
removed_numbers = int(input())
list_of_numbers= []
removed_elements = len(list_of_strings) - removed_numbers
for numbers in list_of_strings:
    list_of_numbers.append(int(numbers))
new_list = list_of_strings
list_of_numbers.sort(reverse=True)
for element in list_of_numbers[len(list_of_numbers):removed_elements - 1:-1]:
    str_element = str(element)
    if str_element in new_list:
        new_list.remove(str_element)
print(", ".join(new_list))