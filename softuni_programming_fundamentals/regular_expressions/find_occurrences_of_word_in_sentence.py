import re
text = input()
searched_word = input()
pattern = fr"\b{searched_word}\b"
matches = re.findall(pattern, text, flags=re.IGNORECASE)
print(len(matches))