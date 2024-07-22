sentence = input()
for index in range(len(sentence)):
    if sentence[index] == ":":
        print(f":{sentence[index+1]}")