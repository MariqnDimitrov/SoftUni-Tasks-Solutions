def smallest_number(some_number):
    some_number = min(some_number)
    return some_number

first_number = int(input())
second_number = int(input())
third_number = int(input())
list_of_numbers = [first_number,second_number,third_number]
print(smallest_number(list_of_numbers))