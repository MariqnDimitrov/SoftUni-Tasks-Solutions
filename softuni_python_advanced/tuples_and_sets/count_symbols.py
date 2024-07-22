text = tuple(input())
char_in_text = sorted(set([char for char in text]))
for string in char_in_text:
    char_count = text.count(string)
    print(f"{string}: {char_count} time/s")


