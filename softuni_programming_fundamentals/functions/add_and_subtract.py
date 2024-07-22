def sum_numbers(first, second):
    sum_of_numbers = first + second
    return sum_of_numbers
def subtract(numbers_sum,third):
    subtracted_numbers = numbers_sum - third
    return subtracted_numbers
def add_and_subtract(number_one,number_two,number_three):
    add = sum_numbers(number_one,number_two)
    result = subtract(add,number_three)
    return result
first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number,second_number,third_number))