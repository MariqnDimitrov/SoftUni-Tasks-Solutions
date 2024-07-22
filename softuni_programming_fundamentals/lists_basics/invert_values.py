numbers = input().split(" ")
opposite_numbers_list = list()
for number in numbers:
    number = -int(number)
    opposite_numbers_list.append(number)
print(opposite_numbers_list)