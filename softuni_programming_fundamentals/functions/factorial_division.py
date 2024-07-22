def factorial_division(first, second):
    first_number_factorial = first
    second_number_factorial = second
    for number in range(first - 1, 0, -1):
        first_number_factorial *= number
    for digit in range(second - 1, 0, -1):
        second_number_factorial *= digit
    total_factorial_sum = first_number_factorial / second_number_factorial
    return f"{total_factorial_sum:.2f}"


first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))