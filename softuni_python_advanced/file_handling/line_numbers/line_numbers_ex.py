from string import punctuation
with open("line_numbers.txt", "r") as f:
    result = []
    for line_number, text in enumerate(f):
        char_count = 0
        punc_count = 0
        for char in text:
            if char.isalpha():
                char_count += 1
            elif char in punctuation:
                punc_count += 1
        result.append(f"Line {line_number + 1}: {text} ({char_count})({punc_count})")
with open("line_numbers_result.txt", "w") as f:
    f.write("\n".join(result))



