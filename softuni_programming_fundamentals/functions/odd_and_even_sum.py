def odd_and_even_sum(some_number):
    list_of_odd_numbers = []
    list_of_even_numbers = []
    for digits in some_number:
        digits = int(digits)
        if digits % 2 == 0:
            list_of_even_numbers.append(digits)
        else:
            list_of_odd_numbers.append(digits)
    odd_sum = sum(list_of_odd_numbers)
    even_sum = sum(list_of_even_numbers)
    return odd_sum, even_sum

number = input()
sum_of_odd_numbers, sum_of_even_numbers = odd_and_even_sum(number)
print(f"Odd sum = {sum_of_odd_numbers}, Even sum = {sum_of_even_numbers}")