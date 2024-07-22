with open("even_line.txt", "r") as f:
    for line_number, text in enumerate(f):
        if line_number % 2 == 0:
            for string in text:
                if string in "-,.!?":
                    text = text.replace(string, "@")
                elif "\n" in text:
                    text = text.replace("\n", "")
            text = text.split(" ")
            print(" ".join(text[::-1]))

