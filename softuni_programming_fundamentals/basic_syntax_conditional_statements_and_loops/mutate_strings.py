string_one = input()
string_two = input()
repeating_word = string_one
for letter in range(len(string_one)):
    word_one = string_two[:letter + 1]
    word_two = string_one[letter + 1:]
    word_three = word_one + word_two
    if word_three == repeating_word:
        continue
    print(word_three)
    repeating_word = word_three