command = ""
double_word = ""
while True:
    command = input()
    if command == "End":
        break
    if command == "SoftUni":
        continue
    for letter in range(len(command)):
        double_command = command[letter] + command[letter]
        double_word += double_command
    print(double_word)
    double_word = ""