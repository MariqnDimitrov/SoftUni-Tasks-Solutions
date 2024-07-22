word = input()
final_word = ""
for letter in word:
    final_word += chr(ord(letter) + 3)
print(final_word)