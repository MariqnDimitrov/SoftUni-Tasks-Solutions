number_of_letters = int(input())
sum_of_letters = 0
for number in range(number_of_letters):
    letter = input()
    letter_number = ord(letter)
    sum_of_letters += letter_number
print(f"The sum equals: {sum_of_letters}")