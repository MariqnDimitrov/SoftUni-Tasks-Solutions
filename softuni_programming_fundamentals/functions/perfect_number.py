def perfect_number_check(some_number):
    list_of_divisors = []
    for digit in range(1, some_number):
        if some_number % digit == 0:
            list_of_divisors.append(digit)
    if sum(list_of_divisors) == some_number:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())
print(perfect_number_check(number))