def get_primes(list_of_numbers: list):
    for number in list_of_numbers:
        if number < 2:
            continue
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            yield number

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))



