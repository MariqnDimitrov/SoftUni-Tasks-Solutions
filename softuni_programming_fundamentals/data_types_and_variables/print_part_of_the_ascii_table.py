first_number = int(input())
second_number = int(input())
word = ""
for number in range(first_number, second_number + 1):
    letter = chr(number)
    print(letter, end=" ")