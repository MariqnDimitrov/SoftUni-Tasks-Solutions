number = int(input())
for i in range(1, number + 1):
    word = input()
    pure = True
    for letter in range(len(word)):
        if word[letter] == ".":
            pure = False
        if word[letter] == ",":
            pure = False
        if word[letter] == "_":
            pure = False
    if pure == True:
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")