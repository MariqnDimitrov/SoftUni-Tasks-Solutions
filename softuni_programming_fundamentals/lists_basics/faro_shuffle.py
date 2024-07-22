strings = input().split()
number_of_shuffles = int(input())
left_part = []
right_part = []
shuffled_deck = strings
fully_shuffled_deck = []
middle = len(shuffled_deck) // 2
for shuffle in range(number_of_shuffles):
    for left_strings in shuffled_deck[0:middle]:
        left_part.append(left_strings)
    for right_strings in shuffled_deck[middle::]:
        right_part.append(right_strings)
    for cards in range(len(left_part)):
        fully_shuffled_deck.append(left_part[cards])
        fully_shuffled_deck.append(right_part[cards])
    shuffled_deck = fully_shuffled_deck
    fully_shuffled_deck = []
    left_part = []
    right_part = []
print(shuffled_deck)