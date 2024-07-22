def even_odd(*args):
    command = args[-1]
    if command == "even":
        even_numbers = list(filter(lambda x: x % 2 == 0, args[:-1]))
        return even_numbers
    elif command == "odd":
        odd_numbers = list(filter(lambda x: x % 2 == 1, args[:-1]))
        return odd_numbers



print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))



