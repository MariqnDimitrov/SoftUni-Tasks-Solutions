factor = int(input())
count = int(input())
list_of_numbers = list()
for numbers in range(1, count + 1):
    number = numbers * factor
    list_of_numbers.append(number)
print(list_of_numbers)