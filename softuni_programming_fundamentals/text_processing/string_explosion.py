word = input()
final_word = ""
explosion_strength = 0
for index in range(len(word)):
    current_index = word[index]
    if word[index - 1] == ">":
        explosion_strength -= 1
        continue
    if word[index] == ">":
        final_word += word[index]
        explosion_strength += int(word[index + 1])
        continue

    if explosion_strength > 0:
        explosion_strength -= 1
    else:
        final_word += word[index]

print(final_word)