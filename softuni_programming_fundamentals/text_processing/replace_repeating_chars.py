word = input()
current_letter = ""
final_word = ""
for letter in word:
    if letter == current_letter:
        continue
    final_word += letter
    current_letter = letter
print(final_word)