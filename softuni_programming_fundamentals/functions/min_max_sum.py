def min_number(some_number):
    return min(some_number)
def max_number(other_number):
    return max(other_number)
def sum_of_numbers(numbers):
    return sum(numbers)

list_of_strings = input().split()
list_of_numbers = []
for string in list_of_strings:
    list_of_numbers.append(int(string))
print(f"The minimum number is {min_number(list_of_numbers)}")
print(f"The maximum number is {max_number(list_of_numbers)}")
print(f"The sum number is: {sum_of_numbers(list_of_numbers)}")